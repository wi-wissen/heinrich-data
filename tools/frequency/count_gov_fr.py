#!/usr/bin/env python3
"""Count tokens in official French texts (all under the Licence Ouverte / Etalab 2.0, or official acts).

All sources are open data of the DILA (Direction de l'information légale et administrative):
  1. an:    Assemblée nationale debates (Journal officiel, compte rendu intégral), 2011-2026, every
            AN_STEP-th issue (https://echanges.dila.gouv.fr/OPENDATA/Debats/AN/<year>/AN_*.taz).
  2. senat: Sénat debates (Journal officiel, compte rendu intégral), 2011-2016 (the years the DILA offers),
            every SEN_STEP-th issue (.../Debats/SENAT/<year>/SEN_*.taz).
  3. legi:  Légifrance LEGI database (consolidated legislation), full export
            (.../LEGI/Freemium_legi_global_*.tar.gz, streamed): articles in force (ETAT = VIGUEUR) of codes,
            laws, organic laws, ordinances and the constitution. Articles are put in LEGI_BUCKETS buckets by
            article id; only the first LEGI_KEEP buckets are counted.
  4. sp:    service-public.gouv.fr practical guides (fiches pratiques) for individuals and for businesses
            (https://lecomarquage.service-public.gouv.fr/vdd/3.5/{part,pro}/zip/vosdroits-latest.zip),
            fiches F*.xml only, <Paragraphe>/<Titre> text, identical paragraphs counted once per fiche.
Debates: only speech paragraphs; speaker names, stage directions ("(Applaudissements ...)"), vote lists and
the table of contents are skipped, and so is the AN annex of amendments ("cahier bleu"). Everything is processed in memory; only counts are written.
Usage: count_gov_fr.py OUTDIR [part ...]   (parts: an senat legi sp; default: all)
"""
import gzip, html, io, os, re, subprocess, sys, tarfile, zipfile
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

DILA = "https://echanges.dila.gouv.fr/OPENDATA"
AN_YEARS, AN_STEP = range(2011, 2027), 5
SEN_YEARS, SEN_STEP = range(2011, 2017), 3
LEGI_BUCKETS, LEGI_KEEP = 20, 20
LEGI_NATURES = {"CODE", "LOI", "LOI_ORGANIQUE", "LOI_CONSTIT", "ORDONNANCE", "CONSTITUTION"}
SP_ZIPS = [("part", "https://lecomarquage.service-public.gouv.fr/vdd/3.5/part/zip/vosdroits-latest.zip"),
           ("pro", "https://lecomarquage.service-public.gouv.fr/vdd/3.5/pro/zip/vosdroits-latest.zip")]


def curl(url):
    return subprocess.run(["curl", "-sSfL", "--retry", "5", "--retry-delay", "3", "--retry-all-errors", url],
                          check=True, capture_output=True).stdout


def write(out, n, tot, init):
    tok.dump(out + ".tmp", tot, init)
    os.rename(out + ".tmp", out)
    return out, n


# ---------- debates ----------
def members(data):
    """Yield the XML documents in a DILA .taz (tar, possibly compress'd .Z, possibly a tar inside a tar)."""
    if data[:2] == b"\x1f\x9d":  # compress (.Z); gzip can decompress it
        data = subprocess.run(["gzip", "-dc"], input=data, check=True, capture_output=True).stdout
    elif data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    try:
        tf = tarfile.open(fileobj=io.BytesIO(data))
    except tarfile.ReadError:
        yield data
        return
    with tf:
        for m in tf:
            if m.isfile():
                yield from members(tf.extractfile(m).read())


DROP = re.compile(r"<(Sommaire|Metadonnees|Orateur|QualiteMouvement|Exposant|Denomination|Libelle|TitreStruct|"
                  r"LienInterneDocRef|ResultatVote|LigneResultat)\b[^>]*>.*?</\1>", re.S)
PI = re.compile(r"<\?[^>]*\?>")
PARA = re.compile(r"<Para\b[^>/]*>(.*?)</Para>", re.S)
TAGS = re.compile(r"<[^>]+>")
REACT = re.compile(r"\((?:Applaudissements|Exclamations|Rires|Sourires|Protestations|Murmures|Vives?|Mêmes|"
                   r"Brouhaha|Huées|Bruit|Mouvements?|Interruptions?|Approbation|Marques|Nouvelles|Plusieurs|"
                   r"Quelques|De nombreux|Mmes et MM|M\. |Mme |MM\. |La séance|Le scrutin|L'amendement|"
                   r"L’amendement)[^)]*\)")


def debate_text(x):
    x = x.replace("&#128;", " ")  # the DILA files use &#128; for a (narrow) no-break space
    x = PI.sub("", x)
    x = DROP.sub(" ", x)
    out = []
    for p in PARA.findall(x):
        t = re.sub(r"\s+", " ", html.unescape(TAGS.sub("", p))).strip()
        if not t or (t.startswith("(") and t.endswith(")")):
            continue
        t = REACT.sub(" ", t).strip(" .,")
        if t:
            out.append(t)
    return "\n".join(out)


def job_debate(a):
    url, out = a
    tok.set_lang("fr")
    if os.path.exists(out):
        return out, None
    for attempt in (1, 2):
        tot, init, n = Counter(), Counter(), 0
        try:
            for d in members(curl(url)):
                x = d.decode("utf-8", "replace")
                if "<Para" in x and "PublicationDANBleu" not in x[:1000]:  # skip the annex of amendments
                    n += tok.count_text(debate_text(x), tot, init)
            return write(out, n, tot, init)
        except (tarfile.TarError, OSError, EOFError, subprocess.CalledProcessError) as e:
            print("retry" if attempt == 1 else "skip", url, e, flush=True)
    return out, None


def jobs_debates(outdir, chamber, years, step, prefix):
    urls = []
    for y in years:
        idx = curl(f"{DILA}/Debats/{chamber}/{y}/").decode("utf-8", "replace")
        urls += [f"{DILA}/Debats/{chamber}/{y}/{f}" for f in sorted(set(re.findall(r'href="([A-Z]+_[\d_]+\.taz)"', idx)))]
    sel = urls[step // 2::step]
    return [(u, os.path.join(outdir, f"{prefix}_" + u.rsplit("/", 1)[1][:-4] + ".tsv")) for u in sel]


# ---------- Légifrance (LEGI) ----------
ARTI = re.compile(r"/code_et_TNC_en_vigueur/.*/article/.*/LEGIARTI(\d+)\.xml$")
ETAT = re.compile(r"<ETAT>([^<]*)</ETAT>")
NATURE = re.compile(r'<TEXTE\b[^>]*\bnature="([^"]*)"')
BLOC = re.compile(r"<BLOC_TEXTUEL>\s*<CONTENU>(.*?)</CONTENU>", re.S)
BLOCK_TAGS = re.compile(r"</?(?:p|br|div|blockquote|li|ul|ol|table|tr|td|th|h\d)\b[^>]*>", re.I)


def legi_text(c):
    c = BLOCK_TAGS.sub("\n", c)
    c = html.unescape(TAGS.sub(" ", c))
    c = html.unescape(TAGS.sub(" ", c))  # the article bodies are HTML escaped once more
    c = re.sub(r"<table\b.*?</table>", " ", c, flags=re.S | re.I)
    c = TAGS.sub(" ", c)
    return "\n".join(re.sub(r"[ \t ]+", " ", l).strip() for l in c.split("\n") if l.strip())


def run_legi(outdir):
    tok.set_lang("fr")
    outs = [os.path.join(outdir, f"legi_{b:02d}.tsv") for b in range(LEGI_KEEP)]
    if all(os.path.exists(o) for o in outs):
        print("legi done", flush=True)
        return
    idx = curl(f"{DILA}/LEGI/").decode("utf-8", "replace")
    name = sorted(set(re.findall(r'href="(Freemium_legi_global_[\d-]+\.tar\.gz)"', idx)))[-1]
    print("legi", name, flush=True)
    cnt = [(Counter(), Counter()) for _ in range(LEGI_KEEP)]
    ntok = [0] * LEGI_KEEP
    per_nature = Counter()
    seen = 0
    proc = subprocess.Popen(["curl", "-sSfL", "--retry", "5", f"{DILA}/LEGI/{name}"], stdout=subprocess.PIPE)
    with tarfile.open(fileobj=proc.stdout, mode="r|gz") as tf:
        for m in tf:
            if not m.isfile():
                continue
            mm = ARTI.search(m.name)
            if not mm:
                continue
            b = int(mm.group(1)) % LEGI_BUCKETS
            if b >= LEGI_KEEP:
                continue
            x = tf.extractfile(m).read().decode("utf-8", "replace")
            e, nat = ETAT.search(x), NATURE.search(x)
            if not e or e.group(1) != "VIGUEUR" or not nat or nat.group(1) not in LEGI_NATURES:
                continue
            c = BLOC.search(x)
            if not c:
                continue
            k = tok.count_text(legi_text(c.group(1)), *cnt[b])
            ntok[b] += k
            per_nature[nat.group(1)] += k
            seen += 1
            if seen % 20000 == 0:
                print("legi articles", seen, "tokens", sum(ntok), dict(per_nature), flush=True)
    proc.wait()
    for b in range(LEGI_KEEP):
        write(outs[b], ntok[b], *cnt[b])
    print("legi articles", seen, "tokens", sum(ntok), dict(per_nature), flush=True)


# ---------- service-public.gouv.fr ----------
SP_P = re.compile(r"<(Paragraphe|Titre)\b[^>]*>(.*?)</\1>", re.S)


def run_sp(outdir):
    tok.set_lang("fr")
    for kind, url in SP_ZIPS:
        out = os.path.join(outdir, f"sp_{kind}.tsv")
        if os.path.exists(out):
            continue
        tot, init, n, fiches = Counter(), Counter(), 0, 0
        with zipfile.ZipFile(io.BytesIO(curl(url))) as z:
            for name in sorted(z.namelist()):
                if not re.fullmatch(r"F\d+\.xml", os.path.basename(name)):
                    continue
                x = z.read(name).decode("utf-8", "replace")
                seen, texts = set(), []
                for _, p in SP_P.findall(x):
                    t = re.sub(r"\s+", " ", html.unescape(TAGS.sub(" ", p))).strip()
                    if t and t not in seen:
                        seen.add(t)
                        texts.append(t)
                n += tok.count_text("\n".join(texts), tot, init)
                fiches += 1
        write(out, n, tot, init)
        print(out, fiches, "fiches", n, "tokens", flush=True)


def main():
    outdir = sys.argv[1]
    parts = sys.argv[2:] or ["an", "senat", "legi", "sp"]
    os.makedirs(outdir, exist_ok=True)
    tok.set_lang("fr")
    for p in parts:
        if p in ("an", "senat"):
            jobs = (jobs_debates(outdir, "AN", AN_YEARS, AN_STEP, "an") if p == "an"
                    else jobs_debates(outdir, "SENAT", SEN_YEARS, SEN_STEP, "sen"))
            print(p, len(jobs), "jobs", flush=True)
            tn = 0
            with Pool(3) as pool:
                for out, n in pool.imap_unordered(job_debate, jobs):
                    tn += n or 0
                    print(out, n, "running", tn, flush=True)
        elif p == "legi":
            run_legi(outdir)
        elif p == "sp":
            run_sp(outdir)


if __name__ == "__main__":
    main()

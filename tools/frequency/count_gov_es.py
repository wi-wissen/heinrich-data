#!/usr/bin/env python3
"""Count tokens in official Spanish (es-ES) texts.

  1. boe:      BOE consolidated legislation (Agencia Estatal Boletín Oficial del Estado, open data API
               https://www.boe.es/datosabiertos/api/legislacion-consolidada): state-level norms in force
               (ámbito Estatal, vigencia not exhausted) of the ranks in BOE_RANKS. Per norm, the current
               (last) version of each preamble and precept block; headings, footnotes, signatures and tables are
               skipped. Norms are put in BOE_BUCKETS buckets by a hash of their id; one count file per bucket.
               Reuse conditions: https://www.boe.es/informacion/aviso_legal/index.php (commercial reuse allowed,
               source to be cited).
  2. congreso: Diario de Sesiones del Congreso de los Diputados, Pleno y Diputación Permanente, legislatures
               X-XIV (2011-2023; before the co-official languages were admitted in the chamber), every
               CONG_STEP-th number, full text as HTML from congreso.es. Only speech paragraphs: the summary, the
               headings, the speaker names ("El señor PRESIDENTE:"), stage directions ("(Aplausos)"), vote
               results and page markers are skipped; paragraphs that read as Catalan, Galician or Basque
               (function-word test, `foreign()`) are dropped.
Everything is processed in memory; only counts are written.
Usage: count_gov_es.py OUTDIR [part ...]   (parts: boe congreso; default: all)
"""
import hashlib, html, json, os, re, subprocess, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

UA = "heinrich-data/1.0 (frequency counts)"
BOE_API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada"
BOE_RANKS = {"Constitución", "Ley Orgánica", "Ley", "Real Decreto-ley", "Real Decreto Legislativo", "Real Decreto"}
BOE_BUCKETS = 10
CONG_LEGIS = [("X", 10, 400), ("XI", 11, 80), ("XII", 12, 250), ("XIII", 13, 80), ("XIV", 14, 350)]  # upper bounds
CONG_STEP = 1
CONG_URL = ("https://www.congreso.es/es/busqueda-de-intervenciones?p_p_id=intervenciones&p_p_lifecycle=0"
            "&p_p_state=normal&p_p_mode=view&_intervenciones_mode=mostrarTextoIntegro"
            "&_intervenciones_legislatura={leg}&_intervenciones_id_texto=(DSCD-{n}-PL-{num}.CODI.)")


def curl(url, accept=None):
    cmd = ["curl", "-sSfL", "-A", UA, "--retry", "5", "--retry-delay", "3", "--retry-all-errors", "-m", "300"]
    if accept:
        cmd += ["-H", f"Accept: {accept}"]
    return subprocess.run(cmd + [url], check=True, capture_output=True).stdout


def write(out, n, tot, init):
    tok.dump(out + ".tmp", tot, init)
    os.rename(out + ".tmp", out)
    return out, n


TAGS = re.compile(r"<[^>]+>")


# ---------- BOE consolidated legislation ----------
BLOQUE = re.compile(r'<bloque\b[^>]*\btipo="([^"]*)"[^>]*>(.*?)</bloque>', re.S)
VERSION = re.compile(r"<version\b[^>]*>(.*?)</version>", re.S)
P = re.compile(r'<p\b(?:[^>]*\bclass="([^"]*)")?[^>]*>(.*?)</p>', re.S)
P_SKIP = re.compile(r"^(?:nota_pie|firma|articulo|capitulo|titulo|seccion|centro|cita|anexo|tabla|imagen|subseccion)")


def boe_text(x):
    x = re.sub(r"<table\b.*?</table>", " ", x, flags=re.S | re.I)
    out = []
    for tipo, body in BLOQUE.findall(x):
        if tipo not in ("preambulo", "precepto"):
            continue
        vs = VERSION.findall(body)
        if not vs:
            continue
        for cls, p in P.findall(vs[-1]):  # the last version is the one in force
            if cls and P_SKIP.match(cls):
                continue
            t = re.sub(r"\s+", " ", html.unescape(TAGS.sub(" ", p))).strip()
            if t:
                out.append(t)
    return "\n".join(out)


def boe_norms():
    norms, off = [], 0
    while True:
        d = json.loads(curl(f"{BOE_API}?limit=5000&offset={off}", "application/json"))["data"]
        if not d:
            break
        norms += d
        off += len(d)
        if len(d) < 5000:
            break
    keep = [x for x in norms if x["ambito"]["texto"] == "Estatal" and x["vigencia_agotada"] == "N"
            and x["rango"]["texto"] in BOE_RANKS]
    return sorted({x["identificador"]: x for x in keep}.values(), key=lambda x: x["identificador"])


def bucket(ident):
    return int(hashlib.sha1(ident.encode()).hexdigest(), 16) % BOE_BUCKETS


def job_boe(norm):
    tok.set_lang("es")
    ident = norm["identificador"]
    try:
        x = curl(f"{BOE_API}/id/{ident}/texto", "application/xml").decode("utf-8", "replace")
    except subprocess.CalledProcessError as e:
        return ident, None, None, None
    time.sleep(0.5)
    tot, init = Counter(), Counter()
    n = tok.count_text(boe_text(x), tot, init)
    return ident, n, tot, init


def run_boe(outdir):
    outs = [os.path.join(outdir, f"boe_{b}.tsv") for b in range(BOE_BUCKETS)]
    if all(os.path.exists(o) for o in outs):
        print("boe done", flush=True)
        return
    norms = boe_norms()
    print("boe norms", len(norms), Counter(x["rango"]["texto"] for x in norms), flush=True)
    cnt = [(Counter(), Counter()) for _ in range(BOE_BUCKETS)]
    ntok, nnorm, failed = [0] * BOE_BUCKETS, [0] * BOE_BUCKETS, []
    manifest = open(os.path.join(outdir, "boe_manifest.tsv.txt"), "w", encoding="utf-8")
    with Pool(2) as pool:
        for k, (ident, n, tot, init) in enumerate(pool.imap(job_boe, norms)):
            if n is None:
                failed.append(ident)
                continue
            b = bucket(ident)
            cnt[b][0].update(tot); cnt[b][1].update(init)
            ntok[b] += n; nnorm[b] += 1
            manifest.write(f"{ident}\t{b}\t{n}\n")
            if k % 200 == 0:
                print("boe", k, ident, "tokens", sum(ntok), flush=True)
    for b in range(BOE_BUCKETS):
        write(outs[b], ntok[b], *cnt[b])
    print("boe tokens per bucket", ntok, "norms", nnorm, "failed", failed, flush=True)


# ---------- Congreso de los Diputados ----------
SPEAKER = re.compile(r"^(?:El|La) (?:señor|señora) [A-ZÁÉÍÓÚÑÜÀÈÒÏÇ][^:]{0,160}?:\s*")
SKIP_PARA = re.compile(r"^(?:- |Página \d|Comenzada la votación|Efectuada la votación|Se suspende la sesión|"
                       r"Se reanuda la sesión|Se levanta la sesión|Se abre la sesión|Eran? las? |"
                       r"En el caso de las intervenciones realizadas en las lenguas)")
STAGE = re.compile(r"\((?:[A-ZÁÉÍÓÚÑ¡¿]|muestra|señala|pausa|continúa|risas|aplausos|rumores)[^()]*\)")
# Function words that are frequent in Catalan, Galician or Basque but are not Spanish words (own list).
FOREIGN = set("""i els amb perquè això aquesta aquest aquests aquestes molt també avui nosaltres vostè vostès
senyor senyora gràcies però ens hem estem som és dels als més seva seu seus seves fer fins uns doncs encara allà
només ho li mai sempre tothom gaire
non coa ao aos unha unhas moi grazas tamén hoxe nós vostede xa polo pola isto iso onde agora
eta ez bat ere du dira dute baina hori hau eskerrik asko gara dugu egin behar dago zuek gu""".split())
SPANISH = set("""el la los las de del que y en un una es por con para se no lo al su sus como más pero este esta
estos estas han ha muy también hoy nosotros ustedes usted señor señora gracias eso esto ya donde ahora porque
sin sobre todo todos hay""".split())


def foreign(p):
    w = [x.lower() for x in tok.WORD.findall(p)]
    f = sum(x in FOREIGN for x in w)
    s = sum(x in SPANISH for x in w)
    return f > 0 and f >= s


def congreso_text(page):
    i = page.find('<p class="textoCompleto"')
    if i < 0:
        return None
    j = page.find("</div>", i)
    paras = []
    for p in re.split(r"<br\s*/?>\s*<br\s*/?>", page[i:j]):
        t = re.sub(r"\s+", " ", html.unescape(TAGS.sub(" ", p))).strip()
        if not t:
            continue
        if re.fullmatch(r"Página \d+", t):
            continue
        if paras and t[0].islower():  # paragraph cut by a page break
            paras[-1] += " " + t
        else:
            paras.append(t)
    out, started = [], False
    for t in paras:
        m = SPEAKER.match(t)
        if m:
            started = True
            t = t[m.end():]
        if not started or SKIP_PARA.match(t):
            continue
        letters = [c for c in t if c.isalpha()]
        if letters and sum(c.isupper() for c in letters) > 0.6 * len(letters):
            continue  # headings in capitals
        t = STAGE.sub(" ", t).strip()
        if t and not foreign(t):
            out.append(t)
    return "\n".join(out)


def job_congreso(a):
    leg, n, num, out = a
    tok.set_lang("es")
    if os.path.exists(out):
        return out, -1
    try:
        page = curl(CONG_URL.format(leg=leg, n=n, num=num)).decode("utf-8", "replace")
    except subprocess.CalledProcessError:
        return out, None
    time.sleep(1)
    text = congreso_text(page)
    if text is None:
        return out, None
    tot, init = Counter(), Counter()
    return write(out, tok.count_text(text, tot, init), tot, init)


def run_congreso(outdir):
    """Numbers have gaps (legislature X has none of the first ~50 online): try every CONG_STEP-th number up to the
    upper bound, stop after 40 misses in a row once a number was found."""
    tn = 0
    with Pool(2) as pool:
        for leg, n, top in CONG_LEGIS:
            num, misses, found = CONG_STEP // 2 + 1, 0, False
            while num <= top and (misses < 40 or not found):
                batch = [(leg, n, k, os.path.join(outdir, f"cong_{n}_{k:03d}.tsv"))
                         for k in range(num, min(num + 8 * CONG_STEP, top + 1), CONG_STEP)]
                num += 8 * CONG_STEP
                for out, k in pool.imap(job_congreso, batch):
                    if k is None:
                        misses += 1
                        continue
                    misses, found = 0, True
                    tn += max(k, 0)
                    print(out, k, "running", tn, flush=True)


def main():
    outdir = sys.argv[1]
    parts = sys.argv[2:] or ["boe", "congreso"]
    os.makedirs(outdir, exist_ok=True)
    tok.set_lang("es")
    for p in parts:
        {"boe": run_boe, "congreso": run_congreso}[p](outdir)


if __name__ == "__main__":
    main()

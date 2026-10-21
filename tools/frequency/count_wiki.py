#!/usr/bin/env python3
"""Count tokens in a systematic sample of German, English or French Wikipedia (pages-articles-multistream).

For several dump parts we read the (small) index, group the bz2 streams into chunks of 10 streams
(~1000 pages), pick evenly spaced chunks and fetch only those byte ranges. Text is processed in memory.
Usage: count_wiki.py OUTDIR [chunks_per_part=30] [lang=de]
English only: articles tagged {{Use American English}} are additionally counted into chunk_*.us.tsv,
articles tagged {{Use British English}}, {{Use Oxford spelling}} or {{EngvarB}} into chunk_*.gb.tsv.
"""
import bz2, os, re, subprocess, sys, html, random
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

LANG = "de"
BASE_TPL = "https://dumps.wikimedia.org/{lang}wiki/"
PARTS_DE = [  # (data file, index file)
    ("dewiki-latest-pages-articles-multistream2.xml-p297013p1262093.bz2", "dewiki-latest-pages-articles-multistream-index2.txt-p297013p1262093.bz2"),
    ("dewiki-latest-pages-articles-multistream3.xml-p1262094p2762093.bz2", "dewiki-latest-pages-articles-multistream-index3.txt-p1262094p2762093.bz2"),
    ("dewiki-latest-pages-articles-multistream5.xml-p6115465p7615464.bz2", "dewiki-latest-pages-articles-multistream-index5.txt-p6115465p7615464.bz2"),
    ("dewiki-latest-pages-articles-multistream6.xml-p12261245p13761244.bz2", "dewiki-latest-pages-articles-multistream-index6.txt-p12261245p13761244.bz2"),
]
_EN = ["2.xml-p41243p151573", "5.xml-p558392p958045", "8.xml-p2134112p2936260", "12.xml-p7054860p8554859",
       "18.xml-p23716198p25216197", "24.xml-p50564554p52064553"]
PARTS_EN = [(f"enwiki-latest-pages-articles-multistream{p}.bz2",
             "enwiki-latest-pages-articles-multistream-index" + p.replace(".xml", ".txt") + ".bz2") for p in _EN]
_FR = ["2.xml-p306135p1050822", "3.xml-p1050823p2550822", "4.xml-p2977215p4477214", "5.xml-p6702074p8202073",
       "6.xml-p10574284p12074283", "6.xml-p15074284p16574283"]
PARTS_FR = [(f"frwiki-latest-pages-articles-multistream{p}.bz2",
             "frwiki-latest-pages-articles-multistream-index" + p.replace(".xml", ".txt") + ".bz2") for p in _FR]
PARTS_BY_LANG = {"de": PARTS_DE, "en": PARTS_EN, "fr": PARTS_FR}
PARTS = PARTS_DE
BASE = BASE_TPL.format(lang="de")
STREAMS_PER_CHUNK = 10
DATE = "latest"

def curl(url, rng=None):
    cmd = ["curl", "-sSf", "--retry", "5", "--retry-delay", "3", url]
    if rng:
        cmd += ["-r", rng]
    return subprocess.run(cmd, check=True, capture_output=True).stdout

# ---------- wikitext cleaning ----------
TPL = re.compile(r"\{\{[^{}]*\}\}")
COMMENT = re.compile(r"<!--.*?-->", re.S)
REF = re.compile(r"<ref\b[^>]*?/>|<ref\b[^>]*>.*?</ref>", re.S | re.I)
BLOCK = re.compile(r"<(gallery|math|code|source|syntaxhighlight|pre|timeline|imagemap|score|chem|ce|hiero|poem_off|mapframe|maplink)\b.*?</\1>", re.S | re.I)
TABLE = re.compile(r"\{\|.*?\|\}", re.S)
TAG = re.compile(r"</?[A-Za-z][^>]*>")
FILE_LINE = re.compile(r"^\s*\[\[(?:Datei|File|Bild|Image|Kategorie|Category|Media):.*$", re.M | re.I)
FILE_LINE_FR = re.compile(r"^\s*\[\[(?:Fichier|File|Image|Catégorie|Category|Média|Media):.*$", re.M | re.I)
LINK = re.compile(r"\[\[(?:[^\[\]|]*\|)?([^\[\]|]*)\]\]")
EXTLINK = re.compile(r"\[(?:https?:)?//[^\s\]]+\s*([^\]]*)\]")
URL = re.compile(r"(?:https?://|www\.)\S+")
CUT_BY_LANG = {
    "de": re.compile(r"^==+\s*(Literatur|Weblinks|Einzelnachweise|Anmerkungen|Quellen|Siehe auch|Fußnoten|Belege|Filme|Diskografie|Werke|Schriften|Veröffentlichungen|Publikationen)\b.*$", re.M),
    "fr": re.compile(r"^==+\s*(Notes et références|Références|Notes|Liens externes|Voir aussi|Bibliographie|Annexes|Articles connexes|Sources|Discographie|Filmographie|Œuvres|Publications|Ouvrages|Principales publications)\b.*$", re.M),
    "en": re.compile(r"^==+\s*(References|External links|See also|Further reading|Notes|Bibliography|Sources|Works cited|Footnotes|Citations|Discography|Filmography|Works|Publications|Selected works|Selected publications|Literature|Notes and references)\b.*$", re.M),
}
CUT = CUT_BY_LANG["de"]
REDIRECT = ("#WEITERLE", "#REDIRECT")  # "#REDIRECTION" (fr) starts with "#REDIRECT" too
# English variety tags (Wikipedia maintenance templates that state the spelling variety of an article)
REGION_TAGS = [(re.compile(r"\{\{\s*Use American English\b", re.I), "us"),
               (re.compile(r"\{\{\s*(?:Use British English|Use Oxford spelling|EngvarB)\b", re.I), "gb")]
NS = re.compile(r"<ns>(\d+)</ns>")
PAGE = re.compile(r"<page>(.*?)</page>", re.S)
TEXT = re.compile(r"<text[^>]*>(.*?)</text>", re.S)

def clean(wt):
    wt = html.unescape(wt)
    # entities written as "&nbsp;" in wikitext are "&amp;nbsp;" in the dump XML: unescape a second time
    # (added 2026-10-21; the lists counted before were corrected with drop_forms.py instead of a recount)
    wt = html.unescape(wt)
    m = CUT.search(wt)
    if m:
        wt = wt[:m.start()]
    wt = COMMENT.sub("", wt)
    wt = REF.sub("", wt)
    wt = BLOCK.sub("", wt)
    wt = TABLE.sub("", wt)
    for _ in range(8):
        n = TPL.sub("", wt)
        if n == wt:
            break
        wt = n
    wt = (FILE_LINE_FR if LANG == "fr" else FILE_LINE).sub("", wt)
    for _ in range(3):
        wt = LINK.sub(r"\1", wt)
    wt = EXTLINK.sub(r"\1", wt)
    wt = URL.sub(" ", wt)
    wt = TAG.sub(" ", wt)
    wt = wt.replace("'''", "").replace("''", "")
    out = []
    for line in wt.split("\n"):
        s = line.strip()
        if s.startswith("="):
            continue  # headings
        if not s or s[0] in "{|!" or s.startswith("__") or s.startswith("[["):
            continue
        s = s.lstrip("*#:; ")
        s = s.strip("= ")
        out.append(s)
    return "\n".join(out)

def region_of(wt):
    if LANG != "en":
        return None
    head = wt[:3000]
    for rx, r in REGION_TAGS:
        if rx.search(head):
            return r
    return None

def setup(lang):
    global LANG, PARTS, BASE, CUT
    LANG, PARTS, BASE, CUT = lang, PARTS_BY_LANG[lang], BASE_TPL.format(lang=lang), CUT_BY_LANG[lang]
    tok.set_lang(lang)

def process_chunk(args):
    part_i, ci, start, end, outdir, lang = args
    setup(lang)
    path = os.path.join(outdir, f"chunk_{part_i}_{ci:05d}.tsv")
    if os.path.exists(path):
        return path, None
    data = curl(BASE + DATE + "/" + PARTS[part_i][0], f"{start}-{end - 1}")
    tot, init = Counter(), Counter()
    reg = tok.Regional()
    n = pages = 0
    while data:
        d = bz2.BZ2Decompressor()
        xml = d.decompress(data).decode("utf-8", "replace")
        data = d.unused_data
        for pm in PAGE.finditer(xml):
            p = pm.group(1)
            ns = NS.search(p)
            if not ns or ns.group(1) != "0":
                continue
            tm = TEXT.search(p)
            if not tm:
                continue
            wt = tm.group(1)
            if wt.lstrip()[:9].upper() in REDIRECT:
                continue
            txt = clean(wt)
            n += tok.count_text(txt, tot, init)
            reg.count(region_of(html.unescape(wt)), txt)
            pages += 1
    reg.dump(path)
    tok.dump(path + ".tmp", tot, init)
    os.rename(path + ".tmp", path)
    return path, (n, pages)

def main():
    outdir = sys.argv[1]
    per_part = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    lang = sys.argv[3] if len(sys.argv) > 3 else "de"
    setup(lang)
    os.makedirs(outdir, exist_ok=True)
    jobs = []
    for pi, (dfile, ifile) in enumerate(PARTS):
        idx = bz2.decompress(curl(BASE + DATE + "/" + ifile)).decode("utf-8")
        offs = sorted({int(l.split(":", 1)[0]) for l in idx.splitlines() if l})
        size = int(re.search(r"Content-Length: (\d+)", subprocess.run(["curl", "-sSIL", BASE + DATE + "/" + dfile], capture_output=True, text=True).stdout, re.I).group(1))
        offs.append(size)
        chunks = [(offs[i], offs[min(i + STREAMS_PER_CHUNK, len(offs) - 1)]) for i in range(0, len(offs) - 1, STREAMS_PER_CHUNK)]
        k = max(1, len(chunks) // per_part)
        for ci in range(k // 2, len(chunks), k):
            jobs.append((pi, ci, chunks[ci][0], chunks[ci][1], outdir, lang))
        print(f"part {pi}: {len(offs)-1} streams, {len(chunks)} chunks, taking every {k}th", flush=True)
    random.Random(1).shuffle(jobs)
    tn = tp = 0
    with Pool(4) as pool:
        for path, r in pool.imap_unordered(process_chunk, jobs):
            if r:
                tn += r[0]; tp += r[1]
            print(path, r, "running total tokens", tn, "pages", tp, flush=True)

if __name__ == "__main__":
    main()

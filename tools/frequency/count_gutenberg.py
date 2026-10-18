#!/usr/bin/env python3
"""Count tokens in German or English public-domain books from gutenberg.org (NOT projekt-gutenberg.org).

Reads the official catalog (pg_catalog.csv), selects Language == de (or en), downloads each plain text from
gutenberg.org/cache/epub/<id>/pg<id>.txt one at a time (polite delay), strips the Project Gutenberg
header/footer, counts tokens in memory and discards the text.
Usage: count_gutenberg.py OUTDIR CATALOG_CSV [max_tokens=35000000] [shard=0] [nshards=1]
Shards split the (fixed-order) book list so several polite workers can run in parallel; max_tokens is per shard.
Canonical authors (Goethe, Schiller, ...) are processed first, the rest in a fixed pseudo-random order.

English (lang=en): only books whose first person is an author (not an editor) and is listed in authors_en.py (American "us" or British "gb"
English), whose every named person (author, editor, translator; illustrators ignored) has a known death
year <= 1955 (public domain in the US and life + 70 years), at most 12 books per author. us and gb books
alternate and max_tokens is split evenly between them; each book is also written as book_<id>.<region>.tsv.
Usage: count_gutenberg.py OUTDIR CATALOG_CSV max_tokens shard nshards en
"""
import csv, os, re, subprocess, sys, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
import authors_en
from collections import Counter, defaultdict

CANON = ["Goethe", "Schiller", "Heine", "Kleist", "Fontane", "Kafka", "Storm", "Lessing", "Hauff", "Eichendorff",
         "Hoffmann, E. T. A", "Büchner", "Grillparzer", "Keller, Gottfried", "Meyer, Conrad", "Raabe", "Hesse",
         "Mann, Thomas", "Mann, Heinrich", "Rilke", "Brentano", "Novalis", "Tieck", "Grimm", "Andersen", "Busch, Wilhelm",
         "Hebbel", "Stifter", "Droste", "Hölderlin", "Wieland", "Herder", "Kant", "Nietzsche", "Schnitzler", "Hofmannsthal",
         "Hauptmann", "Wedekind", "Zweig", "Spyri", "Ebner-Eschenbach", "Marx", "Freud", "Gerstäcker", "May, Karl", "Heyse",
         "Keller", "Jean Paul", "Lenz", "Bürger", "Chamisso", "Uhland", "Mörike", "Fouqué", "Arnim", "Humboldt", "Schopenhauer"]
START = re.compile(r"\*\*\* ?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*\n", re.I)
END = re.compile(r"\*\*\* ?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK", re.I)

def fetch(i):
    for url in (f"https://www.gutenberg.org/cache/epub/{i}/pg{i}.txt", f"https://www.gutenberg.org/files/{i}/{i}-0.txt"):
        r = subprocess.run(["curl", "-sSf", "--retry", "3", "--retry-delay", "5", url], capture_output=True)
        if r.returncode == 0:
            return r.stdout.decode("utf-8", "replace")
    return None

MAX_DEATH, PER_AUTHOR = 1955, 12
YEARS = re.compile(r",\s*(?:(?:ca\.\s*)?\d{1,4}\??(?:\s*BCE)?)?\s*-\s*(?:ca\.\s*)?(\d{3,4})\??(?:\s*BCE)?\s*$")

def persons(authors):
    """(name, role) per person of a catalog author field."""
    out = []
    for p in authors.split(";"):
        p = p.strip()
        if not p:
            continue
        m = re.search(r"\s*\[([^\]]+)\]\s*$", p)
        role = m.group(1) if m else "Author"
        out.append((p[:m.start()] if m else p, role))
    return out

def en_region(r):
    ps = persons(r["Authors"])
    if not ps or ps[0][1] != "Author":
        return None
    for name, role in ps:
        if role == "Illustrator":
            continue
        m = YEARS.search(name)
        if not m or int(m.group(1)) > MAX_DEATH:
            return None
    first = ps[0][0]
    if any(first.startswith(k) for k in authors_en.US):
        return "us"
    if any(first.startswith(k) for k in authors_en.GB):
        return "gb"
    return None

def en_books():
    """Fixed-order list of (row, region): us and gb books alternate, at most PER_AUTHOR books per author."""
    rnd = random.Random(7)
    by = {"us": [], "gb": []}
    for r in ROWS:
        g = en_region(r)
        if g:
            by[g].append(r)
    out = {}
    for g, lst in by.items():
        rnd.shuffle(lst)
        seen = defaultdict(int)
        keep = []
        for r in lst:
            a = persons(r["Authors"])[0][0]
            if seen[a] < PER_AUTHOR:
                seen[a] += 1
                keep.append(r)
        out[g] = keep
    res = []
    for i in range(max(len(v) for v in out.values())):
        for g in ("us", "gb"):
            if i < len(out[g]):
                res.append((out[g][i], g))
    return res

ILLU = re.compile(r"\[(?:Illustration|Transcriber's Note|Footnote)[^\]]*\]", re.I)

def body(t):
    m = START.search(t)
    if m:
        t = t[m.end():]
    m = END.search(t)
    if m:
        t = t[:m.start()]
    t = t.replace("\r", "")
    # join hard-wrapped lines inside paragraphs; blank line = paragraph break
    t = re.sub(r"(?<!\n)\n(?!\n)", " ", t)
    t = t.replace("_", "")
    t = ILLU.sub(" ", t)
    return t

def main():
    outdir, catalog = sys.argv[1], sys.argv[2]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 35_000_000
    shard = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    nsh = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    lang = sys.argv[6] if len(sys.argv) > 6 else "de"
    tok.set_lang(lang)
    os.makedirs(outdir, exist_ok=True)
    global ROWS
    ROWS = rows = [r for r in csv.DictReader(open(catalog, encoding="utf-8")) if r["Language"] == lang and r["Type"] == "Text"]
    if lang == "en":
        books_list = en_books()[shard::nsh]
        caps = {"us": cap // 2, "gb": cap // 2}
    else:
        def canon(r):
            return any(c in r["Authors"] for c in CANON)
        rnd = random.Random(7)
        a = [r for r in rows if canon(r)]; b = [r for r in rows if not canon(r)]
        rnd.shuffle(a); rnd.shuffle(b)
        books_list = [(r, None) for r in (a + b)[shard::nsh]]
        caps = {None: cap}
    tot_all, done, books = 0, 0, 0
    per = defaultdict(int)
    manifest = open(os.path.join(outdir, f"manifest_{shard}.tsv"), "a", encoding="utf-8")
    for r, g in books_list:
        i = r["Text#"]
        path = os.path.join(outdir, f"book_{i}.tsv")
        if os.path.exists(path):
            k = int(open(path + ".n").read())
            tot_all += k; per[g] += k; books += 1
            continue
        if per[g] >= caps[g]:
            if all(per[x] >= caps[x] for x in caps):
                break
            continue
        t = fetch(i)
        time.sleep(2)
        if t is None:
            print("skip", i, flush=True); continue
        tot, init = Counter(), Counter()
        n = tok.count_text(body(t), tot, init)
        if g:
            tok.dump(path[:-4] + f".{g}.tsv", tot, init)
        tok.dump(path, tot, init)
        open(path + ".n", "w").write(str(n))
        manifest.write(f"{i}\t{r['Authors']}\t{r['Title'].splitlines()[0]}\t{n}" + (f"\t{g}" if g else "") + "\n"); manifest.flush()
        tot_all += n; per[g] += n; books += 1
        print(i, n, "total", tot_all, "books", books, flush=True)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Count tokens in German public-domain books from gutenberg.org (NOT projekt-gutenberg.org).

Reads the official catalog (pg_catalog.csv), selects Language == de, downloads each plain text from
gutenberg.org/cache/epub/<id>/pg<id>.txt one at a time (polite delay), strips the Project Gutenberg
header/footer, counts tokens in memory and discards the text.
Usage: count_gutenberg.py OUTDIR CATALOG_CSV [max_tokens=35000000] [shard=0] [nshards=1]
Shards split the (fixed-order) book list so several polite workers can run in parallel; max_tokens is per shard.
Canonical authors (Goethe, Schiller, ...) are processed first, the rest in a fixed pseudo-random order.
"""
import csv, os, re, subprocess, sys, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

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
    return t

def main():
    outdir, catalog = sys.argv[1], sys.argv[2]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 35_000_000
    shard = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    nsh = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    os.makedirs(outdir, exist_ok=True)
    rows = [r for r in csv.DictReader(open(catalog, encoding="utf-8")) if r["Language"] == "de" and r["Type"] == "Text"]
    def canon(r):
        return any(c in r["Authors"] for c in CANON)
    rnd = random.Random(7)
    a = [r for r in rows if canon(r)]; b = [r for r in rows if not canon(r)]
    rnd.shuffle(a); rnd.shuffle(b)
    tot_all, done, books = 0, 0, 0
    manifest = open(os.path.join(outdir, f"manifest_{shard}.tsv"), "a", encoding="utf-8")
    for r in (a + b)[shard::nsh]:
        i = r["Text#"]
        path = os.path.join(outdir, f"book_{i}.tsv")
        if os.path.exists(path):
            tot_all += int(open(path + ".n").read()); books += 1
            continue
        if tot_all >= cap:
            break
        t = fetch(i)
        time.sleep(2)
        if t is None:
            print("skip", i, flush=True); continue
        tot, init = Counter(), Counter()
        n = tok.count_text(body(t), tot, init)
        tok.dump(path, tot, init)
        open(path + ".n", "w").write(str(n))
        manifest.write(f"{i}\t{r['Authors']}\t{r['Title'].splitlines()[0]}\t{n}\n"); manifest.flush()
        tot_all += n; books += 1
        print(i, n, "total", tot_all, "books", books, flush=True)

if __name__ == "__main__":
    main()

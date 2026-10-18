#!/usr/bin/env python3
"""Count tokens in official German texts (works of authorities, Sec. 5 UrhG: no copyright).

1. Bundestag plenary protocols (bundestag.de open data): zip archives pp18/pp19 (plain text format) and
   the most recent individual XML protocols (WP 20/21, structured format, speech paragraphs only).
2. Federal laws and ordinances from gesetze-im-internet.de (one xml.zip per law, listed in gii-toc.xml).
Everything is processed in memory; only counts are written (one TSV per work/law batch).
Usage: count_gov.py OUTDIR WORKDIR
"""
import io, os, re, subprocess, sys, html, zipfile
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

BT_LISTS = ["1058442", "866354"]  # ajax filter lists of WP 21 and WP 20 protocols (first page = 20 newest each)
BT_ZIPS = ["https://www.bundestag.de/resource/blob/870686/pp19.zip", "https://www.bundestag.de/resource/blob/490392/pp18.zip"]

def curl(url):
    return subprocess.run(["curl", "-sSfL", "--retry", "5", "--retry-delay", "3", url], check=True, capture_output=True).stdout

TAGS = re.compile(r"<[^>]+>")
RP = re.compile(r'<p klasse="(?:J|J_1|O)">(.*?)</p>', re.S)
REACT = re.compile(r"\((?:Beifall|Zuruf|Zurufe|Heiterkeit|Widerspruch|Unruhe|Lachen|Vereinzelt|Glocke|Gegenruf|Abg\.)[^)]*\)")
LP = re.compile(r"<P[^>]*>(.*?)</P>", re.S)

def clean_plain(t):
    i = t.find("\nBeginn:")
    if i > 0:
        t = t[i:]
    t = re.sub(r"-\n(?=[a-zäöüß])", "", t)       # line-break hyphenation
    t = re.sub(r"(?<!\n)\n(?!\n)", " ", t)
    t = re.sub(r" ([.,;:!?])", r"\1", t)
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\([A-D]\)", " ", t)           # column markers
    return REACT.sub(" ", t)

def count_xml_bt(x):
    tot, init = Counter(), Counter()
    if "<TEXT>" in x[:2000]:
        n = tok.count_text(clean_plain(html.unescape(x.split("<TEXT>", 1)[-1])), tot, init)
    else:
        txt = "\n".join(html.unescape(TAGS.sub("", p)) for p in RP.findall(x))
        n = tok.count_text(REACT.sub(" ", txt), tot, init)
    return n, tot, init

def job_bt_zip(a):
    url, out = a
    if os.path.exists(out):
        return out, None
    data = curl(url)
    tot, init, n = Counter(), Counter(), 0
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for name in z.namelist():
            if name.endswith(".xml"):
                k, t, i = count_xml_bt(z.read(name).decode("utf-8", "replace"))
                n += k; tot.update(t); init.update(i)
    tok.dump(out, tot, init)
    return out, n

def job_bt_xml(a):
    url, out = a
    if os.path.exists(out):
        return out, None
    n, tot, init = count_xml_bt(curl(url).decode("utf-8", "replace"))
    tok.dump(out, tot, init)
    return out, n

def job_laws(a):
    urls, out = a
    if os.path.exists(out):
        return out, None
    tot, init, n = Counter(), Counter(), 0
    for u in urls:
        try:
            with zipfile.ZipFile(io.BytesIO(curl(u))) as z:
                for name in z.namelist():
                    if name.endswith(".xml"):
                        x = z.read(name).decode("utf-8", "replace")
                        txt = "\n".join(html.unescape(TAGS.sub("", p)) for p in LP.findall(x))
                        n += tok.count_text(txt, tot, init)
        except Exception as e:
            print("skip", u, e, flush=True)
    tok.dump(out, tot, init)
    return out, n

def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    jobs_zip = [(u, os.path.join(outdir, "bt_" + u.rsplit("/", 1)[1] + ".tsv")) for u in BT_ZIPS]
    jobs_xml = []
    for lid in BT_LISTS:
        page = curl(f"https://www.bundestag.de/ajax/filterlist/de/services/opendata/{lid}-{lid}").decode()
        for u in sorted(set(re.findall(r"https://www.bundestag.de/resource/blob/\d+/\d+\.xml", page))):
            jobs_xml.append((u, os.path.join(outdir, "bt_" + u.rsplit("/", 1)[1] + ".tsv")))
    toc = curl("https://www.gesetze-im-internet.de/gii-toc.xml").decode()
    laws = sorted(set(re.findall(r"<link>(http://www\.gesetze-im-internet\.de/[^<]+/xml\.zip)</link>", toc)))
    laws = [l.replace("http://", "https://") for l in laws]
    jobs_laws = [(laws[i:i + 25], os.path.join(outdir, f"laws_{i:05d}.tsv")) for i in range(0, len(laws), 25)]
    print(len(jobs_zip), len(jobs_xml), "protocol jobs;", len(laws), "laws", flush=True)
    with Pool(4) as pool:
        for fn, jobs in ((job_bt_zip, jobs_zip), (job_bt_xml, jobs_xml), (job_laws, jobs_laws)):
            for out, n in pool.imap_unordered(fn, jobs):
                print(out, n, flush=True)

if __name__ == "__main__":
    main()

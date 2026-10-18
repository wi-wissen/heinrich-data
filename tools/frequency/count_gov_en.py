#!/usr/bin/env python3
"""Count tokens in official English texts, American ("us") and British ("gb").

us (works of the US federal government, public domain under 17 U.S.C. 105), from govinfo.gov bulk data:
  1. Public Papers of the Presidents (PPP), 2009-2016: speeches, remarks, news conferences (<para> only).
  2. Federal Register daily issues: every 12th issue of 2023-2025 (<P>/<FP> paragraphs only, no tables).
gb (Open Government Licence v3.0 / Open Parliament Licence v3.0):
  3. House of Commons Hansard debates (via TheyWorkForYou's XML of the official report), every 8th
     sitting day 2015-2025, speech paragraphs only.
  4. UK Public General Acts (legislation.gov.uk), even years 2000-2024, first feed page (up to 20 acts) per year.
  5. GOV.UK news stories, speeches and guides (GOV.UK content API), English-locale pages only.
Everything is processed in memory; only counts are written. Each output file <name>.tsv is accompanied by
<name>.<region>.tsv with the same counts (so merge.py can fill the us/gb columns).
Usage: count_gov_en.py OUTDIR [part ...]   (parts: ppp fr hansard leg govuk; default: all)
"""
import html, json, os, re, subprocess, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
from collections import Counter

GOVINFO = "https://www.govinfo.gov/bulkdata"
TWFY = "https://www.theyworkforyou.com/pwdata/scrapedxml/debates/"
LEG = "https://www.legislation.gov.uk"
GOVUK = "https://www.gov.uk"
GOVUK_TYPES = [("news_story", 6000), ("speech", 3000), ("detailed_guide", 2000)]


def curl(url, accept=None):
    cmd = ["curl", "-sSfL", "--retry", "5", "--retry-delay", "3", "--retry-all-errors", url]
    if accept:
        cmd += ["-H", f"Accept: {accept}"]
    return subprocess.run(cmd, check=True, capture_output=True).stdout


INLINE = re.compile(r"<(?:A|E|SU|FTREF|PRTPAGE|em|i|b|strong|span|abbr|Emphasis|Strong|Citation|CitationSubRef|"
                    r"Abbreviation|Acronym|Term|Definition|SmallCaps|Superior|Inferior|Addition|Repeal|Substitution|"
                    r"CommentaryRef|Underline|Uppercase|Expanded|a|phrase)\b[^>]*/?>|</(?:A|E|SU|FTREF|em|i|b|strong|span|"
                    r"abbr|Emphasis|Strong|Citation|CitationSubRef|Abbreviation|Acronym|Term|Definition|SmallCaps|Superior|"
                    r"Inferior|Addition|Repeal|Substitution|CommentaryRef|Underline|Uppercase|Expanded|a|phrase)>")
TAGS = re.compile(r"<[^>]+>")


def strip(x):
    x = INLINE.sub("", x)
    x = TAGS.sub(" ", x)
    return html.unescape(x)


def paras(xml, rx):
    return "\n".join(re.sub(r"\s+", " ", strip(p)).strip() for p in rx.findall(xml))


def write(out, region, n, tot, init):
    tok.dump(out[:-4] + f".{region}.tsv", tot, init)
    tok.dump(out + ".tmp", tot, init)
    os.rename(out + ".tmp", out)
    return out, n


def count(texts):
    tot, init, n = Counter(), Counter(), 0
    for t in texts:
        n += tok.count_text(t, tot, init)
    return n, tot, init


# ---------- us ----------
PPP_P = re.compile(r"<para\b[^>]*>(.*?)</para>", re.S)
FR_P = re.compile(r"<(?:P|FP)\b[^>]*>(.*?)</(?:P|FP)>", re.S)
FR_TABLE = re.compile(r"<GPOTABLE\b.*?</GPOTABLE>", re.S)


def job_url(a):
    kind, url, out, region = a
    tok.set_lang("en")
    if os.path.exists(out):
        return out, None
    x = curl(url).decode("utf-8", "replace")
    if kind == "ppp":
        texts = [paras(x, PPP_P)]
    else:
        texts = [paras(FR_TABLE.sub(" ", x), FR_P)]
    return write(out, region, *count(texts))


def jobs_ppp(outdir):
    jobs = []
    for y in range(2009, 2017):
        d = json.loads(curl(f"{GOVINFO}/json/PPP/{y}", "application/json"))
        for f in d["files"]:
            if f["name"].endswith(".xml"):
                jobs.append(("ppp", f["link"], os.path.join(outdir, "ppp_" + f["name"][:-4] + ".tsv"), "us"))
    return jobs


def jobs_fr(outdir):
    issues = []
    for y in (2023, 2024, 2025):
        for m in range(1, 13):
            d = json.loads(curl(f"{GOVINFO}/json/FR/{y}/{m:02d}", "application/json"))
            issues += sorted(f["link"] for f in d["files"] if re.search(r"FR-\d{4}-\d\d-\d\d\.xml$", f["name"]))
    return [("fr", u, os.path.join(outdir, "fr_" + u.rsplit("/", 1)[1][:-4] + ".tsv"), "us") for u in issues[3::12]]


# ---------- gb ----------
HANS_P = re.compile(r"<speech\b[^>]*>(.*?)</speech>", re.S)
P = re.compile(r"<p\b[^>]*>(.*?)</p>", re.S)


def job_hansard(a):
    url, out = a
    tok.set_lang("en")
    if os.path.exists(out):
        return out, None
    x = curl(url).decode("utf-8", "replace")
    texts = [paras(s, P) for s in HANS_P.findall(x)]
    return write(out, "gb", *count(texts))


def jobs_hansard(outdir):
    idx = curl(TWFY).decode()
    files = sorted(set(re.findall(r'href="(debates(\d{4}-\d\d-\d\d)([a-z])\.xml)"', idx)))
    latest = {}
    for f, d, v in files:
        if "2015-01-01" <= d <= "2025-12-31":
            latest[d] = f  # sorted, so the last letter (newest version) wins
    days = sorted(latest)
    return [(TWFY + latest[d], os.path.join(outdir, f"hansard_{d}.tsv")) for d in days[5::8]]


LEG_TEXT = re.compile(r"<Text\b[^>]*>(.*?)</Text>", re.S)


def job_leg(a):
    year, out = a
    tok.set_lang("en")
    if os.path.exists(out):
        return out, None
    feed = curl(f"{LEG}/ukpga/{year}/data.feed").decode("utf-8", "replace")
    links = sorted(set(re.findall(r'href="http://www\.legislation\.gov\.uk/(ukpga/\d{4}/\d+)(?:/[\d-]+)?/data\.xml"', feed)))
    texts = []
    for l in links:
        try:
            x = curl(f"{LEG}/{l}/data.xml").decode("utf-8", "replace")
            texts.append(paras(x, LEG_TEXT))
        except subprocess.CalledProcessError as e:
            print("skip", l, e, flush=True)
        time.sleep(0.5)
    return write(out, "gb", *count(texts))


def jobs_leg(outdir):
    return [(y, os.path.join(outdir, f"leg_ukpga_{y}.tsv")) for y in range(2000, 2026, 2)]


def job_govuk(a):
    links, out = a
    tok.set_lang("en")
    if os.path.exists(out):
        return out, None
    texts = []
    for l in links:
        try:
            d = json.loads(curl(GOVUK + "/api/content" + l))
        except Exception as e:
            print("skip", l, e, flush=True)
            continue
        if d.get("locale", "en") != "en":
            continue
        body = (d.get("details") or {}).get("body") or ""
        if isinstance(body, list):
            body = " ".join(b.get("content", "") for b in body if isinstance(b, dict))
        body = re.sub(r"<table\b.*?</table>", " ", body, flags=re.S)
        texts.append(paras(body, re.compile(r"<(?:p|li|h2|h3)\b[^>]*>(.*?)</(?:p|li|h2|h3)>", re.S)))
        time.sleep(0.1)
    return write(out, "gb", *count(texts))


def jobs_govuk(outdir):
    jobs = []
    for typ, want in GOVUK_TYPES:
        links = []
        for start in range(0, want, 1000):
            d = json.loads(curl(f"{GOVUK}/api/search.json?filter_content_store_document_type={typ}"
                                f"&count=1000&start={start}&order=-public_timestamp&fields=link"))
            links += [r["link"] for r in d["results"] if r["link"].startswith("/")]
        for i in range(0, len(links), 200):
            jobs.append((links[i:i + 200], os.path.join(outdir, f"govuk_{typ}_{i // 200:03d}.tsv")))
    return jobs


def main():
    outdir = sys.argv[1]
    parts = sys.argv[2:] or ["ppp", "fr", "hansard", "leg", "govuk"]
    os.makedirs(outdir, exist_ok=True)
    tok.set_lang("en")
    plan = {"ppp": (job_url, jobs_ppp, 4), "fr": (job_url, jobs_fr, 4), "hansard": (job_hansard, jobs_hansard, 3),
            "leg": (job_leg, jobs_leg, 2), "govuk": (job_govuk, jobs_govuk, 3)}
    for p in parts:
        fn, mk, w = plan[p]
        jobs = mk(outdir)
        print(p, len(jobs), "jobs", flush=True)
        tn = 0
        with Pool(w) as pool:
            for out, n in pool.imap_unordered(fn, jobs):
                tn += n or 0
                print(out, n, "running", tn, flush=True)


if __name__ == "__main__":
    main()

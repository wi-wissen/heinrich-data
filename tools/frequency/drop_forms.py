#!/usr/bin/env python3
"""Remove forms that are counting artefacts from <lang>/frequency/forms.tsv and update STATS.md to match.

Usage: drop_forms.py FREQDIR FORM [FORM ...]
Used once (2026-10-21) for HTML entity names that the Wikipedia cleaning of de/en/fr counted as words (the
dumps write `&nbsp;` in wikitext as `&amp;nbsp;`, which `count_wiki.py` unescaped only once). The removed
counts are subtracted from the source and regional token totals and from the distinct-form counts; the
coverage curve and the top 50 are recomputed from the new forms.tsv (every coverage target up to 99 % lies
inside forms.tsv). Forms with count 1 are unchanged (a removed form has count >= 3).
"""
import os, re, sys

def num(s):
    return int(s.replace(",", ""))

def main():
    d, drop = sys.argv[1], set(sys.argv[2:])
    path = os.path.join(d, "forms.tsv")
    lines = open(path, encoding="utf-8").read().split("\n")
    header = lines[0].split("\t")
    rows = [l.split("\t") for l in lines[1:] if l]
    gone = [r for r in rows if r[0] in drop]
    keep = [r for r in rows if r[0] not in drop]
    if not gone:
        sys.exit("nothing to drop")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(header) + "\n")
        f.writelines("\t".join(r) + "\n" for r in keep)
    col = {h: i for i, h in enumerate(header)}
    regions = header[6:]
    sp = os.path.join(d, "STATS.md")
    s = open(sp, encoding="utf-8").read()
    removed = {c: sum(int(r[col[c]]) for r in gone) for c in ["wiki", "lit", "gov", "total"] + regions}
    nonzero = {c: sum(1 for r in gone if int(r[col[c]])) for c in ["wiki", "lit", "gov"] + regions}

    def src(m):
        name = m.group(1)
        return f"| {name} | {m.group(2)} | {num(m.group(3)) - removed[name]:,} | {num(m.group(4)) - nonzero[name]:,} |"
    s = re.sub(r"^\| (wiki|lit|gov) \| (\d+) \| ([\d,]+) \| ([\d,]+) \|$", src, s, flags=re.M)
    m = re.search(r"^\| \*\*total\*\* \| \| \*\*([\d,]+)\*\* \| ([\d,]+) \|$", s, re.M)
    all_tokens = num(m.group(1)) - removed["total"]
    all_distinct_old = num(m.group(2))
    s = s[:m.start()] + f"| **total** | | **{all_tokens:,}** | {num(m.group(2)) - len(gone):,} |" + s[m.end():]
    for r in regions:
        s = re.sub(rf"^\| {r} \| ([\d,]+) \| ([\d,]+) \|$",
                   lambda m: f"| {r} | {num(m.group(1)) - removed[r]:,} | {num(m.group(2)) - nonzero[r]:,} |", s, flags=re.M)
    kept_tokens = sum(int(r[1]) for r in keep)
    s = re.sub(r"Forms in `forms.tsv`: ([\d,]+) (\(.*?\)); they cover ([\d.]+) %",
               lambda m: f"Forms in `forms.tsv`: {num(m.group(1)) - len(gone):,} {m.group(2)}; they cover "
                         f"{100 * kept_tokens / all_tokens:.2f} %", s)
    # spelling pairs (English): per million tokens of each region
    if regions:
        tok_r = {r: num(re.search(rf"^\| {r} \| ([\d,]+) \|", s, re.M).group(1)) for r in regions}
        cnt = {r[0]: r for r in keep}
        def pair(m):
            a, b = m.group(1), m.group(2)
            f = lambda w, g: f"{1e6 * int(cnt[w][col[g]]) / tok_r[g]:.1f}" if w in cnt else "0.0"
            return f"| {a} | {f(a, 'us')} | {f(a, 'gb')} | {b} | {f(b, 'us')} | {f(b, 'gb')} |"
        s = re.sub(r"^\| ([a-z]+) \| [\d.]+ \| [\d.]+ \| ([a-z]+) \| [\d.]+ \| [\d.]+ \|$", pair, s, flags=re.M)
    # coverage curve
    cov, acc, targets = {}, 0, [0.80, 0.90, 0.95, 0.99]
    for rank, r in enumerate(keep, 1):
        acc += int(r[1])
        while targets and acc / all_tokens >= targets[0]:
            cov[targets.pop(0)] = rank
    # A target beyond forms.tsv (German: the list is capped at 500,000 forms) lies among the forms with count 1
    # (the last `Forms with count 1` ranks). All removed forms rank above it, so the old rank shifts by -k, and
    # the lower total needs (1 - t) * removed tokens less, i.e. that many forms of count 1 more (exact to +-1).
    n1 = num(re.search(r"Forms with count 1: ([\d,]+)", s).group(1))
    distinct_old = all_distinct_old
    for t in targets:
        m = re.search(rf"^\| {int(t * 100)} % \| ([\d,]+) \|$", s, re.M)
        old_rank = num(m.group(1))
        if old_rank <= distinct_old - n1:
            sys.exit(f"target {t} lies outside forms.tsv but not among the count-1 forms")
        cov[t] = old_rank - len(gone) + round((1 - t) * removed["total"])
    for t, rank in cov.items():
        s = re.sub(rf"^\| {int(t * 100)} % \| [\d,]+ \|$", f"| {int(t * 100)} % | {rank:,} |", s, flags=re.M)
    # top 50
    i = s.index("## Top 50 forms")
    head = s[i:].split("\n")[:4]
    body = [f"| {k} | {r[0]} | {int(r[1]):,} | {int(r[2]):,} | {int(r[3]):,} | {int(r[4]):,} | {int(r[5]):,} |"
            + "".join(f" {int(r[col[g]]):,} |" for g in regions) for k, r in enumerate(keep[:50], 1)]
    s = s[:i] + "\n".join(head + body) + "\n"
    s += ("\n## Removed artefacts\n\n"
          "On 2026-10-21 these forms were removed by `tools/frequency/drop_forms.py` (HTML entity names that the "
          "Wikipedia cleaning counted as words; the counts above are reduced accordingly, the texts were not "
          "recounted):\n\n| form | total | wiki | lit | gov |\n|---|---:|---:|---:|---:|\n"
          + "".join(f"| {r[0]} | {int(r[1]):,} | {int(r[2]):,} | {int(r[3]):,} | {int(r[4]):,} |\n" for r in gone))
    open(sp, "w", encoding="utf-8").write(s)
    print(f"dropped {len(gone)} forms, {removed['total']:,} tokens; total now {all_tokens:,}")

if __name__ == "__main__":
    main()

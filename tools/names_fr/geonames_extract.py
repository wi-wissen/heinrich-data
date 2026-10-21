#!/usr/bin/env python3
"""Extract GeoNames candidates with a French name (CC BY 4.0, https://www.geonames.org/).

Reads allCountries.zip and alternateNamesV2.zip (download: tools/names_fr/fetch.sh) and writes a
small TSV of candidate features:
    geonameid  feature_class.feature_code  country  population  n_names  fr_name  ascii_name
`n_names` is the number of distinct alternate names in other languages (a proxy for how widely
known a feature is); `fr_name` is the French name (preferred name first, then short name, then
the first plain one). Historic and colloquial names are skipped.
Usage: geonames_extract.py RAW_DIR OUT_TSV
"""
import io
import sys
import zipfile
from collections import defaultdict

KEEP = {
    "L.CONT", "L.RGN", "L.RGNH", "L.AREA", "A.ADM1", "A.PCLI", "A.PCLD", "A.PCLIX", "A.PCLS",
    "H.STM", "H.LK", "H.LKS", "H.SEA", "H.OCN", "H.GULF", "H.BAY", "H.STRT", "H.CHN", "H.SD",
    "T.MT", "T.MTS", "T.PK", "T.ISL", "T.ISLS", "T.PEN", "T.DSRT", "T.PLAT", "T.VLC", "T.VAL",
    "T.PLN", "T.CAPE", "T.ATOL", "T.UPLD", "T.HLLS",
}
CITY = {"P.PPLC", "P.PPLA", "P.PPL", "P.PPLA2", "P.PPLA3", "P.PPLG"}
MIN_CITY_POP = 50_000


def lines(zpath, member):
    with zipfile.ZipFile(zpath) as z:
        with z.open(member) as f:
            yield from io.TextIOWrapper(f, encoding="utf-8")


def main(raw, out):
    feats = {}
    for line in lines(f"{raw}/allCountries.zip", "allCountries.txt"):
        p = line.rstrip("\n").split("\t")
        fc = f"{p[6]}.{p[7]}"
        pop = int(p[14] or 0)
        if fc in KEEP or (fc in CITY and (pop >= MIN_CITY_POP or fc == "P.PPLC")):
            feats[p[0]] = (fc, p[8], pop, p[1], p[2])
    langs = defaultdict(set)
    fr = defaultdict(list)
    for line in lines(f"{raw}/alternateNamesV2.zip", "alternateNamesV2.txt"):
        p = line.rstrip("\n").split("\t")
        gid = p[1]
        if gid not in feats:
            continue
        lang = p[2]
        hist = p[6] == "1" or p[7] == "1" or (len(p) > 9 and p[9])
        if lang and len(lang) <= 3 and lang not in ("link", "post", "iata", "icao", "faac", "abbr", "wkdt", "unlc"):
            langs[gid].add(lang)
        if lang == "fr" and not hist:
            rank = 0 if p[4] == "1" else 1 if p[5] == "1" else 2
            fr[gid].append((rank, p[3]))
    with open(out, "w", encoding="utf-8") as o:
        for gid, (fc, cc, pop, name, ascii_) in feats.items():
            if gid not in fr:
                continue
            frname = sorted(fr[gid])[0][1]
            o.write(f"{gid}\t{fc}\t{cc}\t{pop}\t{len(langs[gid])}\t{frname}\t{name}\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

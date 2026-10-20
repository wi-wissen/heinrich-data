#!/usr/bin/env python3
"""Build fr/names/{given_names,surnames,places}.tsv from official open data.

Sources (download with tools/names_fr/fetch.sh into RAW_DIR; licences in SOURCES.md):
  INSEE Fichier des prenoms, edition 2025          (Licence Ouverte 2.0)  given names
  INSEE Fichier des noms, 2018 (births 1891-2000)  (Licence Ouverte 2.0)  surnames
  INSEE COG 2026 + populations de reference 2023   (Licence Ouverte 2.0)  French places, countries
  GeoNames extract (geonames_extract.py)           (CC BY 4.0)            foreign cities, regions
plus our own curation files in fr/names/curated/ (see fr/names/README.md).

Usage: build.py RAW_DIR GEO_TSV OUT_DIR [--stats FILE]
"""
import csv
import sys
import unicodedata
from collections import defaultdict

# ---- thresholds (documented in fr/names/README.md) ----
GIVEN_MIN_BIRTHS = 200        # births 1900-2025 with this first given name
GENDER_SHARE = 0.90           # m (f) if at least this share of the births are boys (girls), else u
SURNAME_MIN_BIRTHS = 700      # births 1891-2000 with this surname
COMMUNE_MIN_POP = 3_000       # municipal population (populations de reference 2023)
FOREIGN_CITY_MIN_POP = 150_000
FOREIGN_ADM1_MIN_POP = 1_000_000

# Particles and articles: never listed as name parts.
PARTICLES = {
    "le", "la", "les", "l", "de", "du", "des", "d", "et", "en", "sur", "sous", "lès", "lez",
    "lés", "aux", "au", "à", "da", "das", "do", "dos", "di", "del", "della", "dei", "van",
    "von", "der", "den", "ter", "ten", "y", "e", "el", "al", "saint", "sainte", "saints",
    "st", "ste", "san", "santa", "santo", "são", "sao",
}
# Generic French place words: kept inside a whole hyphenated name, never listed alone.
GENERIC = {
    "mer", "mont", "monts", "bois", "pont", "ponts", "port", "val", "vallée", "plage", "bains",
    "fort", "château", "roche", "roches", "ville", "villes", "vieux", "vieille", "neuf",
    "neuve", "grand", "grande", "petit", "petite", "haut", "haute", "hauts", "bas", "basse",
    "nord", "sud", "est", "ouest", "lac", "lacs", "île", "îles", "ile", "iles", "pays",
    "plaine", "rivière", "forêt", "champ", "champs", "puits", "moulin", "moulins", "fontaine",
    "fontaines", "bourg", "cap", "côte", "coteau", "plateau", "étang", "étangs", "marais",
    "pré", "prés", "saules", "vignes", "loges", "eaux", "sables", "chênes", "croix", "rive",
    "rives", "gare", "abbaye", "prieuré", "église", "maison", "maisons", "village", "camp",
    "province", "préfecture", "région", "état", "états", "oblast", "district", "territoire",
    "gouvernorat", "wilaya", "voïvodie", "comté", "canton", "land", "république", "kraï",
    "municipalité", "département", "capitale", "ville-état", "autonome", "communauté",
    "fédéral", "fédérale", "métropolitaine", "spéciale", "occidental", "occidentale",
    "oriental", "orientale", "central", "centrale", "septentrional", "méridional",
    "méridionale", "septentrionale", "nouveau", "nouvelle", "royaume", "unis", "unies",
    "arabes", "démocratique", "populaire", "islamique", "fédérative", "socialiste",
    "partie", "néerlandaise", "britanniques", "britannique", "américaines", "dépendance",
    "dépendances", "couronne", "terre", "terres", "australes", "antarctiques", "françaises",
    "française", "mineures", "éloignées", "zone", "metropolitan", "city", "county", "new",
    "massif", "golfe", "détroit", "océan", "baie", "chaîne", "cordillère", "désert", "delta",
    "canal", "mers", "océans", "plaines", "collines", "fédération", "ravine", "pic", "col",
    "pointe", "anse", "archipel", "atoll", "péninsule", "presqu", "lagune",
}


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)).lower()


def sort_key(name):
    return (fold(name), name)


def title(upper):
    """INSEE upper case -> usual case: JEAN-PIERRE -> Jean-Pierre, LE GALL -> Le Gall."""
    out, start = [], True
    for c in upper:
        out.append(c.upper() if start else c.lower())
        start = c in " -'"
    return "".join(out)


def ok_name(n):
    return len(n) >= 3 and "'" not in n and "’" not in n and not any(ch.isdigit() for ch in n)


WORDS = set()  # names that are also ordinary words (fr/names/curated/word.tsv)


def parts(name):
    """Whole name (if one token, possibly hyphenated) and its name parts.

    A part that is an ordinary word is left out (`Royal` of Cormelles-le-Royal); a whole name
    that is one is kept and marked."""
    name = name.replace("’", "'")
    if "," in name or "(" in name:
        out = []
        for piece in name.replace("(", ",").replace(")", ",").split(","):
            out += parts(piece.strip())
        return out
    out = []
    tokens = name.split()

    def whole(tok):
        # a hyphenated token is a name only if it does not end or start with a particle
        # (`Valgelon-La` of Valgelon-La Rochette is a fragment)
        segs = tok.split("-")
        return ok_name(tok) and segs[0].lower() not in PARTICLES and segs[-1].lower() not in PARTICLES

    if len(tokens) == 1 and whole(name):
        out.append(name)
    for tok in tokens:
        if "-" in tok and len(tokens) > 1 and whole(tok):
            out.append(tok)
        for p in tok.split("-"):
            if "'" in p:
                head, _, p = p.partition("'")
                if head.lower() not in ("d", "l"):
                    continue
            if p.lower() in PARTICLES or p.lower() in GENERIC or not ok_name(p):
                continue
            if p[0].islower() or (p in WORDS and p != name):
                continue
            out.append(p)
    return out


def read_curated(path, ncols):
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    p = line.rstrip("\n").split("\t")
                    rows.append(p + [""] * (ncols - len(p)))
    except FileNotFoundError:
        pass
    return rows


def main(raw, geo, out, stats_path=None):
    cur = f"{out}/curated"
    words = {r[0] for r in read_curated(f"{cur}/word.tsv", 1)}
    WORDS.update(words)
    excluded = defaultdict(set)  # name -> lists it is left out of (given, surname, place)
    for r in read_curated(f"{cur}/excluded.tsv", 3):
        excluded[r[0]].add(r[1])
    accents = defaultdict(list)
    for r in read_curated(f"{cur}/surname_accents.tsv", 2):
        accents[r[0]].append(r[1])
    stats = []

    # ---- given names ----
    births = defaultdict(lambda: [0, 0])
    with open(f"{raw}/prenoms/prenoms-2025-nat.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["prenom"].startswith("_"):
                continue
            births[r["prenom"]][int(r["sexe"]) - 1] += int(r["valeur"] or 0)
    all_births = sum(m + f for m, f in births.values())
    given, covered = {}, 0
    for up, (m, f) in births.items():
        if m + f < GIVEN_MIN_BIRTHS:
            continue
        n = title(up)
        if " " in n or not ok_name(n) or "given" in excluded[n]:
            continue
        g = "m" if m >= GENDER_SHARE * (m + f) else "f" if f >= GENDER_SHARE * (m + f) else "u"
        covered += m + f
        if n in given and given[n] != g:
            g = "u"
        given[n] = g
    stats.append(f"given names: {len(given)} (>= {GIVEN_MIN_BIRTHS} births 1900-2025), "
                 f"{covered / all_births:.1%} of all births with a listed first given name; "
                 f"m {sum(1 for g in given.values() if g == 'm')}, "
                 f"f {sum(1 for g in given.values() if g == 'f')}, "
                 f"u {sum(1 for g in given.values() if g == 'u')}")

    # ---- surnames ----
    surnames, covered, total = set(), 0, 0
    with open(f"{raw}/noms/noms2008nat_txt.txt", encoding="latin-1") as f:
        next(f)
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            c = sum(map(int, p[1:]))
            total += c
            if p[0] == "AUTRES NOMS" or c < SURNAME_MIN_BIRTHS:
                continue
            got = False
            for n in parts(title(p[0])):
                for v in [n] + accents.get(n, []):
                    if "surname" not in excluded[v]:
                        surnames.add(v)
                        got = True
            covered += c if got else 0
    stats.append(f"surnames: {len(surnames)} (>= {SURNAME_MIN_BIRTHS} births 1891-2000, "
                 f"with accented spellings), {covered / total:.1%} of all persons born 1891-2000")

    # ---- places ----
    places = {}

    def add_place(name, gender, kind):
        for n in parts(name):
            if "place" in excluded[n]:
                continue
            is_whole = n == name
            g = gender if is_whole else "u"
            if n not in places:
                places[n] = (g, kind, is_whole)
                continue
            og, ok, ow = places[n]
            if is_whole and not ow:  # the name itself beats a part of a longer name
                places[n] = (g, kind, True)
            elif is_whole == ow:
                # a known gender beats `u`; two different known genders give `u`
                ng = g if og == "u" else og if g in ("u", og) else "u"
                places[n] = (ng, ok, ow)

    tncc_gender = {"2": "m", "3": "f"}
    for row in read_curated(f"{cur}/places.tsv", 3):
        add_place(row[0], row[1] or "u", row[2])
    for r in csv.DictReader(open(f"{raw}/cog/v_region_2026.csv", encoding="utf-8")):
        add_place(r["NCCENR"], tncc_gender.get(r["TNCC"], "u"), "state")
    for r in csv.DictReader(open(f"{raw}/cog/v_departement_2026.csv", encoding="utf-8")):
        add_place(r["NCCENR"], tncc_gender.get(r["TNCC"], "u"), "state")
    for r in csv.DictReader(open(f"{raw}/cog/v_comer_2026.csv", encoding="utf-8")):
        add_place(r["NCCENR"], tncc_gender.get(r["TNCC"], "u"), "state")
    for r in csv.DictReader(open(f"{raw}/cog/v_pays_territoire_2026.csv", encoding="utf-8")):
        if r["COG"] == "99100" and r["ACTUAL"] != "1":
            continue
        kind = {"1": "country", "4": "region"}.get(r["ACTUAL"], "historic")
        add_place(r["LIBCOG"], "u", kind)
    pop = {}
    with open(f"{raw}/pop/donnees_communes.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            pop[r["COM"]] = int(r["PMUN"])
    with open(f"{raw}/pop/donnees_collectivites.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            pop[r["COM"]] = int(r["PMUN"])
    n_com = 0
    pop_all = sum(pop.values())
    pop_cov = 0
    for r in csv.DictReader(open(f"{raw}/cog/v_commune_2026.csv", encoding="utf-8")):
        if r["TYPECOM"] != "COM" or pop.get(r["COM"], 0) < COMMUNE_MIN_POP:
            continue
        n_com += 1
        pop_cov += pop[r["COM"]]
        add_place(r["NCCENR"], tncc_gender.get(r["TNCC"], "u"), "city")
    for r in csv.DictReader(open(f"{raw}/cog/v_commune_comer_2026.csv", encoding="utf-8")):
        if pop.get(r["COM_COMER"], 0) >= COMMUNE_MIN_POP:
            n_com += 1
            add_place(r["NCCENR"], tncc_gender.get(r["TNCC"], "u"), "city")
    stats.append(f"communes: {n_com} with >= {COMMUNE_MIN_POP} inhabitants, "
                 f"{pop_cov / pop_all:.1%} of the population of France")
    n_city = n_adm = 0
    with open(geo, encoding="utf-8") as f:
        for line in f:
            gid, fc, cc, p, _n, frname, _name = line.rstrip("\n").split("\t")
            p = int(p)
            if cc == "FR":
                continue
            if fc.startswith("P.") and (p >= FOREIGN_CITY_MIN_POP or fc == "P.PPLC"):
                n_city += 1
                add_place(frname, "u", "city")
            elif fc == "A.ADM1" and p >= FOREIGN_ADM1_MIN_POP:
                n_adm += 1
                add_place(frname, "u", "state")
    stats.append(f"GeoNames: {n_city} foreign cities (>= {FOREIGN_CITY_MIN_POP} inhabitants "
                 f"or capital), {n_adm} first-level regions (>= {FOREIGN_ADM1_MIN_POP})")
    stats.append(f"places: {len(places)} names")

    # ---- write ----
    def write(fname, rows):
        with open(f"{out}/{fname}", "w", encoding="utf-8", newline="\n") as o:
            for cols in sorted(rows, key=lambda r: sort_key(r[0])):
                o.write("\t".join(c for c in cols if c) + "\n")

    def w(n):
        return "word" if n in words else ""

    write("given_names.tsv", [(n, g, w(n)) for n, g in given.items()])
    write("surnames.tsv", [(n, "u", w(n)) for n in surnames])
    write("places.tsv", [(n, g, k, w(n)) for n, (g, k, _) in places.items()])
    text = "\n".join(stats)
    print(text)
    if stats_path:
        open(stats_path, "w", encoding="utf-8").write(text + "\n")


if __name__ == "__main__":
    a = sys.argv[1:]
    st = None
    if "--stats" in a:
        i = a.index("--stats")
        st = a[i + 1]
        del a[i:i + 2]
    main(*a, stats_path=st)

#!/bin/sh
# Download the raw open data for fr/names into RAW_DIR (not committed; see SOURCES.md).
# Usage: tools/names_fr/fetch.sh RAW_DIR
set -eu
RAW=${1:?usage: fetch.sh RAW_DIR}
INSEE=https://www.insee.fr/fr/statistiques/fichier
GEO=https://download.geonames.org/export/dump
mkdir -p "$RAW/prenoms" "$RAW/noms" "$RAW/cog" "$RAW/pop" "$RAW/geonames"

# INSEE Fichier des prénoms, édition 2025 (births 1900-2025), Licence Ouverte 2.0
curl -fsS -o "$RAW/prenoms/prenoms-2025-nat_csv.zip" "$INSEE/8595130/prenoms-2025-nat_csv.zip"
unzip -o -q -d "$RAW/prenoms" "$RAW/prenoms/prenoms-2025-nat_csv.zip"

# INSEE Fichier des noms (État civil, births 1891-2000, published 2018-05-22), Licence Ouverte 2.0
curl -fsS -o "$RAW/noms/noms2008nat_txt.zip" "$INSEE/3536630/noms2008nat_txt.zip"
unzip -o -q -d "$RAW/noms" "$RAW/noms/noms2008nat_txt.zip"

# INSEE Code officiel géographique au 1er janvier 2026, Licence Ouverte 2.0
for f in v_commune_2026 v_departement_2026 v_region_2026 v_comer_2026 v_commune_comer_2026 \
         v_pays_territoire_2026; do
  curl -fsS -o "$RAW/cog/$f.csv" "$INSEE/8740222/$f.csv"
done

# INSEE populations de référence 2023 (in force 2026-01-01), Licence Ouverte 2.0
curl -fsS -o "$RAW/pop/ensemble.zip" "$INSEE/8680726/ensemble.zip"
unzip -o -q -d "$RAW/pop" "$RAW/pop/ensemble.zip"

# GeoNames gazetteer dump, CC BY 4.0 (about 630 MB)
for f in allCountries.zip alternateNamesV2.zip readme.txt; do
  curl -fsS -o "$RAW/geonames/$f" "$GEO/$f"
done

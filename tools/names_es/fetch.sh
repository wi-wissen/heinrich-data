#!/bin/sh
# Download the raw open data for es/names into RAW_DIR (not committed; see SOURCES.md).
# Usage: tools/names_es/fetch.sh RAW_DIR
set -eu
RAW=${1:?usage: fetch.sh RAW_DIR}
INE=https://www.ine.es
GEO=https://download.geonames.org/export/dump
UA="Mozilla/5.0 (heinrich-data names_es)"
mkdir -p "$RAW/ine" "$RAW/mun" "$RAW/geonames"

# INE, nombres y apellidos por frecuencia (Censos de poblacion anuales, 1 January 2025), CC BY 4.0
curl -fsSL -A "$UA" -o "$RAW/ine/nombres_por_edad_media.xlsx" "$INE/daco/daco42/nombyapel/nombres_por_edad_media.xlsx"
curl -fsSL -A "$UA" -o "$RAW/ine/apellidos_frecuencia.xls" "$INE/daco/daco42/nombyapel/apellidos_frecuencia.xls"

# INE, cifras oficiales de poblacion de los municipios (Padron, 1 January 2025), CC BY 4.0
curl -fsSL -A "$UA" -o "$RAW/mun/pobmun.zip" "$INE/pob_xls/pobmun.zip"
unzip -o -q -j -d "$RAW/mun" "$RAW/mun/pobmun.zip" pobmun/pobmun25.xlsx

# GeoNames gazetteer dump, CC BY 4.0 (about 630 MB)
for f in allCountries.zip alternateNamesV2.zip readme.txt; do
  curl -fsS -o "$RAW/geonames/$f" "$GEO/$f"
done

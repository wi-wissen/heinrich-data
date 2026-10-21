# Spanish name lists (`es/names/`)

Three switchable data files with person and place names for the Spanish names pack
`es-names.pack` (Heinrich `docs/PACK_FORMAT.md` §6, `docs/SPANISH.md` S-D4). As for French, the
lists are **filtered from official open data** and then curated. Same format as `de/names/`,
`en/names/` and `fr/names/`, so the same parser and pack builder read them. Spanish of Spain
(`es-ES`) only.

| file | content | columns |
|---|---|---|
| `given_names.tsv` | 8,208 given names: every given name borne by at least 100 residents of Spain (INE, 1 January 2025), alone or as part of a compound given name (`José Luis` → `José`, `Luis`), in its usual spelling with accents (`José`, `María`, `Ángel`), plus the Catalan or Galician spelling where it is common (`Maria`, `Núria`, `Àngel`) | `name<TAB>gender[<TAB>word]` |
| `surnames.tsv` | 16,195 surnames: every surname that is the first surname of at least 200 residents (INE, 1 January 2025), split into name parts, in its usual spelling (`González`, `Núñez`, `García`, Catalan `Garcia`, `Domènech`) | `name<TAB>u[<TAB>word]` |
| `places.tsv` | 7,833 place names in their Spanish form: all municipalities with at least 500 inhabitants (INE, Padrón 2025) in every official form (`Alicante`/`Alacant`, `Donostia`/`San Sebastián`, `Vitoria-Gasteiz`), the provinces, the Spanish names of all countries and continents, foreign cities with at least 150,000 inhabitants and all capitals, foreign first-level regions with at least 1,000,000 inhabitants (GeoNames), and our own list of autonomous communities, traditional Castilian forms (`La Coruña`, `Gerona`, `Lérida`, `Orense`, `Vizcaya`), continents, rivers, mountains, seas, islands, regions, historic states and foreign exonyms (`curated/places.tsv`) | `name<TAB>gender<TAB>kind[<TAB>word]` |

Format rules (all files): UTF-8, LF line endings, tab separated, one name per line, sorted by
name (accents folded, case-insensitive, then by code point), no header, no comment lines, each
name once per file. `gender` is `m`, `f` or `u`; surnames always carry `u`. In `places.tsv`
the gender is the grammatical gender of the name where the source gives it (the article of the
official municipality name: `m` El Ejido, `f` A Coruña, Las Palmas; our own list: `m` el Ebro,
los Pirineos, `f` la Mancha), otherwise `u`; the pack does not store place genders. `kind` is one
of `continent`, `country`, `historic`, `state`, `city`, `river`, `mountain`, `region`, `island`,
`water` and is documentation only. The optional last column `word` marks a name that is also an
ordinary Spanish word (`Rosa`, `Pilar`, `Dolores`, `Moreno`, `Blanco`, `Castillo`, `Prieto`,
`Cruz`, `Rey`, `León`, `Granada`, `Ejido`): the name alone is no evidence of a person or place
(as in `en/names/` and `fr/names/`).

## Spanish surnames

A person in Spain has two surnames, the first from the father, the second from the mother
(`Ana García López`: father García, mother López); since 2017 parents may choose the order.
Both are written without a hyphen; a surname of several words keeps its particles (`de la
Fuente`, `del Río`, `San Martín`), and some people join their two surnames with `y` (`Ortega y
Gasset`) or a hyphen. The INE file counts each surname as first and as second surname; the list
uses the first-surname count. Because a full name is a sequence of single words for the
tokenizer, `surnames.tsv` lists the name parts that are not particles (`de la Fuente` →
`Fuente`, `del Río` → `Río`, `San Martín` → `Martín`); the particles `de`, `del`, `la`, `los`,
`y`, `san`, `santa` … are never listed. A married woman keeps her own surnames, so the list
needs no married forms.

## How the lists are made

`tools/names_es/fetch.sh RAW` downloads the raw data (not committed), `tools/names_es/geonames_extract.py
RAW/geonames GEO.tsv` extracts the GeoNames features with a Spanish name, and
`tools/names_es/build.py RAW GEO.tsv es/names` writes the three lists (needs `openpyxl` and
`xlrd`). The thresholds are constants at the top of `build.py`.

**Spelling.** INE writes person names in capitals **without accents** (`JOSE`, `GONZALEZ`;
`Ñ` and `Ç` are kept). The usual spelling of every name of the two lists comes from
`curated/spellings.tsv`; a name without an entry is written in title case (`ANTONIO` →
`Antonio`). The accented spelling replaces the register spelling: `Jose`, `Gonzalez` and
`Nunez` are not listed (in es-ES text they are spelling errors), except where the unaccented or
differently accented form is the regular spelling of Catalan, Galician, Basque or Portuguese
and common in Spain (`María` and `Maria`, `García` and `Garcia`, `Adriá` and `Adrià`).
Surnames in `-ez` were checked against the stress rule (llana, accent on the second-last
syllable: `Rodríguez`, `Sáez`, `Gutiérrez`); the exceptions are kept as written (`Álvarez`,
`Estébanez`, `Díez`, `Jerez`, Latin-American `Valdez`, `Cortez`).

**Given names.** Residents per given name and sex. A compound given name (`MARIA CARMEN`,
`JOSE LUIS`; INE drops the particles of `María del Carmen`) counts for each of its parts, so
`Carmen` and `Luis` are listed even where they occur mostly as the second part. Gender: `m` if
at least 90 % of the bearers are men, `f` if at least 90 % are women, otherwise `u`. The share is
taken from the name alone or as the **first** part of a compound name, because in Spain the first
part decides the gender (`José María` is a man, `María José` a woman): `María` stays `f`,
`José` and `Jesús` stay `m`. A name that only occurs as a later part takes its gender from those
compounds. `u` are names borne by men and women alike (`Reyes`, `Cruz`, `Claude`,
`Dominique`, `Francis`, Basque `Izar`, many Chinese and Sikh names); `Andrea`, `Noa` and
`Trinidad` are `f` in Spain (the salutation rules never use `u`).

**Surnames.** Residents per first surname; a multi-word surname counts for each part.

**Places.** Official INE names: the article that INE puts after the name is dropped (`Coruña, A`
→ `Coruña`, gender `f`; `Palmas, Las` → `Palmas`), each language form of a bilingual name is a
name of its own (`Alicante/Alacant`, `Castelló de la Plana/Castellón de la Plana`). A hyphenated
name is listed whole and by its parts (`Vitoria-Gasteiz`, `Vitoria`, `Gasteiz`). Particles and
articles of Castilian, Catalan, Galician and Balearic (`de`, `del`, `la`, `el`, `els`, `les`,
`a`, `o`, `os`, `es`, `sa`, `ses`, `y`, `i`, `san`, `sant` …, list in `build.py`) and ordinary
Spanish words (`curated/word.tsv`: `Frontera` of Jerez de la Frontera, `Puerto`, `Real`) are not
listed as parts; a Catalan elision is cut (`l'Hospitalet de Llobregat` → `Hospitalet`,
`Llobregat`). Generic words of the other languages of Spain and of foreign names stay as parts
(`Vall`, `Kuala`, `Hong`), so that `La Vall d'Uixó`, `Kuala Lumpur` and `Hong Kong` are known.
GeoNames gives the Spanish name of foreign places (`Londres`, `Múnich`, `Colonia`, `Nueva
York`, `Pekín`, `Baviera`, `Alemania`); Spanish places of GeoNames are not used.

**Left out.** Names of one or two letters, names with an apostrophe, a middle dot, a period or
a digit (`D'Angelo`, `Marcel·lí`), the particles,
and the names in `curated/excluded.tsv`.

## Curation (`curated/`, our own data)

| file | content |
|---|---|
| `spellings.tsv` | 2,556 usual spellings of INE register names (`REGISTER<TAB>given\|surname<TAB>spelling[<TAB>spelling]`): 408 given names, 2,148 surnames; 96 lines with a second (Catalan, Galician or Portuguese) spelling |
| `word.tsv` | 2,987 names that are also ordinary Spanish words (`name`), also covering parts of the place names (`Golfo`, `Estrecho`, `Imperio`, `Unidas`) |
| `excluded.tsv` | 48 names left out of a list (`name<TAB>given\|surname\|place<TAB>reason`): fragments of split foreign names (`Eddine`, `Ullah`, `Ould`), function words (`En`, `No`, `Entre`), register noise (`Fernadez`, `Mariajose`, `Nunez`) |
| `places.tsv` | 3,313 autonomous communities, traditional Castilian and co-official forms, continents, countries, rivers, mountains, seas, lakes, islands, regions, historic states and foreign exonyms in their Spanish form, with grammatical gender (`name<TAB>gender<TAB>kind`) |

The curation was written on 2026-10-21 from our own knowledge of Spanish, of the other
languages of Spain and of geography (no dictionary, lexicon, word list, name list, gazetteer or
web source was consulted): every name of the three candidate lists (given names ≥ 100, surnames
≥ 200, place-name parts of municipalities ≥ 500 and of the GeoNames selection) was read once and
given its usual spelling, marked as `word` or excluded. A Spanish lexicon and frequency list of
our own do not exist yet; once they do, the `word` marker should be checked against them as for
English (`en/names/AUTHORING.md` §2). The `word` marker is set generously (verb forms such as
`Sean`, `Dame`, rare nouns such as `Medina`, `Herrera`): a wrongly set marker only removes a
name cue, a missing one can make a word look like a name.

## Coverage

State 2026-10-21 (`build.py --stats`):

| list | entries | coverage |
|---|---|---|
| given names | 8,208 (m 3,565, f 4,135, u 508; 523 marked `word`) | every given name is listed for 98.7 % of the residents in the INE file (names borne by ≥ 20 persons) |
| surnames | 16,195 (2,175 marked `word`) | the first surname is listed for 91.9 % of the residents in the INE file (first surnames borne by ≥ 20 persons); ≥ 300 bearers would be 11,900 names for 89.7 %, ≥ 100 would be 26,400 for 95.0 % |
| places | 7,833 (464 marked `word`) | 4,150 municipalities with ≥ 500 inhabitants (98.5 % of the population of Spain), the 50 provinces and 2 autonomous cities, 247 countries and continents, 1,792 foreign cities and 1,071 foreign regions (GeoNames), 3,313 lines of our own list |

Pack size (`heinrich pack build-names --lang es`, 29,178 distinct names): 168,976 bytes,
78,364 bytes gzip -9, within the names-pack budget of 100 KB gzip. Lowering the surname threshold
is the way to grow the lists (about 2.5 bytes gzip per name).

## Licence and attribution

The lists are derived from INE statistics and GeoNames, both under CC BY 4.0, which allows
commercial use, modification and use in closed-source software with attribution; the curation
files are our own data. Required attribution (also stored in the pack and in Heinrich
`NOTICE`):

- Elaboración propia con datos extraídos del sitio web del INE: www.ine.es — Apellidos y nombres
  más frecuentes (Censos de población anuales a 1 de enero de 2025, ficheros actualizados el
  2026-04-23) y Cifras oficiales de población de los municipios españoles (Revisión del Padrón
  municipal a 1 de enero de 2025, actualizado el 2025-12-11); CC BY 4.0,
  https://creativecommons.org/licenses/by/4.0/. Filtered and modified (selection by frequency and
  population, accents restored, name parts, regional spellings added).
- GeoNames (https://www.geonames.org/), dump of 2026-10-21, CC BY 4.0,
  https://creativecommons.org/licenses/by/4.0/. Selection of Spanish place names, modified.

INE does not take part in, sponsor or support this reuse.

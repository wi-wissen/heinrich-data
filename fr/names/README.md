# French name lists (`fr/names/`)

Three switchable data files with person and place names for the French names pack
`fr-names.pack` (Heinrich `docs/PACK_FORMAT.md` §6, `docs/FRENCH.md` F-D4). Unlike the German and
English lists, which are our own work, these lists are **filtered from official open data**
and then curated by hand. Same format as `de/names/` and `en/names/`, so the same parser and
pack builder read them.

| file | content | columns |
|---|---|---|
| `given_names.tsv` | 9,178 given names: every first given name given to at least 200 children born in France 1900–2025 (INSEE *Fichier des prénoms*), with spelling variants (`Léo`/`Leo`, `Hélène`/`Helene`) and hyphenated names (`Jean-Pierre`, `Marie-Claire`) | `name<TAB>gender[<TAB>word]` |
| `surnames.tsv` | 15,577 surnames: every surname borne by at least 700 persons born in France 1891–2000 (INSEE *Fichier des noms*), split into name parts, plus the usual accented spelling of names the register writes without accents | `name<TAB>u[<TAB>word]` |
| `places.tsv` | 9,536 place names in their French form: French regions, departments and overseas collectivities, all communes with at least 3,000 inhabitants (INSEE COG 2026 and populations de référence 2023), all countries and territories (COG), foreign cities with at least 150,000 inhabitants and all capitals, foreign first-level regions with at least 1,000,000 inhabitants (GeoNames, French names), and our own list of continents, rivers, mountains, seas, islands, historic states and traditional regions (`curated/places.tsv`) | `name<TAB>gender<TAB>kind[<TAB>word]` |

Format rules (all files): UTF-8, LF line endings, tab separated, one name per line, sorted by
name (accents folded, case-insensitive, then by code point), no header, no comment lines, each
name once per file. `gender` is `m`, `f` or `u`; surnames always carry `u`. In `places.tsv`
the gender is the grammatical gender of the name where the source gives it (the article of
the official commune name: `m` Le Havre, `f` La Rochelle; our own list: `m` le Rhin, `f` la
Seine), otherwise `u`; the pack does not store place genders. `kind` is one of `continent`,
`country`, `historic`, `state`, `city`, `river`, `mountain`, `region`, `island`, `water` and
is documentation only. The optional last column `word` marks a name that is also an ordinary
French word (`Pierre`, `Rose`, `Petit`, `Blanc`, `Nice`, `Tours`, `Orange`): the name alone is
no evidence of a person or place (as in `en/names/`).

## How the lists are made

`tools/names_fr/fetch.sh RAW` downloads the raw data (not committed), `tools/names_fr/geonames_extract.py
RAW/geonames GEO.tsv` extracts the GeoNames features with a French name, and
`tools/names_fr/build.py RAW GEO.tsv fr/names` writes the three lists. The thresholds are
constants at the top of `build.py`.

**Given names.** Births per first given name and sex, summed over 1900–2025. Gender: `m` if at
least 90 % of the births are boys, `f` if at least 90 % are girls, otherwise `u` (`Claude`
88 % boys, `Dominique`, `Camille`, `Alix`, `Sacha`... the salutation rules never use `u`).
INSEE writes names in capitals with accents (`RAPHAËL`); they are converted to the usual case
per hyphen part (`JEAN-PIERRE` → `Jean-Pierre`).

**Surnames.** Persons per surname, summed over the decades of birth 1891–2000. The register
writes surnames in plain ASCII capitals (`LEFEVRE`, `GUERIN`): the list keeps the register
spelling in the usual case (`Lefevre`, `Guerin`) and adds the usual accented spelling from
`curated/surname_accents.tsv` (`Lefèvre`, `Guérin`). Multi-word surnames are listed by their
parts that are not particles (`Le Gall` → `Gall`, `Da Silva` → `Silva`); hyphenated ones whole
(`Jean-Baptiste`).

**Places.** Official names without the article (`Havre`, `Rochelle`, `Sables-d'Olonne` → see
below). A hyphenated name is listed whole and by its name parts (`Aix-en-Provence`, `Aix`,
`Provence`; `Boulogne-Billancourt`, `Boulogne`, `Billancourt`); articles, particles (`le`,
`de`, `sur`, `lès`, `Saint` …), generic place words (`mer`, `mont`, `pont`, `ville`, `nord`,
`province`, `région` …, list in `build.py`) and ordinary words (`curated/word.tsv`) are not
listed as parts. GeoNames gives the French name of foreign places (`Londres`, `Munich`,
`Cologne`, `Anvers`, `Pékin`, `Bavière`, `Californie`); countries come from the COG
(`Allemagne`, `Royaume-Uni`, `Tchéquie`).

**Left out.** Names of one or two letters, names with an apostrophe or a digit (`N'Golo`,
`Prud'homme`, `Sables-d'Olonne` as a whole: the tokenizer splits at the apostrophe; the part
after `d'`/`l'` is listed: `Olonne`), names with a space in the given-name data, the INSEE
groups `_PRENOMS_RARES` and `AUTRES NOMS`, and the names in `curated/excluded.tsv`.

## Curation (`curated/`, our own data)

| file | content |
|---|---|
| `word.tsv` | 1,880 names that are also ordinary French words (`name`) |
| `surname_accents.tsv` | 788 accented spellings of register surnames (`ascii<TAB>accented`) |
| `excluded.tsv` | 280 names left out of a list (`name<TAB>given\|surname\|place<TAB>reason`): register spellings that are an ordinary word without its accent (`Leger` for *léger*; the accented `Léger` is kept), function words and very frequent words whose use as a name is negligible, generic geographic words and fragments of the sources |
| `places.tsv` | 2,683 continents, rivers, mountains, seas, lakes, islands, historic states and traditional regions in their French form, with grammatical gender (`name<TAB>gender<TAB>kind`) |

The curation was written on 2026-10-20 from our own knowledge of French (no dictionary,
lexicon, word list or web source was consulted): every name of the three lists was read once
and marked as `word`, given an accented spelling or excluded. `curated/places.tsv` was written
from general knowledge of geography as taught in French schools, like `de/names/places.tsv`.
A French lexicon and frequency list of our own do not exist yet; once they do, the `word`
marker should be checked against them as for English (`en/names/AUTHORING.md` §2).

## Coverage

State 2026-10-20 (`build.py --stats`):

| list | entries | coverage |
|---|---|---|
| given names | 9,178 (m 3,910, f 4,757, u 511; 225 marked `word`) | the listed names are the first given name of 98.4 % of all children born in France 1900–2025 |
| surnames | 15,577 (788 of them added accented spellings; 1,276 marked `word`) | 56.0 % of all persons born in France 1891–2000 bear a listed surname (the register has 218,982 surnames with ≥ 30 bearers; the long tail is very flat: ≥ 300 bearers would be 37,000 names for 70 %) |
| places | 9,536 (259 marked `word`) | 3,761 communes with ≥ 3,000 inhabitants (66.6 % of the population of France), all 18 regions, 101 departments, the overseas collectivities, all countries and territories of the COG, 2,056 foreign cities and 1,071 foreign regions (GeoNames), 2,683 lines of our own list of natural and historic names |

Pack size (`heinrich pack build-names --lang fr`, 32,529 distinct names): 193,632 bytes,
87,561 bytes gzip -9, within the names-pack budget of 100 KB gzip. Lowering the thresholds is
the way to grow the lists: surnames are the largest part (about 2.9 bytes gzip per name).

## Licence and attribution

The lists are derived from data under the Licence Ouverte / Open Licence 2.0 (Etalab) and
CC BY 4.0, both of which allow commercial use with attribution; the curation files are our own
data. Required attribution (also stored in the pack and in Heinrich `NOTICE`):

- Source : Insee, Fichier des prénoms (édition 2025, parue le 2026-07-16), Fichier des noms
  (2018-05-22), Code officiel géographique au 1er janvier 2026 (mise à jour 2026-02-24), Populations de référence 2023
  (2025-12-18); Licence Ouverte / Open Licence 2.0, https://www.etalab.gouv.fr/licence-ouverte-open-licence.
  Filtered and modified (selection by frequency and population, change of case, name parts,
  accented spellings added).
- GeoNames (https://www.geonames.org/), dump of 2026-10-20, CC BY 4.0,
  https://creativecommons.org/licenses/by/4.0/. Selection of French place names, modified.

INSEE does not endorse this reuse.

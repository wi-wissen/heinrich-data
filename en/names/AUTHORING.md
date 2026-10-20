# Authoring protocol: English name lists (`en/names/`)

Work package E2 of Heinrich `docs/PARITY.md` (names pack and name cues for English). Format and
rules of the files: [`README.md`](README.md).

## 1. Clean-room rules

- The author writes every name from own knowledge. No third-party name list, census or
  birth-name statistic (no SSA or ONS baby-name lists, no census surname tables), gazetteer
  (no GeoNames), telephone directory, Wikipedia or Wiktionary list, dictionary, Hunspell/SCOWL
  file or other lexicon was read, on disk or on the web.
- The only data consulted are our own: the English lexicon `en/lexicon/` (through
  `heinrich-lexicon --lang en split`) and our own frequency list `en/frequency/forms.tsv`.
- A separate reviewer may compare the lists with third-party data later and reports only
  "disputed" / "missing" and statistics, never the third-party value (Heinrich `CLAUDE.md`).

## 2. Procedure (2026-10-20)

1. **Raw lists from memory**, grouped by origin and period so that nothing large is forgotten:
   given names (male, female, unisex; traditional and modern US/UK, Welsh, Scottish, Irish,
   South Asian, Arabic and Muslim, East Asian, African, Slavic, Romance, biblical, Anglo-Saxon
   and medieval), surnames (English by letter, Scottish, Irish, Welsh, Hispanic, South Asian,
   Chinese, Korean, Vietnamese, Japanese, African, Italian, German, Scandinavian, Slavic,
   Jewish, Iranian, Arabic) and persons of the school canon (English and American literature,
   science, philosophy, US presidents, British prime ministers and monarchs' houses, figures of
   history, composers, painters, architects), places by kind (continents, countries, historic
   states, US states, Canadian provinces, Australian states, German/Austrian/Swiss states and
   other regions, UK counties and regions, London districts, Scottish, Welsh and Irish
   counties, cities by country, rivers, mountains, islands, waters).
2. **Assembly.** Given names in both the male and the female list, or in the unisex list,
   get `u`. Multi-word places are split into parts; parts that are particles or ordinary words
   (lowercase form known to the lexicon), and demonym or adjective parts, are dropped
   (`README.md`). Hyphenated places are kept whole and by their name parts. Names of one or two
   letters, with an apostrophe or a period, are dropped. Sorting: accents folded, then code
   point.
3. **`word` marker.** Every name and name part, lowercased, was run through
   `heinrich-lexicon --lang en split en/lexicon`; status `exact` or `compound` sets `word`.
   Then the names whose lowercase form occurs at least 15 times in `en/frequency/forms.tsv`
   without `word` were checked by hand: the lowercase form is an ordinary word the lexicon
   lacks so far (`smith`, `nick`, `billy`, `warren`, `savannah`, `burgundy`, `griffin`, `stoke`,
   `browning`, `outback`, `seine`, `natal`, `cayenne`, `spree`, `mantel`, `dirk`, `paddy`,
   `verity`, `jasmine`, `hank`, `bobby`, `sonny`; also `English`, `French`, ordinary words
   although capitalised) → `word`; otherwise rare or foreign (`del`, `les`, `sur`, `dar`,
   `martin` the bird, `morris` the dance, `kirk`) → no marker.
4. **Error-hiding check.** Every name without `word` whose lowercase form is one edit
   (insertion, deletion, substitution, transposition) from a lowercase word counted at least
   8,000 times was listed (about 500 names) and read by hand. Names that a typical pupil error
   produces for that word were removed (`Childs`, `Sumer`, `Champaign`, `Brough`, `Notting`,
   `Leaming`, `Spedding`, `Weekes`, `Seren`, `Treves`); the rest are ordinary coincidences of
   real names (`Alan`/`plan`, `Amy`/`any`, `York`/`work`) and stay.
5. **Gender.** Names used for both sexes in English-speaking countries get `u` even when one
   use dominates (`Evelyn`, `Lindsay`, `Vivian`, `Hilary`, `Courtney`, `Laurie`, `Leigh`,
   `Kerry`, `Ashley`): the genders serve the salutation rule (`Dear Mr Sarah Jones`), where a
   wrong `m`/`f` would be a false alarm and `u` never counts.
6. **Removed as not belonging:** characters of works (`Gatsby`, `Jekyll`), obscure or invented
   given-name spellings that came up while listing (`Ahren`, `Sinjin`, `Yvaine`, `Rozalind` …),
   and words that are not given names in normal use (`Queen`, `Ransom`, `Canon`).
7. **Size.** The lists are sized for the engine's `en-names.pack` budget (≤ 25 KB gzip). The
   pack uses the compact list layout (`docs/PACK_FORMAT.md` §6); with the FST layout of the
   German pack the same lists would need about 38 KB gzip.

## 3. Result (2026-10-20)

| file | names | with `word` |
|---|---|---|
| `given_names.tsv` | 2,808 (1,298 f, 1,381 m, 129 u) | 214 |
| `surnames.tsv` | 2,731 | 290 |
| `places.tsv` | 2,444 (218 countries, 129 states/provinces, 323 regions, 1,418 cities, 102 rivers, 65 mountains, 70 islands, 45 waters, 64 historic, 10 continents) | 115 |

## 4. Open points for the reviewer

- Completeness of modern given names (US and UK names of the last 20 years) and of names of
  migrant families in the UK (Polish, Romanian, Somali, Nigerian, Bangladeshi names).
- The `word` marker for borderline cases (rare lowercase words such as `croft`, `pollard`,
  `crick`, `gage`, `firth`, `wight`).
- Places that should be added (more UK towns; US county seats are out of scope).

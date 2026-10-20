# English name lists (`en/names/`)

Three switchable data files with person and place names that occur in English school, office
and everyday texts. Like the German lists (`../../de/names/README.md`) they are **not** part of
the lexicon shards; the engine packs them as the optional `en-names.pack` (Heinrich
`docs/PACK_FORMAT.md` §6). Authoring protocol: [`AUTHORING.md`](AUTHORING.md).

| file | content | columns |
|---|---|---|
| `given_names.tsv` | about 3,050 given names: traditional and modern names of the US, the UK, Ireland, Canada, Australia and New Zealand (`Olivia`, `Jayden`, `Siobhan`, `Callum`, `Lachlan`), Welsh, Scottish and Irish names (`Rhys`, `Eilidh`, `Saoirse`), names common in families of South Asian, African, Arabic, Hispanic, East Asian, Polish and other origin in English-speaking countries (`Priya`, `Chidi`, `Zainab`, `Mateo`, `Mei`), biblical and historical names (`Ezekiel`, `Boudica`, `Athelstan`) | `name<TAB>gender[<TAB>word]` |
| `surnames.tsv` | about 3,000 surnames: common surnames of England, Scotland, Wales, Ireland and the US (including frequent Hispanic, South Asian, East Asian, African, Jewish, Italian, German, Scandinavian and Slavic surnames) and the names of persons of the school canon (writers, scientists, philosophers, composers, painters, US presidents, British prime ministers and monarchs' houses, figures of history) | `name<TAB>u[<TAB>word]` |
| `places.tsv` | about 2,600 place names in their English form: continents, all countries (and historical states and regions of history lessons), US states, Canadian provinces, Australian states, the German, Austrian and Swiss states, the counties and regions of England, Scotland, Wales and the island of Ireland, London boroughs and districts, about 1,550 towns and cities (the UK and Ireland, the US, Canada, Australia, New Zealand, India, Pakistan and the world's capitals and large cities), English exonyms (`Munich`, `Cologne`, `Vienna`, `Nuremberg`, `Brunswick`, `Hanover`, `Bavaria`, `Prague`, `Warsaw`, `Lisbon`, `The Hague` → `Hague`), rivers, mountains and ranges, islands, seas and lakes | `name<TAB>u<TAB>kind[<TAB>word]` |

Format rules (all files): UTF-8, LF line endings, tab separated, one name per line, sorted by
name (case-insensitive with accents folded, then by code point), no header, no comment lines, each name once per file.
`gender` is `m`, `f` or `u` (unisex or unknown); surnames and places always carry `u` (English
place names have no grammatical gender), so the files can be read by the same parser as the
German ones. `kind` is one of `continent`, `country`, `historic`, `state`, `city`, `river`,
`mountain`, `region`, `island`, `water`; it is documentation only (the parser ignores it), and
a place listed under several kinds (`Georgia`, `Victoria`) carries the first one.

**The `word` marker.** A name that is also an ordinary English word carries `word` as its last
column: given names such as `Bill`, `Rose`, `Mark`, `Will`, `Hope`, `Grace`, `Dawn`, `Jack`,
surnames such as `Smith`, `Baker`, `Cook`, `Brown`, `Bush`, and places such as `Reading`,
`Bath`, `Nice`, `Turkey`, `China`, `Mobile`, `Split`, `Worms`. The engine accepts these words
anyway (they are in the lexicon); the marker says that the name on its own is no evidence of a
person or place (`Bill` may be a bill), so name cues need a second sign (a title, a following
surname). The marker was set when the lowercase form is a word of our English lexicon
(`heinrich-lexicon --lang en split en/lexicon`, status `exact` or `compound`) or, for words the
lexicon does not have yet, by hand after a check of the lowercase counts in our frequency list
`en/frequency/forms.tsv` (`Hank`, `Bobby`, `Dirk`, `Paddy`, `Jasmine`, `Verity`, `Spree`,
`Mantel`, `Sexton`, `Bunting`, `Goldsmith`, `Underwood`, `Flagstaff` …). Readers that predate the
marker ignore the extra column.

**Multi-word names** are listed by their parts that are not ordinary words and not particles
(`Angeles`, `Aires`, `Janeiro`, `Lumpur`, `Keynes`; not `New`, `North`, `Saint`, `St`, `Fort`,
`Lake`, `City`, `Salt`); `Los`, `Las`, `San`, `Santa`, `Rio`, `Sri` are kept, because they start
a sentence in English texts (`San Diego is …`). Hyphenated names are listed whole and by their
name parts (`Stratford-upon-Avon`, `Stratford`; `Baden-Württemberg`, `Baden`, `Württemberg`).
Parts that are demonyms or adjectives are left out (`English` of English Channel, `Persian`,
`Soviet`, `Indian`, `British`, `Latin`, `Bavarian`).

**Left out on purpose** (as in the German lists): names of one or two letters (`Al`, `Ed`, `Jo`,
`Li`, `Wu`, `Le`), names with an apostrophe or a period (`O'Brien`, `Martha's Vineyard`,
`St. John's`, `Xi'an`: the tokenizer splits them, a later extension may add them), acronyms and names in capitals
(`USSR` is in the lexicon), characters of works and legends (`Gatsby`, `Jekyll`), and names one
typical pupil error away from a frequent word, so that the misspelling would be accepted at the
start of a sentence: `Childs` (*childs*), `Sumer` (*sumer* for summer), `Champaign`
(*champaign* for champagne), `Brough` (*brough* for brought), `Notting` (*notting* for nothing),
`Leaming`, `Spedding`, `Weekes`, `Seren`, `Treves`. Accented and unaccented spellings are both
listed where both are usual in English texts (`Zürich`/`Zurich`, `Düsseldorf`/`Dusseldorf`,
`Bogotá`/`Bogota`, `Zoë`/`Zoe`).

The engine derives the inflected forms; they are not stored: the possessive `'s` (`Emma's`,
`London's`), the plural possessive (`the Joneses'`) and plurals of surnames (`the Smiths`).

All lists were written from the author's own knowledge of names in English-speaking schools,
families and offices, of the school canon and of geography. No name list, census or birth-name
statistic, telephone directory, gazetteer, Wikipedia/Wiktionary list, dictionary or any other
third-party data was read, on disk or on the web (see `../../SOURCES.md`). Candidates were checked
only against our own English lexicon and our own frequency list. They are own data, released
under the licence of this repository.

# German name lists (`de/names/`)

Three switchable data files with person and place names that occur in school and office texts.
They are **not** part of the lexicon shards (policy: no person names in `de/lexicon/`); the engine
loads them as optional name lists (one `names` pack), default on.

| file | content | columns |
|---|---|---|
| `given_names.tsv` | about 2,750 given names used in German-speaking schools: traditional and modern German names, names common in Turkish, Kurdish, Arabic, Persian, Albanian, Balkan, Slavic, Romance, Vietnamese and other migrant families; biblical, saints' and historical given names taught in religion and history (`Jesaja`, `Petrus`, `Theoderich`, `Nofretete`) | `name<TAB>gender` |
| `surnames.tsv` | about 4,450 surnames: about 2,500 common surnames in Germany, Austria and Switzerland, including frequent names of migrant families (Turkish, Polish, Russian, South-Slavic, Albanian, Arabic, Vietnamese, Italian, Greek, ...), and about 1,950 names of persons of the school and general-education canon (see below) | `name<TAB>u` |
| `places.tsv` | about 3,250 place names in their German form: continents, all countries (and historical states and regions often named in history lessons), German federal states, Austrian states, Swiss cantons, US states, Canadian provinces and other often named sub-national regions, about 900 cities and towns of Germany and ~250 of Austria, Switzerland, Luxembourg, Liechtenstein and South Tyrol, ~750 world cities (the capitals and large cities; with German exonyms: `Mailand`, `Breslau`, `Lüttich`), rivers, mountains and ranges, landscapes and regions, islands, seas and lakes | `name<TAB>gender<TAB>kind` |

Format rules (all files): UTF-8, LF line endings, tab separated, one name per line, sorted by
name (accents folded), no header, no comment lines, each name once. `gender` is `m`, `f` or `u`
(unisex or unknown); surnames always carry `u`, so all files can be read by the same parser.
In `places.tsv` the gender is the grammatical gender of the name (`m` der Rhein, `f` die
Schweiz, `n` das Saarland, `u` plural or unclear: die Alpen, die USA); the pack stores `n` as
unspecified. `kind` is one of `continent`, `country`, `historic`, `state`, `city`, `river`,
`mountain`, `region`, `island`, `water` and is documentation only (the parser ignores it).
Multi-word names are listed by their parts that are not ordinary words (`Janeiro`, `Aires`,
`Gallen`; not `Bad`, `San`, `New`). Parts that would hide a capitalisation or old-spelling error
when accepted as names are left out (`Weil` der Stadt, `Kamen`, `Leer`, `Riß`, `Nahe` for a misspelt `Nähe`).
A name that is also a common noun or adjective (`Müller`, `Koch`, `Klein`, `Weiß`) is listed
as well: the engine only uses the lists to accept capitalized words.

**Canon persons** (`surnames.tsv`). Writers (German-language literature from the Middle Ages
to the present, children's and youth literature, world literature from antiquity on), philosophers,
psychologists and educationalists, figures of religion, composers and musicians, painters,
sculptors and architects, scientists, engineers and economists, and persons of history and
politics (antiquity to present, Germany, Austria, Switzerland and the world). Each person is
listed by the part that is not an ordinary word, usually the surname (`Goethe`, `Dürrenmatt`,
`Gogh`, `Vinci`, `Exupéry`), or the single name they are known by (`Homer`, `Michelangelo`,
`Voltaire`, `Konfuzius`); German forms of classical names are used (`Platon`, `Horaz`,
`Tizian`). Given names of such persons that are not on the given-name list go to
`given_names.tsv`.

**Left out on purpose.** A canon name that is also an ordinary word (`Brecht`, `Händel`, `Fichte`,
`Klee`, `Engels`, `Bohr`, `Ohm`, `Diesel`, `Zeppelin`, `Stifter`, `Frisch`, `Zweig`, `Hauptmann`,
`Locke`, `Wilde`; places `Leer`, `Lehrte`, `Giengen`, `Pfarrkirchen`, `Regen`) is not listed: the
format cannot mark a name as "also a common word", and the lexicon already knows the form. Also
left out: names one typical pupil error away from a frequent word (`Gluck`/`Glück`, `Loos`/`Los`,
`Glass`/`Glas`, `Begin`/`Beginn`, `Kamp`/`Kampf`, `Grass`/`Gras`, `Brod`/`Brot`, `Schweitzer`/`Schweizer`), names of one or two letters (`Li`, `Oz`, `Ur`),
English words (`Field`, `Cash`, `Truth`), adjectival parts of names (`Starnberger`, `Thüringer`,
`Schwarzes`: demonyms and adjectives are not part of the format), acronyms (`DDR`), names with an
apostrophe (`D'Annunzio`), name particles (`Ibn`, `Saint`), deities, characters of works and
legends (`Eulenspiegel`, `Tell`; they belong in the user or class dictionary), institutions
(`Harvard`), and canon names without a single occurrence (also as genitive) in our frequency list
`de/frequency/forms.tsv`. Places known from bynames (`Franz von Assisi`, `Benedikt von Nursia`)
are in `places.tsv`, not in `surnames.tsv`.

**Possible later extensions** (not planned now; owner decision 2026-10-20: the lists grow only
selectively, and work titles and characters belong in the user or class dictionary):
- a marker "also a common word" (e.g. a third column in `surnames.tsv`), so that canon names
  such as `Brecht`, `Händel` or `Klee` could serve as name cues without being accepted as spellings;
- a list kind for work titles and characters (`Woyzeck`, `Mephisto`, `Gretchen`).

The engine derives the inflected forms; they are not stored: genitive `-s` (`Tims`, `Lenas`,
`Ulms`), the apostrophe genitive after s-sounds (`Max'`, `Hans'`), and the plural of surnames
(`die Müllers`). The lexicon tools (`heinrich-lexicon classify --names de/names`) also use the
lists, with place demonyms (`Kieler`, `Münchner`), to keep names off the authoring work lists.

Geographic names that rules need with their gender may *additionally* have a `propn` entry in
the lexicon (`AUTHORING.md` §4.5); the place list only makes them known words.

All lists were written from the author's own knowledge of names in German-speaking schools and
families and, for `places.tsv`, of geography as taught in German-speaking schools. No name list, telephone directory, civil-register statistic, Wikipedia/Wiktionary list or
any other third-party data was read, on disk or on the web (see `SOURCES.md`). They are own data,
released under the licence of this repository.

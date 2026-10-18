# German name lists (`de/names/`)

Two switchable data files with person names that occur in school texts. They are **not** part of
the lexicon shards (policy: no person names in `de/lexicon/`); the engine loads them as optional
name lists, default on.

| file | content | columns |
|---|---|---|
| `given_names.tsv` | about 2,600 given names used in German-speaking schools: traditional and modern German names, names common in Turkish, Kurdish, Arabic, Persian, Albanian, Balkan, Slavic, Romance, Vietnamese and other migrant families | `name<TAB>gender` |
| `surnames.tsv` | about 2,500 common surnames in Germany, Austria and Switzerland, including frequent names of migrant families (Turkish, Polish, Russian, South-Slavic, Albanian, Arabic, Vietnamese, Italian, Greek, ...) | `name<TAB>u` |

Format rules (both files): UTF-8, LF line endings, tab separated, one name per line, sorted by
name (accents folded), no header, no comment lines, each name once. `gender` is `m`, `f` or `u`
(unisex or unknown); surnames always carry `u`, so both files can be read by the same parser.
A name that is also a common noun or adjective (`Müller`, `Koch`, `Klein`, `Weiß`) is listed
as well: the engine only uses the lists to accept capitalized words.

The engine derives the inflected forms; they are not stored: genitive `-s` (`Tims`, `Lenas`),
the apostrophe genitive after s-sounds (`Max'`, `Hans'`), and the plural of surnames (`die
Müllers`).

Both lists were written from the author's own knowledge of names in German-speaking schools and
families. No name list, telephone directory, civil-register statistic, Wikipedia/Wiktionary list or
any other third-party data was read, on disk or on the web (see `SOURCES.md`). They are own data,
released under the licence of this repository.

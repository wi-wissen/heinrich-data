# Frequency list tools

Builds `de/frequency/forms.tsv`, `en/frequency/forms.tsv` and `fr/frequency/forms.tsv` (case-sensitive word-form counts) by counting
tokens ourselves.
Only counts are stored, never the texts (text and data mining, Sec. 44b UrhG). No existing word list,
frequency list, lexicon or dictionary is used as input (clean-room). Sources: see `/SOURCES.md`.

## Requirements
Python 3.9+, `curl`, internet access, roughly 1 GB of free disk for the temporary count files
(downloads are streamed and processed in memory; the count files are small TSVs).

## Re-running
Pick a work directory `W` outside the repository.

```sh
mkdir -p W && cd W
python3 -I tools/frequency/count_wiki.py wiki 60          # Wikipedia sample: 60 chunks per dump part (~56M tokens, ~10 min)
curl -sSf -o pg_catalog.csv https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv
for k in 0 1 2; do python3 -I tools/frequency/count_gutenberg.py gut pg_catalog.csv 12000000 $k 3 & done; wait   # ~1 h, 2 s delay per book
python3 -I tools/frequency/count_gov.py gov x             # Bundestag protocols + federal laws (~10 min)
python3 -I tools/frequency/merge.py . de/frequency        # writes forms.tsv(.gz) and STATS.md
```

English (separate work directory `W_en`):

```sh
python3 -I tools/frequency/count_wiki.py wiki 24 en      # enwiki sample: 24 chunks in each of 6 dump parts (~50M tokens)
curl -sSf -o pg_catalog.csv https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv
for k in 0 1 2; do python3 -I tools/frequency/count_gutenberg.py gut pg_catalog.csv 15000000 $k 3 en & done; wait
python3 -I tools/frequency/count_gov_en.py gov ppp fr &              # US: Public Papers of the Presidents, Federal Register
python3 -I tools/frequency/count_gov_en.py gov hansard leg govuk &   # UK: Hansard, Acts, GOV.UK
wait
python3 -I tools/frequency/merge.py . en/frequency en
```

French (separate work directory `W_fr`; details in `fr/frequency/README.md`):

```sh
python3 -I tools/frequency/count_wiki.py wiki 42 fr      # frwiki sample: 42 chunks in each of 6 dump parts (~54M tokens)
curl -sSf -o pg_catalog.csv https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv
for k in 0 1 2; do python3 -I tools/frequency/count_gutenberg.py gut pg_catalog.csv 13500000 $k 3 fr & done; wait
python3 -I tools/frequency/count_gov_fr.py gov an senat sp &     # Assemblée nationale, Sénat, service-public.gouv.fr
python3 -I tools/frequency/count_gov_fr.py legi_all legi &       # Légifrance LEGI export (~1 GB, streamed), 20 buckets
wait
cp legi_all/legi_0[0-9].tsv gov/                                 # keep LEGI buckets 00-09 (see fr/frequency/README.md)
python3 -I tools/frequency/merge.py . fr/frequency fr
```

All count scripts are resumable (existing output files are skipped). Dumps and websites change, so numbers
will differ slightly between runs; the Wikipedia sample uses the `latest` dump (ours: 2026-10-01).

## Files
- `tok.py` - tokenizer, sentence splitter, counters (shared).
- `count_wiki.py` - systematic sample of dewiki multistream dump parts via HTTP range requests; wikitext cleaning.
- `count_gutenberg.py` - German books from gutenberg.org (catalog language `de`), canon authors first.
- `count_gov.py` - Bundestag plenary protocols (WP 18-21) and gesetze-im-internet.de.
- `count_gov_en.py` - US federal texts (govinfo.gov: Public Papers of the Presidents, Federal Register) and
  UK texts (Hansard via TheyWorkForYou, legislation.gov.uk, GOV.UK content API).
- `count_gov_fr.py` - French official texts from the DILA open data (Assemblée nationale and Sénat debates,
  Légifrance LEGI, service-public.gouv.fr guides), all Licence Ouverte 2.0.
- `authors_en.py` - hand-written list of American / British authors (bibliographic metadata only) used to
  select and label English Gutenberg books.
- `drop_forms.py` - removes counting artefacts from a `forms.tsv` and updates `STATS.md` to match (used on
  2026-10-21 for HTML entity names, see "Known limitations").
- `merge.py` - merges counts, writes `forms.tsv`, `STATS.md` (`lang=en` adds the `us`/`gb` columns; `lang=fr` has
  no variety columns: fr-FR only for now).

All scripts take the language as an argument (default `de`); `tok.set_lang()` selects the abbreviation list
and quotation marks of the sentence splitter.

## Tokenization
- Token = run of Latin letters (umlauts, ss-sharp, accents kept), optionally joined by single hyphens or
  apostrophes between letters (hyphenated compounds stay one token). NFC-normalized, case kept.
- Anything touching a digit or underscore, and URLs, is dropped. Markup (templates, refs, tables, links) stripped.
- `sentence_initial` = number of times the form is the first token of a sentence. Sentences are split at
  `.!?` followed by an uppercase letter or quote, and at line breaks; common abbreviations, single letters and
  ordinal numbers (`3. Mai`) do not end a sentence. A sentence starting with a number does not count.
  Headings, list markers and table rows in Wikipedia are not counted as sentences (headings are dropped).
- Columns `wiki`, `lit`, `gov` are per-source counts so old spellings (e.g. `daß` in literature) can be weighted per source.

## English specifics
- Same token definition; apostrophes between letters stay inside the token (`don't`, `John's`, `o'clock`),
  a trailing apostrophe is dropped (`students'` -> `students`). `’` is normalised to `'`.
- English abbreviation list (`Mr.`, `Dr.`, `St.`, `Jan.`, `Inc.`, `vs.` ...); numbers followed by a full stop
  do end a sentence (no ordinals as in German).
- Columns `us` and `gb` (after `sentence_initial`, so tools reading column 6 still work) count the form in
  text whose variety is known. They are subsets of `wiki`/`lit`/`gov`, not additions:
  - `wiki`: articles carrying the Wikipedia maintenance template `{{Use American English}}` (us) or
    `{{Use British English}}`, `{{Use Oxford spelling}}`, `{{EngvarB}}` (gb); other articles count in `wiki` only.
  - `lit`: every book is labelled by its author's variety (`authors_en.py`); us and gb books are balanced.
  - `gov`: US federal texts are `us`, UK texts are `gb`.
  Count scripts write the regional subsets as `<name>.us.tsv` / `<name>.gb.tsv` next to `<name>.tsv`.
- Gutenberg: only books by listed authors where every named author/editor/translator died in 1955 or earlier
  (public domain in the US and life + 70 years); at most 12 books per author.

## French specifics
- Same token definition and case handling (case-sensitive surface forms, `sentence_initial` column).
- Elision is split: a leading clitic `l' d' j' m' n' s' t' c' qu' lorsqu' puisqu' jusqu' quoiqu'` (any case)
  becomes its own token with the apostrophe (`l'homme` -> `l'` `homme`, `L'État` -> `L'` `État`,
  `jusqu'aujourd'hui` -> `jusqu'` `aujourd'hui`). Other inner apostrophes stay (`aujourd'hui`, `presqu'île`,
  `quelqu'un`, `prud'homme`); `c'est-à-dire` is kept whole. `l' homme` (space after the apostrophe, old prints)
  is read as `l'homme`.
- Apostrophe variants `’ ʼ ‘ ‛ ´ \` ′` between letters become `'`, hyphen variants U+2010/U+2011 become `-`.
  Hyphenated forms stay one token as in German and English (`peut-être`, `a-t-il`, `est-ce`, `dix-huit`).
- French abbreviation list (`MM.`, `Mme`, `Mlle`, `Mgr`, `art.`, `chap.`, `cf.`, `p.`, `janv.` ...); single letters
  (`M.`, `J.-C.`) do not end a sentence; guillemets with (narrow) no-break spaces are handled by the sentence
  splitter (`? » Il`, `. « Oui`).
- Gutenberg: every named person (illustrators ignored) died in 1954 or earlier, the first author was born in
  1600 or later (no Middle French), at most 12 books per author, canonical authors first.

## Known limitations
- Until 2026-10-21 `count_wiki.py` unescaped HTML entities only once, so `&nbsp;` (`&amp;nbsp;` in the dump XML)
  and similar entities were counted as the words `nbsp`, `shy`, `thinsp` ... . The script now unescapes twice. The
  existing lists were not recounted: the forms that are only entity names were removed with `drop_forms.py` and
  the token totals reduced (removed forms and counts are listed at the end of each `STATS.md`). Entity names that
  are also words (`lt`, `gt`, `amp`, `minus`, English `shy`, `times`) keep a few artefact counts.
- English `gb` text from the 19th century often uses `-ize` (Oxford spelling) and old forms (`to-day`,
  `connexion`); `gb` from Hansard/GOV.UK is modern `-ise` spelling. Compare `us`/`gb` per million, not raw.
- The English sentence-splitter abbreviation list also contains some lowercase short words (e.g. `art`, `ed`,
  `do`); a sentence ending in such a word is not split (affects only `sentence_initial`, rarely).
- Foreign-language names/words in German texts are counted as they are (no language filter); the tail is noisy.
- Wikipedia sample is systematic by dump position, not random by article; lists/stubs are included.
- Gutenberg books use old spelling and sometimes letter-spaced emphasis; the Bundestag zips contain
  line-break hyphenation that is repaired heuristically.

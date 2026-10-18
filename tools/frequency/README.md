# Frequency list tools

Builds `de/frequency/forms.tsv` (case-sensitive German word-form counts) by counting tokens ourselves.
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

All count scripts are resumable (existing output files are skipped). Dumps and websites change, so numbers
will differ slightly between runs; the Wikipedia sample uses the `latest` dump (ours: 2026-10-01).

## Files
- `tok.py` - tokenizer, sentence splitter, counters (shared).
- `count_wiki.py` - systematic sample of dewiki multistream dump parts via HTTP range requests; wikitext cleaning.
- `count_gutenberg.py` - German books from gutenberg.org (catalog language `de`), canon authors first.
- `count_gov.py` - Bundestag plenary protocols (WP 18-21) and gesetze-im-internet.de.
- `merge.py` - merges counts, writes `forms.tsv`, `STATS.md`.

## Tokenization
- Token = run of Latin letters (umlauts, ss-sharp, accents kept), optionally joined by single hyphens or
  apostrophes between letters (hyphenated compounds stay one token). NFC-normalized, case kept.
- Anything touching a digit or underscore, and URLs, is dropped. Markup (templates, refs, tables, links) stripped.
- `sentence_initial` = number of times the form is the first token of a sentence. Sentences are split at
  `.!?` followed by an uppercase letter or quote, and at line breaks; common abbreviations, single letters and
  ordinal numbers (`3. Mai`) do not end a sentence. A sentence starting with a number does not count.
  Headings, list markers and table rows in Wikipedia are not counted as sentences (headings are dropped).
- Columns `wiki`, `lit`, `gov` are per-source counts so old spellings (e.g. `daß` in literature) can be weighted per source.

## Known limitations
- Foreign-language names/words in German texts are counted as they are (no language filter); the tail is noisy.
- Wikipedia sample is systematic by dump position, not random by article; lists/stubs are included.
- Gutenberg books use old spelling and sometimes letter-spaced emphasis; the Bundestag zips contain
  line-break hyphenation that is repaired heuristically.

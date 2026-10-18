# Sources

## German word frequency list (`de/frequency/`)

All counts were produced by our own scripts in `tools/frequency/` (clean-room: no third-party word list,
frequency list, lexicon or dictionary was used). Texts were streamed and discarded; only token counts are kept
(text and data mining, Sec. 44b UrhG; the sources below do not reserve their content against mining or are
works not protected by copyright). Counted on 2026-10-17/18.

| Source | Key | URL | Version / date | Legal basis | Amount counted |
|---|---|---|---|---|---|
| German Wikipedia, article namespace | `wiki` | https://dumps.wikimedia.org/dewiki/latest/ (multistream parts 2, 3, 5, 6; systematic sample of 60 chunks of ~1000 pages per part) | dump of 2026-10-01 | TDM Sec. 44b UrhG; only counts retained (no text is redistributed, so the CC BY-SA license of the text does not carry over to the counts) | 56,209,755 tokens from 135,258 articles |
| Project Gutenberg (gutenberg.org, not projekt-gutenberg.org) | `lit` | https://www.gutenberg.org/ (catalog: https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv, language `de`; texts `cache/epub/<id>/pg<id>.txt`) | accessed 2026-10-17/18 | public-domain texts (US status; some authors died less than 70 years ago, e.g. Hesse, Freud - counted under Sec. 44b only); PG header/footer stripped | 36,073,490 tokens from 771 books (list in `de/frequency/lit_books.tsv`) |
| Bundestag plenary protocols | `gov` | https://www.bundestag.de/services/opendata (WP 18 `pp18.zip`, WP 19 `pp19.zip`, newest 20 protocols each of WP 20 and WP 21 as XML) | accessed 2026-10-17/18 | official works, Sec. 5 UrhG (not protected by copyright) | 39,571,050 tokens (together with laws below: 56,650,242) |
| Federal laws and ordinances | `gov` | https://www.gesetze-im-internet.de/ (`gii-toc.xml`, one `xml.zip` per law; 6,141 laws) | build of 2026-09-26 | official works, Sec. 5 UrhG | 17,079,212 tokens |

Total: 148,933,487 tokens, 3,042,866 distinct forms (see `de/frequency/STATS.md`).

Notes
- Literature contains pre-1996 and older spellings (`dass` vs. old `daß`); the per-source columns allow weighting.
- Gutenberg access was sequential/limited to 3 workers with a 2 s delay per request.
- No Leipzig corpora, wordfreq, SUBTLEX, DeReWo, Hunspell, german-pos-dict, Wiktionary or similar was used.

## German lexicon (`de/lexicon/`)

Our own entries, written clean-room from general knowledge of German grammar and the official
spelling rules (no third-party lexicon, word list, Hunspell file, Wiktionary table or LanguageTool
file was consulted). Format: `Heinrich/docs/LEXICON_FORMAT.md`.

Work lists in `de/lexicon/worklists/` are derived only from our lexicon and our own frequency list
(`de/frequency/forms.tsv`) by `heinrich-lexicon next-batch`.

Lexeme classes in `de/lexicon/classes/` (time nouns, verbs of saying, directed motion verbs,
valency, perfect auxiliary by use) are our own lists, written clean-room from general knowledge of
German grammar; they contain only lemmas of our lexicon.

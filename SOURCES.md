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

## English word frequency list (`en/frequency/`)

All counts were produced by our own scripts in `tools/frequency/` (clean-room: no third-party word list,
frequency list, spelling list, lexicon or dictionary was used - no SCOWL, Hunspell, Wiktionary, WordNet,
wordfreq, COCA/BNC lists or similar). Texts were streamed and discarded; only token counts are kept
(text and data mining, Sec. 44b UrhG; public-domain works and works under open licences that allow
commercial use). Counted on 2026-10-18.

| Source | Key | Region | URL | Version / date | Licence / legal basis | Amount counted |
|---|---|---|---|---|---|---|
| English Wikipedia, article namespace | `wiki` | `us`/`gb` by the article's `{{Use American English}}` / `{{Use British English}}` (also `{{Use Oxford spelling}}`, `{{EngvarB}}`) tag, else none | https://dumps.wikimedia.org/enwiki/latest/ (multistream parts 2, 5, 8, 12a, 18a, 24a; systematic sample of ~25 chunks of ~1000 pages per part) | dump of 2026-10-01 | text CC BY-SA 4.0; TDM Sec. 44b UrhG; only counts retained (no text is redistributed, so the CC BY-SA licence of the text does not carry over to the counts) - same handling as for German | 61,018,270 tokens from 64,697 articles (us 19,632,616, gb 7,322,357) |
| Project Gutenberg (gutenberg.org) | `lit` | `us`/`gb` by author (`tools/frequency/authors_en.py`) | https://www.gutenberg.org/ (catalog `cache/epub/feeds/pg_catalog.csv`, language `en`; texts `cache/epub/<id>/pg<id>.txt`) | accessed 2026-10-18 | public domain in the US **and** every named author/editor/translator died in 1955 or earlier (life + 70 years); PG header/footer and licence text stripped (only the text between the `*** START`/`*** END` markers is counted) | 45,658,326 tokens from 672 books by 213 authors (us 22,704,097 / 355 books, gb 22,954,229 / 317 books; list in `en/frequency/lit_books.tsv`) |
| Public Papers of the Presidents of the United States, 2009-2016 | `gov` | `us` | https://www.govinfo.gov/bulkdata/PPP | govinfo bulk data, accessed 2026-10-18 | work of the US federal government, public domain (17 U.S.C. 105) | 9,026,097 tokens (16 volumes) |
| Federal Register (daily issues) | `gov` | `us` | https://www.govinfo.gov/bulkdata/FR (every 12th issue of 2023-2025; tables skipped) | accessed 2026-10-18 | public domain (17 U.S.C. 105) | 17,974,057 tokens (62 issues) |
| House of Commons Hansard (debates) | `gov` | `gb` | official report as XML via TheyWorkForYou: https://www.theyworkforyou.com/pwdata/scrapedxml/debates/ (every 8th sitting day 2015-2025, speech paragraphs only) | accessed 2026-10-18 | Parliamentary copyright, Open Parliament Licence v3.0 (allows commercial use with attribution: "Contains Parliamentary information licensed under the Open Parliament Licence v3.0.") | 13,315,300 tokens (202 sitting days) |
| UK Public General Acts | `gov` | `gb` | https://www.legislation.gov.uk/ (`ukpga/<year>/data.feed`, first feed page = up to 20 acts per even year 2000-2024, CLML `<Text>` only) | accessed 2026-10-18 | Crown copyright, Open Government Licence v3.0 (allows commercial use with attribution: "Contains public sector information licensed under the Open Government Licence v3.0.") | 8,732,893 tokens (13 years) |
| GOV.UK news stories, speeches, detailed guides | `gov` | `gb` | GOV.UK search and content API: https://www.gov.uk/api/search.json, https://www.gov.uk/api/content/... (newest 6,000 / 3,000 / 2,000 pages, English locale only, tables skipped) | accessed 2026-10-18 | Crown copyright, Open Government Licence v3.0 (attribution as above) | 9,023,749 tokens |

Total: 164,748,692 tokens, 1,189,619 distinct forms; `us` 69,336,867 tokens, `gb` 61,348,528 tokens
(see `en/frequency/STATS.md`).

Notes
- The OGL v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) permits copying,
  adapting and commercial exploitation provided the source is attributed; the Open Parliament Licence v3.0
  (https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/) is modelled on it.
  We redistribute no text, only counts; the attribution statements above go into the pack attribution if
  required.
- `authors_en.py` is bibliographic metadata written from general knowledge (author name and variety), not
  linguistic data.
- The `us`/`gb` columns are subsets of the source columns. Literature has old spellings in both varieties
  (`to-day`, `connexion`, British `-ize`); compare per-million rates, not raw counts.
- Gutenberg access was limited to 3 sequential workers with a 2 s delay per request.

## German lexicon (`de/lexicon/`)

Our own entries, written clean-room from general knowledge of German grammar and the official
spelling rules (no third-party lexicon, word list, Hunspell file, Wiktionary table or LanguageTool
file was consulted). Format: `Heinrich/docs/LEXICON_FORMAT.md`.

Work lists in `de/lexicon/worklists/` are derived only from our lexicon and our own frequency list
(`de/frequency/forms.tsv`) by `heinrich-lexicon next-batch`.

Lexeme classes in `de/lexicon/classes/` (time nouns, verbs of saying, directed motion verbs,
valency, perfect auxiliary by use) are our own lists, written clean-room from general knowledge of
German grammar; they contain only lemmas of our lexicon.

## Name lists (`de/names/`)

`given_names.tsv` (about 2,600 given names with gender m/f/u), `surnames.tsv` (about 2,500
common surnames in Germany, Austria and Switzerland) and `places.tsv` (about 2,200 place names in
their German form: countries, states and cantons, cities, rivers, mountains, regions, islands,
waters) are our own data, written clean-room from general knowledge of names in German-speaking
schools and families and of school geography. No third-party name list, gazetteer, register
statistic, directory or web source was consulted. Format and use: `de/names/README.md`.

## English lexicon (`en/lexicon/`)

Our own entries, written clean-room from general knowledge of English grammar and spelling (no
third-party English lexicon, word list, Hunspell/SCOWL file, Wiktionary or WordNet table,
dictionary or LanguageTool file was consulted). Format: `Heinrich/docs/LEXICON_FORMAT_EN.md`. The
closed classes in `en/lexicon/closed/` (articles, pronouns, determiners, prepositions,
conjunctions, auxiliaries and modals, particles, grammar-relevant adverbs, numerals) were written
by hand on 2026-10-18.

## Graded vocabulary (`de/graded/`, `en/graded/`)

Grade bands, CEFR levels and topics per lexeme are our own data, written clean-room by AI authors
(Claude) from their own knowledge of the language and of the topic areas and competence descriptions of
the curricula (educational standards of the German states, state curricula, CEFR descriptors,
integration-course fields of action). The topic catalogues (`topics.tsv`) and the topic descriptions in
the READMEs were written by the orchestrator in its own words. Authors never saw a published word list
(state basic-vocabulary lists, exam or course word lists, CEFR word profiles, learner-dictionary core
lists, frequency lists of others). `src=` records only our own provenance. Reference lists are used
only by a separate reviewer, outside the repositories, for aggregate statistics; no entry and no value
of a reference list is in this repository. Every authoring run is logged in `<lang>/graded/PROVENANCE.md`.

Labelling for end users: "This vocabulary layer was written by AI authors (Claude) based on the
competence levels of the Common European Framework of Reference and the curricula of the German federal
states, sample-checked by teachers and statistically compared internally with common reference lists.
It contains no entries from third-party word lists." (The teacher check is named only once it has been
run.)

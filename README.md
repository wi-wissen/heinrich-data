# heinrich-data

Language data for the Heinrich engine (`wi-wissen/Heinrich`): our own lexicon, created clean-room,
build scripts and finished language packs.

## Rules
- **Only our own data or data under a permissive license** (MIT, BSD, Apache-2.0, CC0, CC BY, Licence Ouverte 2.0) that
  allows commercial use. Every source goes in `SOURCES.md` with license and provenance.
- **No** CC-BY-SA, GPL, LGPL or NC data – not even in excerpts. Comparison lexica
  (german-pos-dict, Wiktionary, UniMorph, DEMorphy …) are used only outside the repo, for measurement.
- **No grammar rules** here – they live in the engine repo.
- Lexicon entries are created following the clean-room procedure (see `Heinrich/docs/PLAN.md` §6).

## Structure
- `de/lexicon/` – lemmas with inflection data (text format, diff-friendly), sharded by part of
  speech and first letter; `de/lexicon/closed/` – closed word classes (articles, pronouns,
  prepositions …), written by hand. Authoring protocol: `de/lexicon/AUTHORING.md`
- `de/frequency/` – our own word-form frequency list, and `trusted_forms.tsv`: real words of it
  that the lexicon lacks, which the spell checker accepts (generated, `de/lexicon/AUTHORING.md` §4.11),
  and `trusted_excluded.tsv`: forms the reviewer disputed, never trusted
- `en/frequency/` – our own English word-form frequency list (with en-US/en-GB counts)
- `fr/frequency/` – our own French word-form frequency list (fr-FR, elision split off;
  `fr/frequency/README.md`)
- `es/frequency/` – our own Spanish word-form frequency list (es-ES; Wikipedia, Gutenberg in modern
  orthography, BOE, Congreso; `es/frequency/README.md`)
- `la/frequency/` – our own Latin word-form frequency list from public-domain texts (Wikisource, Gutenberg),
  normalised (u/v, i/j folded, no macrons), with columns for classical prose, poetry and late/medieval Latin
  (`la/frequency/README.md`)
- `en/lexicon/` – the English lexicon (own clean-room entries, format
  `Heinrich/docs/LEXICON_FORMAT_EN.md`); so far the hand-written closed classes. Authoring
  protocol: `en/lexicon/AUTHORING.md`
- `en/names/` – English given names, surnames and place names (own lists, with a marker for names
  that are also ordinary words; `en/names/README.md`)
- `fr/lexicon/` – the French lexicon (own clean-room entries, format
  `Heinrich/docs/LEXICON_FORMAT_FR.md`), sharded by part of speech and first letter;
  `fr/lexicon/closed/` – closed word classes, written by hand. Overview and PR record:
  `fr/lexicon/README.md`; authoring protocol: `fr/lexicon/AUTHORING.md`
- `fr/names/` – French given names, surnames and place names, filtered from official open data
  (INSEE, Licence Ouverte 2.0; GeoNames, CC BY 4.0) and curated (`fr/names/README.md`)
- `es/names/` – Spanish given names, surnames and place names, filtered from official open data
  (INE, CC BY 4.0; GeoNames, CC BY 4.0) and curated: accents restored, `word` marker
  (`es/names/README.md`)
- `de/phon/` – pronunciation exceptions
- `tools/` – build scripts (lexicon → FST packs)
- `packs/` – build output (not checked in, releases)

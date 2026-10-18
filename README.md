# heinrich-data

Language data for the Heinrich engine (`wi-wissen/Heinrich`): our own lexicon, created clean-room,
build scripts and finished language packs.

## Rules
- **Only our own data or data under a permissive license** (MIT, BSD, Apache-2.0, CC0, CC BY) that
  allows commercial use. Every source goes in `SOURCES.md` with license and provenance.
- **No** CC-BY-SA, GPL, LGPL or NC data – not even in excerpts. Comparison lexica
  (german-pos-dict, Wiktionary, UniMorph, DEMorphy …) are used only outside the repo, for measurement.
- **No grammar rules** here – they live in the engine repo.
- Lexicon entries are created following the clean-room procedure (see `Heinrich/docs/PLAN.md` §6).

## Structure
- `de/lexicon/` – lemmas with inflection data (text format, diff-friendly), sharded by part of
  speech and first letter; `de/lexicon/closed/` – closed word classes (articles, pronouns,
  prepositions …), written by hand. Authoring protocol: `de/lexicon/AUTHORING.md`
- `de/frequency/` – our own word-form frequency list
- `de/phon/` – pronunciation exceptions
- `tools/` – build scripts (lexicon → FST packs)
- `packs/` – build output (not checked in, releases)

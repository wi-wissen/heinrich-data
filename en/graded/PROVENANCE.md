# Clean-room log of the graded vocabulary layer

This file is part of the clean-room evidence for the graded vocabulary layer
(`Heinrich/docs/GRADED_VOCAB.md`). Every run that writes or changes entries is logged here, with the
full prompt the author received in `log/<run>.md`. The reviewer's feedback (aggregate statistics and
patterns only) is logged verbatim outside the repositories and handed to the project owner; the
"reviewer round" column below records only that a round took place.

## Roles

| role | who | sees | never sees |
|---|---|---|---|
| orchestrator | one AI session | everything in the repositories, the reviewer's aggregate report | reference word lists, held-out test sets |
| author | one AI agent per track, area and band | `README.md`, `topics.tsv`, our own lexicon and frequency list, its prompt | any published word list, the reviewer's reference lists, held-out test sets |
| reviewer | a separate AI session, no authoring, no engine code | the export of this layer, reference lists stored outside all repositories | — (reports only aggregate numbers and patterns) |
| teacher | humans (planned) | a stratified random sample of entries | — |

Authors are told not to use web search or web fetch at all, and not to open any file outside the
repositories and their own scratch directory.

## Runs

| date | run | track / area / bands | author | input | output | validation | reviewer round |
|---|---|---|---|---|---|---|---|
| 2026-10-19 | `en-efl-3-4` | efl / all topics / 3-4 (A1) | AI author | brief, catalogue, own lexicon index, own frequency list | 796 rows | own pre-check 0 errors | – |
| 2026-10-19 | `en-efl-5-6` | efl / 5-6 (A1/A2) | AI author | same | 985 rows | 0 errors | – |
| 2026-10-19 | `en-efl-7-8` | efl / 7-8 (A2/B1) | AI author | same | 1,261 rows | 0 errors | – |
| 2026-10-19 | `en-seam` | efl / 3-4 to 7-8 | AI author | same, plus the lemmas among the 3,000 most frequent forms of our own frequency list not yet in the layer (`src=ai\|freq`) | 191 rows; 677 lemma/POS pairs judged later or not school vocabulary | 0 errors | – |
| 2026-10-19 | `lex-en` | lexicon (not the layer) | AI lexicon author (clean-room lexicon protocol) | the authors' work list | 77 lexicon entries (`note=graded`, heinrich-data#73) | `validate` 0 errors | – |
| 2026-10-19 | merge (orchestrator) | efl | mechanical | the runs above | 48 files, 2,888 rows, 2,823 lexemes; duplicates resolved to the earliest band and lowest level | `graded validate` 0 errors, 0 warnings | – |

## Reviewer rounds and revisions

| date | step | topics / runs | input to authors | result |
|---|---|---|---|---|
| 2026-10-19 | reviewer round 1 (separate session; one reference outside the repos, deleted afterwards) | whole layer | – | aggregate statistics and patterns only (verbatim log handed to the project owner) |
| 2026-10-19 | revision round 1 | `en-efl-3-4`, `en-efl-5-6`, `en-efl-7-8` | patterns and per-topic numbers (verbatim in the run logs) | 3-4: rarer animals/toys/food moved out of A1, core A1 and function words added; 5-6: A2 460 → 890 lines; 7-8: 73 lines A2 → B1, +144 lines; layer: 3,169 lexemes, `graded validate` 0 errors, 0 warnings |

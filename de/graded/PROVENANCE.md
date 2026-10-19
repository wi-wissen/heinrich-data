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
| 2026-10-19 | `de-l1-core-1-2` | l1 / core / 1-2 | AI author | brief, catalogue, own lexicon index, own frequency list | 882 rows | own pre-check 0 errors | – |
| 2026-10-19 | `de-l1-core-3-4` | l1 / core / 3-4 | AI author | same | 1,029 rows | 0 errors | – |
| 2026-10-19 | `de-l1-subjects-a-1-4` | l1 / math, science / 1-2, 3-4 | AI author | same | 658 rows | 0 errors | – |
| 2026-10-19 | `de-l1-subjects-b-1-4` | l1 / history, geography, politics, religion_ethics, arts_music, sports, computing, language / 1-2, 3-4 | AI author | same | 779 rows | 0 errors | – |
| 2026-10-19 | `de-seam` | l1 / all areas / 1-2, 3-4 | AI author | same, plus the lemmas among the 3,000 most frequent forms of our own frequency list not yet in the layer (`src=ai\|freq`) | 213 rows; 538 lemmas judged later or not school vocabulary | 0 errors | – |
| 2026-10-19 | `lex-de-a`, `lex-de-b` | lexicon (not the layer): words the authors needed | AI lexicon authors (clean-room lexicon protocol) | the authors' work list | 687 lexicon entries (`note=graded`, heinrich-data#73) | `validate` 0 errors | – |
| 2026-10-19 | merge (orchestrator) | l1 | mechanical | the runs above | 11 files, 3,519 rows, 3,230 lexemes; duplicates resolved to the earliest band; 5 ordinals corrected from `num` to `adj` (the lexicon's part of speech) | `graded validate` 0 errors, 0 warnings | – |

## Incidents

| date | what | handling |
|---|---|---|
| 2026-10-19 | The held-out test repository was present in the orchestrator's container (provisioned with the session). | Never opened by the orchestrator or any author; removal requested from the project owner. |
| 2026-10-19 | The orchestrator's lemma index for authors missed lexemes the generator derives (`adv=` adverbs in English, `demonym=` adjectives). | Index regenerated; authors re-checked their work lists (follow-up messages in the run logs). |
| 2026-10-19 | Authors of neighbouring bands each left out seam words, assuming the other band had them (`Ende`, `Welt`, `bleiben`; `thing`, `question`). | Found with our own frequency list; seam runs `de-seam`, `en-seam`. |
| 2026-10-19 | New separable verbs with an adjective particle (`kleinschreiben`, `kaputtgehen`) blocked the agreement rule for a missing adjective ending. | Entries removed before merge; rule finding reported to the engine side. |

## Reviewer rounds and revisions

| date | step | topics / runs | input to authors | result |
|---|---|---|---|---|
| 2026-10-19 | reviewer round 1 (separate session; references outside the repos, deleted afterwards) | whole layer | – | aggregate statistics and patterns only (verbatim log handed to the project owner) |
| 2026-10-19 | revision round 1 | `de-l1-core-1-2`, `de-l1-core-3-4`, `de-moved` | patterns and per-topic numbers (verbatim in the run logs) | +104 verbs in 1-2, 25 words moved 1-2 → 3-4, +311 lines in 3-4 (`src=…\|rev`); layer: 3,577 lexemes, `graded validate` 0 errors, 0 warnings |

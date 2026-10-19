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

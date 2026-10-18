# German lexicon sources (`*.lex`)

Format specification and author checklist: `Heinrich/docs/LEXICON_FORMAT.md`.
Authoring protocol (work lists, decisions, self-check): [`AUTHORING.md`](AUTHORING.md).
Parser and inflection generator: `Heinrich/crates/heinrich-de-morph`; pipeline tools:
`Heinrich/crates/heinrich-lexicon-tools` (binary `heinrich-lexicon`).
All entries are written clean-room (see `Heinrich/docs/PLAN.md` §6 and `../../SOURCES.md`).

## Layout

| directory | contents | files |
|---|---|---|
| `noun/`, `propn/`, `verb/`, `adj/`, `adv/` | open classes by part of speech | `<letter>.lex`: first letter of the lemma, lowercased, umlauts/accents folded (`Ärger` → `a.lex`), other characters → `_.lex` |
| `other/` | `intj`, `x` (abbreviations, foreign material) | `<letter>.lex` |
| `closed/` | hand-written closed classes: articles, pronouns, prepositions, conjunctions, grammar-relevant adverbs, particles, numerals, auxiliary and modal verbs | by function |
| `classes/` | lexeme classes (semantic/syntactic word classes used by the rules: `time_noun`, `verb_say`, `verb_motion_directed`, `valency`, `perf_sein_sense`); format: `Heinrich/docs/LEXICON_FORMAT.md` §14 | `<class>.tsv`: `lemma[:sense] pos [value]` per line, members must be lemmas of the lexicon |
| `worklists/` | authoring work lists produced by `heinrich-lexicon next-batch` | `batch-NNN.tsv` |

Shards are sorted by lemma; a lemma + part of speech + sense occurs once across all files.
The former M1a `sample.lex` has been split into the shards (its auxiliaries are in
`closed/auxiliaries.lex`); the engine keeps its own copy as a test fixture.

## Tools

Build once in the engine repo: `cargo build --release -p heinrich-lexicon-tools`, then
(`heinrich-lexicon` = `Heinrich/target/release/heinrich-lexicon`):

```sh
heinrich-lexicon validate de/lexicon                          # errors + lint warnings
heinrich-lexicon dump de/lexicon/noun/h.lex Haus              # all generated forms
heinrich-lexicon coverage de/lexicon de/frequency/forms.tsv \
    --top 5000 --uncovered /tmp/uncovered.tsv                 # token coverage report
heinrich-lexicon next-batch de/lexicon de/frequency/forms.tsv --size 3000 \
    --exclude de/lexicon/worklists/batch-001.tsv -o de/lexicon/worklists/batch-002.tsv
heinrich-lexicon review de/lexicon --ref unimorph:/path/outside/repo.tsv \
    --forms de/frequency/forms.tsv                            # REVIEWER only
```

`review` reads reference lexica from paths **outside** the repositories and reports only
lemmas, categories and counts. Only the reviewer runs it; authors never see its inputs.

## CI

`.github/workflows/lexicon.yml` checks out `wi-wissen/Heinrich` at the ref in
`tools/lexicon/HEINRICH_REF`, builds `heinrich-lexicon`, runs `validate` (fails on errors,
annotates warnings) and writes the coverage report to the job summary.

The engine repository is private and the default `GITHUB_TOKEN` of this repository cannot read
it. CI therefore needs a repository secret **`HEINRICH_READ_TOKEN`**: a fine-grained personal
access token (or GitHub App token) with *Contents: read* on `wi-wissen/Heinrich` only. Without
it the job fails with an explicit message.

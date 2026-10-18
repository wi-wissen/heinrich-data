# English lexicon sources (`*.lex`)

Format specification and author checklist: `Heinrich/docs/LEXICON_FORMAT_EN.md`.
Authoring protocol (work lists, decisions, self-check): [`AUTHORING.md`](AUTHORING.md).
Parser and inflection generator: `Heinrich/crates/heinrich-en-morph`; pipeline tools:
`Heinrich/crates/heinrich-lexicon-tools` (binary `heinrich-lexicon`, always with `--lang en`).
All entries are written clean-room: no third-party English lexicon, word list, dictionary or
inflection table is used (see `AUTHORING.md` §1 and `../../SOURCES.md`).

## Layout

The same as the German lexicon (`../../de/lexicon/README.md`):

| directory | contents | files |
|---|---|---|
| `noun/`, `propn/`, `verb/`, `adj/`, `adv/` | open classes by part of speech | `<letter>.lex`: first letter of the lemma, lowercased, other characters → `_.lex` |
| `other/` | `intj`, `x` (abbreviations, foreign material) | `<letter>.lex` |
| `closed/` | hand-written closed classes: articles, pronouns, determiners, prepositions, conjunctions, auxiliaries and modals, particles, grammar-relevant adverbs, numerals | by function |
| `worklists/` | authoring work lists produced by `heinrich-lexicon --lang en next-batch` | `batch-NNN.tsv` |

Status: the closed classes are seeded (`closed/`, 348 entries); the open classes are written by
author agents following `AUTHORING.md`. American and British spellings are one entry each
(`color noun gb=colour`, `LEXICON_FORMAT_EN.md` §8).

## Tools

Build once in the engine repo: `cargo build --release -p heinrich-lexicon-tools -p heinrich-cli`,
then (`heinrich-lexicon` = `Heinrich/target/release/heinrich-lexicon`):

```sh
heinrich-lexicon --lang en validate en/lexicon                   # errors + lint warnings
heinrich-lexicon --lang en dump en/lexicon/closed/personal.lex I   # all generated forms
heinrich-lexicon --lang en split en/lexicon well-known don't       # why a form is covered
heinrich-lexicon --lang en coverage en/lexicon en/frequency/forms.tsv --top 5000
heinrich-lexicon --lang en next-batch en/lexicon en/frequency/forms.tsv --size 3000 \
    -o en/lexicon/worklists/batch-001.tsv
heinrich pack build-morph en/lexicon --lang en -o packs/en-morph.pack
```

`coverage` and `next-batch` need an English frequency list of our own counts
(`en/frequency/forms.tsv`, same columns as `de/frequency/forms.tsv`); it does not exist yet.
`review` is German-only for now.

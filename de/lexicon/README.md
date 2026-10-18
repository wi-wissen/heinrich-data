# German lexicon sources (`*.lex`)

Format specification and author checklist: `Heinrich/docs/LEXICON_FORMAT.md`.
Parser and inflection generator: `Heinrich/crates/heinrich-de-morph`.

- `sample.lex` – M1a sample (~90 entries covering every inflection class and exception);
  identical to `Heinrich/crates/heinrich-de-morph/tests/data/sample.lex`, which the engine
  tests use.

Review the forms generated from a file with
`cargo run -p heinrich-de-morph --example dump -- <file.lex> [LEMMA]` in the engine repo.
All entries are written clean-room (see `Heinrich/docs/PLAN.md` §6 and `../../SOURCES.md`).

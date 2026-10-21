# Latin lexicon (`la/lexicon/`)

Our own Latin lexicon (classical school Latin with vowel lengths), written clean-room by author
sessions from their own knowledge and checked by a separate reviewer session.

- Format: `Heinrich/docs/LEXICON_FORMAT_LA.md`.
- Authoring protocol: [`AUTHORING.md`](AUTHORING.md).
- Plan and decisions: `Heinrich/docs/LATIN.md` (L-D2 norm, L-D3 vowel lengths and size, L-D4
  clean-room).
- The engine builds the Latin morphology pack from this directory.

## Status

As of 2026-10-21: no entries yet. The authoring protocol was written before the first author wave.

## Record of pull requests

| PR | authors | content | review |
|---|---|---|---|
| – | orchestrator | `AUTHORING.md` and this README, written before the first wave | – |

## Review

The Latin lexicon is written clean-room (Heinrich `CLAUDE.md` rule 2, `docs/LATIN.md` L-D4): the
authors never see a third-party lexicon. A separate reviewer compares the entries with third-party
data **outside the repositories** and reports only *disputed* entries (lemma, field, reason in the
reviewer's own words), *missing* lemmas and statistics, never a value taken from a reference
(`AUTHORING.md` §1). No reference data is committed to `heinrich` or `heinrich-data`.

### Reference data (reviewer only, kept outside the repositories)

| reference | version | licence | used for |
|---|---|---|---|
| kaikki.org Latin (Wiktextract dump of the English Wiktionary) | download of 2026-10-21 | CC BY-SA 4.0 / GFDL | used outside the repositories for comparison only; no values flow into the lexicon. Main reference: lemma and principal parts with vowel lengths, gender, and the inflected forms with macrons |
| UniMorph `lat` | download of 2026-10-21 | CC BY-SA (derived from the English Wiktionary) | used outside the repositories for comparison only. Cross-check of paradigm cells; not an independent source for vowel lengths |
| Whitaker's Words (`DICTLINE.GEN`, `INFLECTS.LAT`, `UNIQUES.LAT`) | mk270/whitakers-words, master of 2026-10-21 | free for any use (author's notice) | used outside the repositories for comparison only. Second opinion on stems, declension, conjugation and gender; it has no vowel lengths |

Vowel lengths have no reference independent of Wiktionary; where the reference marks a vowel as
of either length, both readings count as agreeing. Hidden quantities (a long vowel before two
consonants) are the place where references disagree most; such disputes are reported apart from
the other length disputes, so that the author can weigh them. Judgements the references do not
cover (school norm, register, the reading canon) rest on the reviewer's own knowledge.

### Method

1. Build `heinrich-lexicon` from the Heinrich branch `latin` and run `--lang la validate` on each PR
   head; note the commit reviewed.
2. Merge all open PRs of a wave into a scratch copy of `latin` and validate again, to find
   duplicates between the authors (the same lemma in two letter ranges or in a closed-class file,
   a `var=` spelling written as an entry of its own).
3. `dump` the changed files and compare each lexeme with the reference entry of the same lemma
   and part of speech: first the lemma itself (a lemma found only after removing the macrons is a
   length dispute of the principal part), then gender, then every generated single-word form.
   Forms are compared twice: by letters (form missing or extra) and, where the letters agree, by
   macrons (length dispute).
4. Read every difference by hand: error, accepted double form, poetic or archaic form the
   generator does not produce on purpose, gap or inconsistency of the reference. Also read by
   hand: the closed classes, the irregular verbs, every entry with written cells, `style=`,
   `conf=` below 100 or `var=`, and lemmas the reference does not know.
5. *Missing*: uncovered forms of our own frequency list `la/frequency/forms.tsv`, mapped to lemmas,
   per letter range, most frequent first.
6. Report each PR as a comment on the PR and to the orchestrating session; re-check older findings
   against the current `dump` before repeating them.

A calibration run on the engine's own fixture (`crates/heinrich-la-morph/tests/data/sample.lex`,
401 lexemes, Heinrich `latin` 36770a4) found no error in the generated forms; the four length
differences it showed were inconsistencies of the reference.

### Statistics per review round

| round | PR | commit | entries checked | clear errors | points | quote clear / all |
|---|---|---|---:|---:|---:|---:|

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

### Reporting vowel lengths

The length of a single vowel is a yes-or-no question, so "length of the a disputed" gives away the
reference's value. Length disputes are therefore reported **at word level** ("length in the
lemma", "length in the oblique cases", "length in the supine"), without naming the vowel, whenever
the word has more than one candidate vowel. A length that an author changes only because of a
report, and not from their own derivation, carries `conf=` below 100 and `note=reviewer-dispute`,
so that it never counts for a hard error (`AUTHORING.md` §1). In wave 1 some reports still named
the vowel (*vīcissim*, *dēcenter*, *atrium*, *biduum*, *fūnditus*, *Mārius* and the hidden
quantities); the entries changed after those reports fall under this rule.

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
| 1 | #160 p–z | 3cd3b5b | 815 | 5 | 13 | 0.6 % / 1.6 % |
| 1 | #162 e–o | e3322ba | 884 | 2 | 11 | 0.2 % / 1.2 % |
| 1 | #163 a–d + `closed/` | 1d282b0 | 1,216 | 4 | 15 | 0.3 % / 1.2 % |
| 1 | re-check #160 | 14e6b6a | 815 | 0 | 1 | – |
| 2 | #166 p–z | e0daebc | 501 | 5 | 16 | 1.0 % / 4.2 % |
| 2 | #167 e–o | 0b4f672 | 490 | 4 | 15 | 0.8 % / 3.9 % |
| 2 | #168 a–d + `closed/` | 488edb3 | 600 | 6 | 5 | 1.0 % / 1.9 % |
| 2 | re-check #166, #167, #168 | e641baa, 93fd196, 4494e66 | 1,591 | 0 | 0 | – |
| 3 | #170 p–z | b7a6d30 | 253 | 1 | 5 | 0.4 % / 2.4 % |
| 3 | #171 a–d | 0446cff | 241 | 4 | 5 | 1.7 % / 3.7 % |
| 3 | #172 e–o | 6cda8f5 | 276 | 3 | 4 | 1.1 % / 2.6 % |
| 3 | re-check #170, #171, #172 | 1c67d04, 49be76c, 93516fc | 770 | 0 | 0 | – |
| gap | #175 e–o | eece249 | 24 | 0 | 3 | 0 % / 12.5 % |
| gap | #176 p–z | 1303be4 | 7 | 1 | 1 | 14 % / 29 % |
| gap | #177 a–d | 4518148 | 28 | 0 | 6 | 0 % / 21 % |
| gap | re-check (merged) | 3de60f0 | 59 | 0 | 0 | – |

"Clear errors" are wrong lengths or forms; "points" also count uncertain or hidden quantities,
consistency between the authors and minor points. #163 includes the 4 duplicates between the
authors found on the merge of all three waves (*posteā*, *tandem*, *praesum*, *supersum*; settled
by the orchestrator). After the merge of wave 1 (2,943 entries), our frequency list
`la/frequency/forms.tsv` is covered at 99.2 % of the tokens of the top 1,000 forms, 95.6 % of ranks
1,001–5,000 and 86.7 % overall.

In wave 2, length disputes were reported at word level. The clear points were almost all
inconsistencies within the lexicon: a lemma whose length differs from the rest of its word family
(*famōsus* beside *fāma*, *admīsceō* beside *misceō*, the *pro-* compounds before *f*), and the
supines of the *ūrō* compounds, which the three authors had treated differently. Many rarer words
and names raised the share of points. After the merge of wave 2 (4,597 entries) the frequency list
is covered at 99.2 % of the tokens of the top 1,000 forms, 96.2 % of ranks 1,001–5,000, 88.5 % of
ranks 5,001–20,000 and 90.8 % overall.

Wave 3 added a check of every `var=` spelling against the lemmas and forms of all three authors. It
found two entries made twice in wave 1, each written by one author as the main form and by another
as the variant (*Carthāgō*/*Karthāgō*, *Aeduī*/*Haeduus*). The orchestrator settled both, and the
check now runs in every round. The clear points were again inconsistencies within word families
(*biformis* beside *fōrma*, *dēpascor* beside *pāscō*) and, in two cases, the long vowel of *in-*
before *f* (format §1). The engine gap of *vēneō* (the long first vowel lost in the present system) was
passed to the engine. After the merge of wave 3 (5,303 entries) the frequency list is
covered at 99.2 % of the tokens of the top 1,000 forms, 96.3 % of ranks 1,001–5,000, 90.9 % of ranks
5,001–20,000 and 92.0 % overall.

The gap round after a hand check of school reading added mostly proper names of the *Bellum
Gallicum*. Most points there were lengths of Celtic names, where the reference is itself uncertain;
they were kept with `conf=` below 100 or decided again. The river names in *-a* were made masculine
in all three letter ranges. After the gap round the lexicon holds 5,360 entries.

# Spanish lexicon (`es/lexicon/`)

Our own Spanish lexicon (Spanish of Spain, RAE/ASALE orthography 2010), written clean-room by
author sessions from their own knowledge and checked by a separate reviewer session. Format:
`Heinrich/docs/LEXICON_FORMAT_ES.md`; authoring protocol: [`AUTHORING.md`](AUTHORING.md).
The engine builds `es-morph.pack` (core) and `es-morph-ext.pack` (extension) from it
(`tools/build-packs.sh`).

## Status

As of 2026-10-21 (branch `spanish` d8791fc, `heinrich-lexicon --lang es stats` / `coverage`): 29,610
entries, 30,890 lexemes, 355,021 forms (45 forms only in the spelling before 2010, 1,302 accepted
variants); `validate` 0 errors, 0 warnings.

| part of speech | entries |
|---|---:|
| noun | 17,442 |
| adj | 7,300 |
| verb | 4,360 |
| adv | 239 (plus the `-mente` adverbs generated through `adv=`) |
| num | 81 |
| pron | 61 |
| intj | 39 |
| det | 37 |
| adp | 28 |
| cconj, sconj | 9 each |
| aux (`ser`, `estar`, `haber`) | 3 |
| x | 2 |

| letters | entries |
|---|---:|
| a–c | 8,249 |
| d–l | 9,836 |
| m–p | 6,179 |
| q–z | 5,068 |
| `closed/` | 278 |

Token coverage of `es/frequency/forms.tsv` (numbers left out; enclitic forms counted): ranks
1–10,000 97.7 %, 10,001–20,000 85.3 %, 20,001–50,000 75.9 %, 50,001–100,000 61.3 %, all 94.4 %.

## Record of PRs

| PR | authors / letters | content | review |
|---|---|---|---|
| #129 | a–c | open classes a–c, all closed classes, `ser`/`estar`/`haber`/`ir` as full tables, waves 1–7 | round 1 (ae76198): 3,246 entries, 1 clear error, 6 points; round 2 (2b80d1b, 30a8bae): 4 points in new waves, all re-decided; approved |
| #124 | d–l | open classes d–l, waves 1–5 | round 1 (6e24921): 7,304 entries, 1 clear error, 7 points (incl. cross-author duplicates); round 2 (e5252e2, 0282a56): 1 light point, re-decided; approved |
| #121 | q–z | open classes q–z, waves 1–5 | round 1 (1e7b937): 4,635 entries, 3 clear errors, 12 points (incl. 2 generator gaps, duplicates); round 2 (1b80cd2): 1 point, re-decided; approved |
| #127 | m–p | open classes m, n, ñ, o, p, waves 1–4 | round 1 (cdce759): 6,155 entries, 2 clear errors, 9 points; round 2 (0c1ed73): 0 points; approved |

## Review

The Spanish lexicon is written clean-room (Heinrich `CLAUDE.md` rule 2, `docs/SPANISH.md` S-D6):
the authors never see a third-party lexicon. A separate reviewer session compares the authors'
entries with third-party data **outside the repositories** and reports only *disputed* entries
(lemma, field, reason in the reviewer's own words), *missing* lemmas and statistics. No reference
data is committed to `heinrich` or `heinrich-data`.

### Reference data (reviewer only, kept outside the repositories)

| reference | version | licence | used for |
|---|---|---|---|
| kaikki.org Spanish (Wiktextract dump of Wiktionary) | download of 2026-10-21 | CC BY-SA 4.0 / GFDL | used outside the repositories for comparison only; no values flow into the lexicon. Form-by-form comparison of the generated paradigms (gender, plural, feminine, verb forms, participles, spelling variants) |

UniMorph spa and the Hunspell es_ES word list were cleared for comparison as well but not used in
rounds 1–2 (the UniMorph download failed; kaikki covered the need). The *missing* lists come from
our own frequency list `es/frequency/forms.tsv`, the reference only maps forms to lemmas. Norm
questions of the *Ortografía* of 2010 (orthographic monosyllables, *solo*, *guion*, diacritic
accents) and register judgements rest on the reviewer's own knowledge.

### Method

1. Build `heinrich-lexicon` from the Heinrich branch `spanish` (11a0351) and run `--lang es validate`
   on each PR head; note the commit reviewed.
2. Merge all open PRs into a scratch copy of `spanish` in the planned order and validate again, to
   find duplicates between the authors (the same lemma in two letter ranges or in `closed/`, a
   `var=` spelling written as an entry of its own) and files added by two PRs.
3. `dump` every lexicon file and compare each lexeme with the reference paradigm of the same lemma
   and part of speech: verbs form by form (enclitic forms, which the lexicon does not store, are
   filtered out), nouns by gender, plural and feminine, adjectives by their four forms.
4. Read every difference by hand: error, accepted double form (*evacuo/evacúo*), homograph,
   deliberate convention (`defective=`, `pp_inv`) or gap of the reference. Also read by hand: every
   closed-class file, the 2010 spelling (`trad=`), register entries (`style=`, `alt=`) and lemmas
   the reference does not know.
5. *Missing*: uncovered lowercase forms of `es/frequency/forms.tsv`, mapped to lemmas, per letter
   range, most frequent first; closed-class words and Latin American words listed apart.
6. Round 2: re-check every round-1 point on the new head and sample every lexeme added since
   round 1 in the same way.

### Statistics per review round

"Clear errors" are wrong forms or fields; "points" also count duplicates, generator gaps and minor
points.

| round | PR | commit | entries checked | clear errors | points | quote clear / all |
|---|---|---|---:|---:|---:|---:|
| 1 | #129 a–c + closed | ae76198 | 3,246 | 1 | 6 | 0.03 % / 0.2 % |
| 1 | #124 d–l | 6e24921 | 7,304 | 1 | 7 | 0.01 % / 0.1 % |
| 1 | #121 q–z | 1e7b937 | 4,635 | 3 | 12 | 0.06 % / 0.26 % |
| 1 | #127 m–p | cdce759 | 6,155 | 2 | 9 | 0.03 % / 0.15 % |
| 2 | all four (merged scratch copy) | 2b80d1b, e5252e2, 1b80cd2, 0c1ed73 | 29,610 (8,690 new lexemes sampled) | 0 | 6 | 0 % / 0.02 % |
| final | `spanish` | d8791fc | 29,610 | 0 | 0 | – |
| 6 | #143 a–c + closed (diff) | 887f3f3 | 148 | 1 | 3 | 0.7 % / 2.0 % |
| 6 | #144 d–l (diff) | 71ecf9e | 150 | 7 | 13 | 4.7 % / 8.7 % |
| 6 | #142 m–p (diff) | acf258a | 115 | 0 | 2 | 0 % / 1.7 % |
| 6 | #145 q–z (diff) | 76e8ced | 543 | 0 | 20 | 0 % / 3.7 % |

Recurring findings: adjectives of the form *prefix + noun* (*anticorrupción*, *tricolor*,
*monocolor*, *multiuso*, *bicolor*) got a derived feminine (a validator warning was proposed to the
engine session); stem accents of prefixed verbs (*rehacer*, *contrahacer*, *rehuir*) were generator
gaps, worked around with written tables; duplicates between authors (*ir*, *todavía*, five
spelling-variant pairs, *cinc/zinc*) were settled before the merge.

Wave 6 (gaps of the own frequency list up to rank 100,000) was reviewed on `spanish` e9c57d1 with
all four PRs merged (30,512 entries, 0 errors, 0 warnings, no duplicates between the authors); only
the added or changed lines were checked. New in this round, words that are not usual in the Spanish
of Spain (Latin American doublets such as *sustentabilidad*, *televisora*, *tendiente*) were reported
as points; they make up 19 of the 38 points. The clear errors were mostly loans flagged `foreign`
without `pl=`, which get the native plural after a consonant (*hacker*, *kernel*; three older
entries in m–p have the same gap; a validator hint was proposed), and one gentilic with a generated
feminine. #145 also had *tras-*/*trans-* variants set for some members of a word family only.
The authors settled every point in follow-up commits (#143 031d174, #144 9f672c6, #142 2087ebf,
#145 d7b1a54); the re-check on the merge of these heads found 30,496 entries, 0 errors, 0 warnings
and no open point.

### Protocol deviation in round 1

In round 1 (#129, #124, #121, #127) some of the reviewer's reports stated the expected value
("suggestion: `f=…`", "plural with -es") instead of only the lemma, the field and a reason. This
goes against `AUTHORING.md` §1. The m–p author pointed it out; the reviewer acknowledged it, and
all authors were told to decide these entries again from their own knowledge. From round 2 on,
reports name only the lemma, the field and a reason.

Entries concerned (lemma and field only):

| PR | entries (field) |
|---|---|
| #129 a–c | *anticorrupción* (feminine, plural); *antidopaje*, *antisistema*, *antitanque* (plural); *adecuar* (present stem); *apartheid* (plural) |
| #124 d–l | *ion* (2010 spelling, `trad=`) |
| #121 q–z | *tricolor* (feminine); *sénior* (plural); *rehundir* (class); *rehuir*, *rehacer* (preterite, generator); *rally* (plural variant) |
| #127 m–p | *monocolor*, *multiuso*, *monomotor* (feminine); *peciolado* (variant); *mentís*, *plus*, *newton*, *pitcher* (plural); *marimacho* (gender) |

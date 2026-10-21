# French lexicon sources (`*.lex`)

Format specification, validation checklist (§12) and author guide (§13):
`Heinrich/docs/LEXICON_FORMAT_FR.md`. Authoring protocol (clean-room rules, organisation,
decisions, self-check): [`AUTHORING.md`](AUTHORING.md). Parser and generator:
`Heinrich/crates/heinrich-fr-morph`; pipeline tools: `Heinrich/crates/heinrich-lexicon-tools`
(binary `heinrich-lexicon`, always with `--lang fr`). Only metropolitan French (`fr-FR`) for
now; both spellings of 1990 are generated and marked (`Orth=Trad`, `Orth=Rect`).

## Provenance

All entries are our own data, written **clean-room** from the authors' own knowledge of French:
no third-party lexicon, word list, dictionary or conjugation table was consulted (no Lexique,
Morphalou, DELA, Lefff, GLÀFF, Wiktionnaire/kaikki, UniMorph, Dicollecte/Grammalecte,
Hunspell, Le Robert, Larousse, Bescherelle or online dictionaries; `AUTHORING.md` §1,
`../../SOURCES.md`). The authors used our own frequency counts (`../frequency/forms.tsv`) to
order the work and the generator output to check it. Four author sessions wrote the letters
a–c (with all closed classes), d–l, m–p and q–z in parallel, each in its own PRs against the
branch `french`; a separate reviewer session compared each PR with third-party lexica outside
the repositories and reported only disputed and missing lemmas, never the reference values; the
authors decided those entries again themselves. Written 2026-10-20 and 2026-10-21.

## Content

32,334 entries, 33,522 lexemes, 318,890 forms (6,258 forms correct only in the traditional
spelling, 6,381 only in the 1990 spelling), as of 2026-10-21 (`heinrich-lexicon --lang fr
stats fr/lexicon`).

| part of speech | entries |
|---|---:|
| noun | 19,667 |
| adj | 7,246 |
| verb | 4,697 |
| num | 240 |
| adv | 216 (plus the `-ment` adverbs generated through `adv=` on adjectives) |
| intj | 110 |
| pron | 72 |
| adp | 42 |
| det | 24 |
| cconj, sconj | 9 each |
| aux (`être`, `avoir`) | 2 |

| letters | open-class entries |
|---|---:|
| a–c | 7,230 |
| d–l | 10,981 |
| m–p | 7,251 |
| q–z | 6,412 |
| `closed/` | 462 |

Verbs: 4,062 of the first group (derived), 245 of the second (`class=ir`), the rest in the
third-group classes of format §5.3; `être`, `avoir`, `aller` are full tables.

**Core and extension.** `tools/build-packs.sh` in the engine repo splits the lexicon into two
packs (Heinrich `docs/PACK_FORMAT.md` §2a): the core `fr-morph.pack` with the closed classes and
the frequent lexemes that cover 98 % of the counted tokens the lexicon knows (own counts,
`../frequency/forms.tsv`), and the extension `fr-morph-ext.pack` with all other lexemes (rare
technical vocabulary), which web clients load after the first check.

## Layout

The same as the German and English lexicons:

| directory | contents | files |
|---|---|---|
| `noun/`, `verb/`, `adj/`, `adv/` | open classes by part of speech | `<letter>.lex`: first letter of the lemma, lowercased, accents removed (`é` → `e`, `œ` → `o`) |
| `other/` | `intj`, `x` | `<letter>.lex` |
| `closed/` | closed classes, written by hand: `articles.lex`, `determiners.lex`, `pronouns.lex` (incl. *en*, *y*), `prepositions.lex` (incl. *au, aux, du, des, ès*), `conjunctions.lex`, `adverbs.lex` (degree, negation, interrogation, deixis), `numerals.lex`, `auxiliaries.lex` (`être`, `avoir`) | by function |

Proper nouns are not in the lexicon; names live in `../names/`.

## Tools

Build once in the engine repo (branch `french`):
`cargo build --release -p heinrich-lexicon-tools -p heinrich-cli`, then
(`heinrich-lexicon` = `Heinrich/target/release/heinrich-lexicon`):

```sh
heinrich-lexicon --lang fr validate fr/lexicon                       # errors + lint warnings
heinrich-lexicon --lang fr dump fr/lexicon/verb/a.lex aller          # all generated forms
heinrich-lexicon --lang fr stats fr/lexicon                          # counts per POS and class
heinrich-lexicon --lang fr coverage fr/lexicon fr/frequency/forms.tsv \
    --uncovered /tmp/uncovered.tsv --top 5000                        # coverage + work list
heinrich pack build-morph fr/lexicon --lang fr -o packs/fr-morph.pack
```

## Pull requests

All against `french` in `wi-wissen/heinrich-data`. Review: entries (or changed lines) checked by the
reviewer, clear errors and all points; method and per-round statistics in [Review](#review).

| PR | letters | content | review |
|---|---|---|---|
| #91 | d–l | open classes d–l, frequency waves | 2,233 entries; 1 clear error (0.04 %), 15 points in all (0.7 %); fixed before merge |
| #92 | q–z | open classes q–z, frequency waves | 5,566; 9 clear errors (0.16 %), ~90 points (1.6 %), mostly 1990 variants and feminines of person nouns |
| #93 | a–c | open classes a–c (6,936 lemmas) and all closed classes (415 entries), frequency waves 1–6, review fixes | 7,188 + closed; 7 clear errors (0.1 %), ~200 points (2.8 %, incl. 97 missing `pp_inv`); re-check of the fixes (422 lines): 0 clear errors |
| #94 | m–p | open classes m–p, frequency waves | 6,978; 7 clear errors (0.1 %), ~125 points (1.8 %) |
| #95 | d–l | breadth waves 5b–6 | 1,184 changed lemmas; 1 clear error (0.08 %), 17 points (1.4 %) |
| #96 | q–z | `-ment` adverbs as `adv=` on adjectives | 157 `adv=` values, 43 `adv` entries folded in (none lost); 0 errors, 14 rare adverbs could take `[rare]` |
| #97 | q–z | words from the Wikipedia test | 358; 1 clear error (0.3 %), 2 points |
| #98 | m–p | words from the Wikipedia test | 271; 1 clear error (0.4 %), 2 points |
| #99 | d–l | words from the Wikipedia test | 284; 0 clear errors, 2 light points (0.7 %) |
| #100 | a–c | words from the Wikipedia test (270 lemmas), format 1.2: `rect_only` numerals, *courre*, *croître* | 317; 1 clear error (0.3 %), fixed on the PR |
| #102 | d–l | *dihydrogène* without plural | not reviewed separately (follows the #99 review) |
| #103 | m–p | words from the news and debates test | 31 lines; 0 clear errors |
| #104 | d–l | words from the news and parliament list | 62 lines; 0 clear errors |
| #105 | a–c | words from the news and parliament list (70 lemmas), *comparaître*, *auto-entrepreneur* | 73 lines; 0 clear errors; 2 light points fixed in #107 |
| #106 | q–z | words from news, debates and Wikipedia corrections | 62 lines; 0 clear errors |
| #107 | a–c | *cougar* senses, *bavasser* `pp_inv` | not reviewed separately (fixes from the #105 review) |
| #108 | q–z | *vadémécum* (1990 spelling of *vade-mecum*) | not reviewed separately (answers a #103–#106 review question) |
| #109 | d–l | neutral sense for *lascar* | 2 lines; 0 errors |
| #110 | d–l | colloquial *galérer, kiffer, keuf, daron* | 4 lines; 0 errors, approved |
| #111 | m–p | *maths* standard; colloquial *ordi* | 2 lines; 0 errors, approved |
| #112 | q–z | colloquial *taffer, taf, teuf, relou, zarbi, vénère* | 7 lines; 0 errors, approved |
| #113 | a–c | neutral sense for *crever* and *crevé*; *chelou* | 3 changed entries; 0 errors, approved (1 note) |
| #115 | d–l | *daronne* and *frangine* as own entries | 4 lines; 0 errors, approved (1 note) |
| #128 | q–z | 46 person nouns (feminines, epicene `-iste`, colloquial `-ard` with `alt=`) | 46 lines; 0 errors, approved |

Related data PRs: #87 (French names from open data, `../names/`), #88 (French frequency list
from own counts, `../frequency/`).

## Review

The French lexicon is written clean-room (Heinrich `CLAUDE.md` rule 2, `docs/FRENCH.md` F-D6): the
authors never see a third-party lexicon. A separate reviewer compares the authors' entries with
third-party data **outside the repositories** and reports only *disputed* entries (entry, field,
reason in the reviewer's own words), *missing* lemmas and statistics, never a value taken from a
reference. No reference data is committed to `heinrich` or `heinrich-data`.

### Reference data (reviewer only, kept outside the repositories)

| reference | version | licence | used for |
|---|---|---|---|
| Lexique (lexique.org) | 3.83 | CC BY-SA 4.0 | used outside the repositories for comparison only; no values flow into the lexicon. Lemma frequencies for the *missing* lists and coverage statistics |
| Grammalecte French lexicon (inflected forms, from Dicollecte) | 7.7 | MPL-2.0 | used outside the repositories for comparison only; no values flow into the lexicon. Form-by-form comparison of the generated paradigms (gender, number, plural and feminine forms, all verb forms, auxiliary and pronominal flags, 1990 spelling variants) |

CC BY-SA and MPL data are used for internal measurement only (Heinrich `CLAUDE.md` rule 3); nothing
derived from them flows into the lexicon, the rules or a pack. Wiktionnaire could not be queried
(the API refused automated access), so *h aspiré*, register and other judgements not covered by
the two references rest on the reviewer's own knowledge of French.

### Method

1. Build `heinrich-lexicon` from the current Heinrich `french` branch and run `--lang fr validate`
   on the PR head (errors and warnings are reported, warnings already present on `french` are
   noted as such).
2. Restrict the review to the PR: the full letter range for the first waves, later only the lines
   added or changed against `french` (reordered lines are filtered out).
3. Run `dump` on every changed lexicon file and compare each generated form, with its features,
   against the reference paradigm of the same lemma and part of speech (both spellings of a
   `rect=` lemma are looked up). Mood and tense are kept apart (`Mood=Imp` is the imperative,
   `Mood=Sub|Tense=Imp` the subjonctif imparfait).
4. Read every difference by hand and decide whether it is an error, a variant, a deliberate
   convention (e.g. `pp_inv`, `defective=`) or a gap of the reference. Read by hand, in addition:
   - every closed-class file;
   - every word in *h*;
   - every entry with `style=`, `conf=` below 100 or `defective=`;
   - every lemma the references do not know.
5. Check the 1990 spelling separately: lemmas whose reformed spelling exists in the reference
   but has no `rect=`, lemmas with *î*/*û* without `rect=`, and `rect=` forms that would join two
   identical vowels.
6. *Missing*: lemmas of the letter range ranked by Lexique 3 frequency (books 70 %, films 30 %),
   without numerals, proper names, reference artefacts and participle-adjectives already generated
   from a verb; open classes, adverbs and interjections listed apart.
7. Report each PR to the orchestrating session; re-check older findings against the current
   `dump` before repeating them.

### Statistics per review round

"Clear errors" are wrong forms or fields; the total also counts missing 1990 variants and minor
points (missing `pp_inv`, senses, plural rarely used …).

| round | PR | scope | entries checked | clear errors | all points | quote clear / all |
|---|---|---|---:|---:|---:|---:|
| 1 | #91 | d–l wave 1 | 2,233 | 1 | 15 | 0.04 % / 0.7 % |
| 1 | #92 | q–z | 5,566 | 9 | ~90 | 0.16 % / 1.6 % |
| 1 | #93 | a–c + closed | 7,188 | 7 | ~200 | 0.1 % / 2.8 % |
| 1 | #94 | m–p | 6,978 | 7 | ~125 | 0.1 % / 1.8 % |
| 1 | #95 | d–l waves 5/6 (diff) | 1,184 | 1 | 17 | 0.08 % / 1.4 % |
| 2 | #93 | a–c re-check (diff) | 422 | 0 | 2 | 0 % / 0.5 % |
| 3 | #97 | q–z Wikipedia (diff) | 358 | 1 | 2 | 0.3 % / 0.6 % |
| 3 | #98 | m–p Wikipedia (diff) | 271 | 1 | 2 | 0.4 % / 0.7 % |
| 3 | #99 | d–l Wikipedia (diff) | 284 | 0 | 2 | 0 % / 0.7 % |
| 3 | #100 | a–c Wikipedia (diff) | 317 | 1 | 1 | 0.3 % / 0.3 % |
| 4 | #103–#106 | news additions (diff) | 228 | 0 | 2 | 0 % / 0.9 % |
| 5 | #110–#113, #115 | colloquial words (diff) | 21 | 0 | 3 | 0 % |
| 6 | #96, #109 | `-ment` adverbs q–z, *lascar* (diff, checked after merge) | 159 | 0 | 1 | 0 % / 0.6 % |
| 7 | #128 | person nouns q–z (diff) | 46 | 0 | 0 | 0 % |

Coverage of the reference frequency list, nouns / verbs / adjectives (round 1, open classes,
participle-adjectives counted as covered when the verb is present):

| range | top 500 | top 1000 | top 2000 |
|---|---|---|---|
| a–c (after re-check) | 100 / 100 / 100 % | 100 / 87 / 97 % | 99 / 77 / 82 % |
| d–l (after #95) | 99 / 100 / 99 % | 98 / 98 / 98 % | 97 / 84 / 95 % |
| m–p | 98 / 95 / 99 % | 97 / 83 / 96 % | 94 / 83 / 78 % |
| q–z | 98 / 99 / 96 % | 97 / 89 / 91 % | 92 / 70 / 69 % |

Recurring findings that led to format or validator changes: invariable adjectives in *-o*/*-a*
(warning since 1.2), `pp_inv` together with `aux=être` (warning since 1.1), defective verbs
(`defective=`, 1.1), feminine-only adjectives (`fem_only`, 1.1), joined double vowels in `rect=`
(warning since 1.2), the *ie + consonant + er* verbs (`briefer`).

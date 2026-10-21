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

All against `french` in `wi-wissen/heinrich-data`. Review: the reviewer's result as forwarded
by the orchestrator; disputed/missing counts are completed by the reviewer session.

| PR | letters | content | review |
|---|---|---|---|
| #91 | d–l | open classes d–l, frequency waves | – |
| #92 | q–z | open classes q–z, frequency waves | – |
| #93 | a–c | open classes a–c (6,936 lemmas) and all closed classes (415 entries), frequency waves 1–6, review fixes | ≈ 0.1 % clear errors, all fixed on the PR |
| #94 | m–p | open classes m–p, frequency waves | – |
| #95 | d–l | breadth waves 5b–6 | – |
| #96 | q–z | `-ment` adverbs as `adv=` on adjectives | – |
| #97 | q–z | words from the Wikipedia test | – |
| #98 | m–p | words from the Wikipedia test | – |
| #99 | d–l | words from the Wikipedia test | – |
| #100 | a–c | words from the Wikipedia test (270 lemmas), format 1.2: `rect_only` numerals, *courre*, *croître* | ≈ 0.3 %, fixed on the PR |
| #102 | d–l | *dihydrogène* without plural | – |
| #103 | m–p | words from the news and debates test | – |
| #104 | d–l | words from the news and parliament list | – |
| #105 | a–c | words from the news and parliament list (70 lemmas), *comparaître*, *auto-entrepreneur* | 0 clear errors; 2 light points fixed in #107 |
| #106 | q–z | words from news, debates and Wikipedia corrections | – |
| #107 | a–c | *cougar* senses, *bavasser* `pp_inv` | – |
| #108 | q–z | *vadémécum* (1990 spelling of *vade-mecum*) | – |
| #109 | d–l | neutral sense for *lascar* | – |
| #110 | d–l | colloquial *galérer, kiffer, keuf, daron* | – |
| #111 | m–p | *maths* standard; colloquial *ordi* | – |
| #112 | q–z | colloquial *taffer, taf, teuf, relou, zarbi, vénère* | – |
| #113 | a–c | neutral sense for *crever* and *crevé*; *chelou* | – |
| #115 | d–l | *daronne* and *frangine* as own entries | – |

Related data PRs: #87 (French names from open data, `../names/`), #88 (French frequency list
from own counts, `../frequency/`).

# Authoring protocol for Spanish lexicon entries

This is the working protocol for **author agents** (and humans) who write entries for the
Spanish lexicon. It complements the format specification `Heinrich/docs/LEXICON_FORMAT_ES.md`
(read §1–§5 and §8 first; the validation checklist is §12, the author guide §13) and follows
the German, English and French protocols (`../../de/lexicon/AUTHORING.md`,
`../../en/lexicon/AUTHORING.md`, `../../fr/lexicon/AUTHORING.md`) wherever Spanish allows.
It was written before the first author wave and records how the lexicon is built (§2), so that
the procedure can be traced later (`Heinrich/docs/SPANISH.md`, "Provenance record").

## 1. Clean-room rules (non-negotiable, identical to the other languages)

- **Never consult a third-party lexicon, word list, dictionary or conjugation table**: no
  Wiktionary/kaikki, UniMorph spa, Hunspell/aspell/LibreOffice Spanish dictionaries, FreeLing,
  Apertium, LanguageTool's Spanish dictionary, the RAE/ASALE dictionaries (DLE, DPD, Ortografía
  online), CREA/CORPES lists, Clave, María Moliner, SpanishDict, WordReference or any other
  online dictionary or conjugation site, nor web searches for spellings, genders, plurals or
  conjugations. Do not open such files even if they are on disk. The repository `heinrich-eval`
  is off limits for authors.
- **Allowed sources:** your own knowledge of Spanish; our own frequency counts
  (`es/frequency/forms.tsv`, also for corpus evidence such as which of two spellings is more
  common); the generator output (`heinrich-lexicon --lang es dump`); the existing entries in
  this directory; work lists of forms produced by our own tools or by the orchestrator from our
  own test texts. A work list only names forms. Every field of an entry is decided by the author.
- **The reviewer is a different agent.** It compares the lexicon with third-party lexica outside
  the repositories and reports only *which* lemmas are disputed or missing, plus statistics,
  never the reference value. When an entry comes back as disputed, the author re-derives it
  from their own knowledge (and corpus counts or the rules of the format) and decides again;
  never ask for or guess the reference's answer. Comparison data is never committed
  (Heinrich `CLAUDE.md` rule 5).
- **Proper nouns are not in the lexicon.** Given names, surnames and place names live in the
  names pack (`../names/`, built from INE and GeoNames open data, `../../SOURCES.md`). Demonyms
  and origin adjectives in lowercase (`español`, `madrileño`, `gallego`) are ordinary entries.
- **Norm:** Spanish of Spain (`es-ES`) and the RAE/ASALE orthography of 2010 (`Heinrich/docs/SPANISH.md`
  S-D2, S-D9). Latin American forms (voseo, *computadora*) are not written in version 1, except
  words that are common in Spain as well.
- Everything you write is our own data. Notes, file headers and commit messages are in English;
  the entries are Spanish.

## 2. Organisation and work packages

The lexicon is written in parallel by **four author sessions**, split by the first letter of
the lemma without accents (`á` → `a`, `ñ` sorts after `n` and belongs to the m–p author):

| authors | letters | also |
|---|---|---|
| a–c | `a`, `b`, `c` (incl. `ch`) | all closed classes in `closed/` (articles, determiners, pronouns incl. clitics, prepositions and contractions *al*/*del*, conjunctions, grammar adverbs, numerals), `ser`, `estar`, `haber`, `ir` as full tables |
| d–l | `d` … `l` (incl. `ll`) | – |
| m–p | `m`, `n`, `ñ`, `o`, `p` | – |
| q–z | `q` … `z` | – |

An **orchestrator session** assigns the work, merges the PRs into the branch `spanish`, runs the
tests on real texts and forwards work lists and review results. The **S1 engine session** owns the
format and the generator (`Heinrich/docs/LEXICON_FORMAT_ES.md`, `crates/heinrich-es-morph`) and
fixes generator gaps the authors report. A separate **reviewer session** checks each PR (§1).
Authors never edit another author's files. The closed classes belong to the a–c author whatever
their letter: the other authors write no `det`, `pron`, `adp`, `cconj`, `sconj` or `num`, and none
of the grammar adverbs of degree, negation, interrogation and deixis (*muy, no, más, dónde, aquí*).
Content adverbs (*siempre, pronto*, the `-mente` adverbs through `adv=`) stay with their letter's
author.

Boundary as settled on 2026-10-21 (question of the q–z author): the closed classes include the
grammar adverbs of degree (*muy, tan, tanto, más, menos, bastante, demasiado, casi*), of negation,
affirmation and focus (*no, sí, nunca, jamás, tampoco, también*), interrogative and relative adverbs
(*dónde, cuándo, cómo, cuánto*) and deictic and time-reference adverbs (*aquí, ahí, allí, acá, allá,
hoy, ayer, ahora, entonces, ya, todavía, aún*), and ordinals as `num`. *siempre, tarde, temprano,
quizá(s)*, the `-mente` adverbs and *solo* (adjective and adverb with `trad=sólo`) belong to the
letter authors.

Rounds:

1. **Frequency waves.** Waves of about 1,000 lemmas, the most frequent words first: the lowercase
   forms of `es/frequency/forms.tsv` in the author's letters that the lexicon does not generate
   yet, grouped by the author into lemmas; then core vocabulary and common technical words from own
   knowledge. After each wave: validate (0 errors), spot-check the generated forms, commit, push,
   and report the number of lemmas and the coverage (§5) to the orchestrator. The first wave opens
   a draft PR against `spanish`.
2. **Review round.** The reviewer's disputed/missing list per PR; the author decides each entry
   again and pushes the fixes on the same PR (or a new PR if the first one is merged).
3. **Real-text rounds.** Unrecognised lowercase forms from own test texts, sent per letter by the
   orchestrator; authors keep only real Spanish words.
4. **Rule-driven rounds.** Small tasks from the work on the grammar rules (register entries with
   neutral alternatives, senses, format updates).

## 3. Output: entries in shards

- Write each lemma to its shard `<dir>/<letter>.lex` (format §10); keep shards sorted (`validate`
  warns; `ñ` after `n`).
- **One lemma per entry.** Inflected forms and forms with enclitic pronouns (*dámelo*) are never
  lemmas; the engine attaches and splits clitics at run time.
- Regular words need no fields; irregular parts are written as **complete real words** (format
  §5 overrides), never as ending codes.
- Spelling variants are **one entry** (`trad=`, `var=`, tags, format §8). Never write the other
  spelling as an entry of its own.
- Mark uncertainty honestly: `conf=` below 100 **and** a `note=` saying what is unsure.

## 4. Decisions per entry

Follow the author guide (format §13). The points that need the most care:

- **Nouns:** gender always (`g=m|f` for common gender, `amb` for ambiguous nouns such as *mar*);
  plural exceptions and accent shifts (*régimen/regímenes*, *carácter/caracteres*); invariable
  plurals (*la crisis/las crisis*); `f=` for person and animal nouns.
- **Adjectives:** feminine and apocope (*buen, gran, primer*), `adv=` for every common `-mente`
  adverb, comparison where irregular.
- **Verbs:** a class for every irregular verb (stem change, `-zco`, `-go`, model verbs), `hiatus`
  or `diphthong` for every `-iar`/`-uar` verb, irregular participles and double participles,
  `pronominal`, `impersonal`, `defective=`.
- **Register (format §11):** `style=` only when the whole entry is colloquial, vulgar, archaic or
  offensive, with `alt=`; a word colloquial in only one use gets two entries with `sense=`.
- **Generator gaps:** report them to the S1 session (lemma, form, what it is) instead of working
  around them.

## 5. Self-check and measurement (mandatory before every push)

Build the tools in the engine repo (branch `spanish`):
`cargo build --release -p heinrich-lexicon-tools -p heinrich-cli`.

1. `heinrich-lexicon --lang es validate es/lexicon` – **zero errors**; validate the whole lexicon,
   not only your shards, so that duplicates across authors show.
2. `heinrich-lexicon --lang es dump <shard> <lemma>` for every new or changed entry, read in
   frames: *el/la ___, los/las ___*; *yo ___, nosotros ___, ellos ___, he ___, ___ré, que yo ___,
   ¡___!*.
3. `heinrich-lexicon --lang es coverage es/lexicon es/frequency/forms.tsv` – token coverage per
   rank band and the most frequent missing forms. Report the share of tokens the lexicon generates,
   in total and for your letters.
4. `heinrich-lexicon --lang es stats es/lexicon` – entries per part of speech and verb class.
5. Commit per wave with a summary, push, and send the numbers to the orchestrator.

## 6. Record

The PRs, their content and the review results are listed in [`README.md`](README.md); the
reviewer adds its method, comparison sources (names and licences only) and statistics per round.

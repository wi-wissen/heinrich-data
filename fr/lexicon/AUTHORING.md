# Authoring protocol for French lexicon entries

This is the working protocol for **author agents** (and humans) who write entries for the
French lexicon. It complements the format specification `Heinrich/docs/LEXICON_FORMAT_FR.md`
(read §1–§4 and §9 first; the validation checklist is §12, the author guide §13) and follows
the German and English protocols (`../../de/lexicon/AUTHORING.md`,
`../../en/lexicon/AUTHORING.md`) wherever French allows. It also records how the lexicon was
actually built (§2, §6), so that the procedure can be traced later.

## 1. Clean-room rules (non-negotiable, identical to German and English)

- **Never consult a third-party lexicon, word list, dictionary or conjugation table**: no
  Lexique/OpenLexicon, Morphalou, DELA, Lefff, GLÀFF, Wiktionnaire/kaikki, UniMorph,
  Dicollecte/Grammalecte, Hunspell/aspell dictionaries (fr_FR …), Le Robert, Larousse,
  Bescherelle, TLFi/CNRTL or any other online dictionary or conjugation site, nor web searches
  for spellings, genders, plurals or conjugations. Do not open such files even if they are on
  disk (e.g. a scratch directory). The engine checkout of the comparison tooling
  (`heinrich-eval`) is off limits for authors.
- **Allowed sources:** your own knowledge of French; our own frequency counts
  (`fr/frequency/forms.tsv`, also for corpus evidence such as which of two spellings is more
  common); the generator output (`heinrich-lexicon --lang fr dump`, the `conj` example of
  `heinrich-fr-morph`); the existing entries in this directory; work lists of forms produced
  by our own tools or by the orchestrator from our own test texts (§2). A work list only names
  forms. Every field of an entry is decided by the author.
- **The reviewer is a different agent.** It compares the lexicon with third-party lexica outside
  the repositories and reports only *which* lemmas are disputed or missing, plus statistics,
  never the reference value. When an entry comes back as disputed, the author re-derives it
  from their own knowledge (and corpus counts or the rules of the format) and decides again;
  never ask for or guess the reference's answer. Comparison data is never committed
  (Heinrich `CLAUDE.md` rule 5).
- **Proper nouns are not in the lexicon.** Given names, surnames and place names live in the
  names pack (`../names/`, built from official open data, `../../SOURCES.md`). Demonyms and
  origin adjectives in lowercase (`français`, `capétien`, `clermontois`) are ordinary entries.
- Everything you write is our own data. Notes, file headers and commit messages are in English;
  the entries are French.

## 2. Organisation and work packages

The lexicon was written in parallel by **four author sessions**, split by the first letter of
the lemma without accents (`é` → `e`, `œ` → `o`):

| authors | letters | also |
|---|---|---|
| a–c | `a`, `b`, `c` | all closed classes in `closed/` (articles, determiners, pronouns incl. *en*/*y*, prepositions and contractions, conjunctions, grammar adverbs, numerals), `être`/`avoir` and `aller` as full tables |
| d–l | `d` … `l` | – |
| m–p | `m` … `p` | – |
| q–z | `q` … `z` | – |

An **orchestrator session** assigned the work, merged the PRs into the branch `french`, ran the
tests on real texts and forwarded the work lists and the review results. The **F1 engine
session** owned the format and the generator (`Heinrich/docs/LEXICON_FORMAT_FR.md`,
`crates/heinrich-fr-morph`) and fixed the generator gaps the authors reported. A separate
**reviewer session** checked each PR (§1). Authors never edit another author's files. The
closed classes belong to the a–c author whatever their letter: the other authors write no
`det`, `pron`, `adp`, `cconj`, `sconj` or `num`, and none of the grammar adverbs of degree,
negation, interrogation and deixis (*très, trop, ne, pas, plus, où, ici, là, voici* …). Content
adverbs (*souvent, toujours*, the `-ment` adverbs through `adv=`) stay with their letter's
author.

Rounds:

1. **Frequency waves.** Waves of about 1,000 lemmas, the most frequent words first: the
   lowercase forms of `fr/frequency/forms.tsv` in the author's letters that the lexicon did not
   generate yet, grouped by the author into lemmas; then core vocabulary and common technical
   words from own knowledge. After each wave: validate (0 errors), spot-check the generated
   forms, commit, push, and report the number of lemmas and the coverage (§5) to the
   orchestrator. The first wave opens a draft PR against `french`.
2. **Review round.** The reviewer's disputed/missing list per PR; the author decides each entry
   again and pushes the fixes on the same PR.
3. **Real-text rounds.** The orchestrator ran the lexicon on held-out real texts (600 French
   Wikipedia articles; error-free news articles, parliament speeches and Wikipedia correction
   sentences) and sent each author the unrecognised lowercase forms of their letters, unfiltered.
   Authors kept only real French words (technical and scientific terms, derivations, origin and
   period adjectives, common *anti-*/*co-*/*bio-* compounds) and left out English, Latin,
   transliterations, typos of the source texts, old spellings (*avoit*, *connoître*), fragments
   and names. One new branch and draft PR per round.
4. **Rule-driven rounds.** Small tasks from the work on the grammar rules, split by letter:
   register entries (colloquial words with their neutral alternative, neutral senses beside
   colloquial ones), and format updates (1990 hyphenated numerals with `rect_only`, `inf=` for
   *croître*, `defective=`).

## 3. Output: entries in shards

- Write each lemma to its shard `<dir>/<letter>.lex` (format §10): `noun/`, `verb/`, `adj/`,
  `adv/`, `other/` (`intj`, `x`); `closed/` by function. Keep shards sorted by the lemma without
  accents (`validate` warns).
- **One lemma per entry.** Inflected, elided and contracted forms are never lemmas (`l'`,
  `au`, `chantons`). Verb–pronoun inversions (*a-t-il*, *avez-vous*) are split by the
  tokenizer and need no entry. Forms with `oe` for `œ` (*coeur*) are handled typographically by
  the engine and get no variant entry.
- Regular words need no fields (`maison noun g=f`, `chanter verb`, `petit adj`); irregular
  parts are written as **complete real words** (`pl=yeux`, `f=actrice`,
  `pres=dors,dormons,dorment`), never as ending codes.
- Both spellings of 1990 are **one entry** (`rect=`, `rect_pl=`, `[trad]`/`[rect]` tags,
  `rect_only` for words that exist only in the 1990 spelling, format §8). Never write the other
  spelling as an entry of its own.
- Mark uncertainty honestly: `conf=` below 100 **and** a `note=` saying what is unsure.

## 4. Decisions per entry

Follow the author guide (format §13) for each entry. The points that needed the most care:

- **Nouns:** `g=` always; `g=m|f` only for the same form in both genders; nouns whose gender
  changes the meaning are two entries with `sense=`. Plural exceptions (`-al` → `-als`, `-ou` →
  `-oux`, `-ail` → `-aux`, compounds); a person or animal noun gets its feminine as `f=` on the
  masculine (`acteur … f=actrice`, `chef … f=cheffe`), not as a second entry. `pl=-` only with
  a note (fixed phrases: *à califourchon*, *sans cesse*).
- **Adjectives:** say *une ___* and *des ___*; write `f=` for `-eur`, `-c`, `-x`, `-g`, `-f`
  and every adjective whose feminine is the lemma (*accro, chic, cosy*); `mv=` for *bel,
  nouvel, vieil, fol, mol*; `adv=` for every common `-ment` adverb (then no separate `adv` entry;
  `validate` reports the duplicate).
- **Verbs:** first group derived; decide every `-eler`/`-eter` verb (nothing, `class=double`,
  `class=double_trad`); a class for every other verb, `class=irr` with principal parts when
  none fits; `aux=être` or `aux=avoir|être` where it applies; `pronominal` for verbs that
  exist only with *se*; **`pp_inv` for every purely intransitive verb with *avoir*** (*agir,
  appartenir, briller*), never with `aux=être` or `pronominal`; `defective=` and `-` cells for
  defective verbs (*choir, braire, bruire, courre*).
- **Elision:** check every word in *h*: mute or `aspirate`; also vowel-initial words that block
  elision (*onze, oui*, the numeral *un*).
- **Register (format §11):** `style=` only when the whole entry is colloquial, vulgar,
  archaic, literary or offensive, with `alt=` naming the neutral word. A word that is
  colloquial in only one use gets two entries with `sense=`, the neutral one unmarked
  (*crever* `sense=burst` / `sense=die style=colloquial`, *cougar*, *lascar*). Derogatory terms
  for groups of people are ordinary entries with `style=offensive`.
- **Generator gaps:** when the format cannot express a form, report it to the F1 session
  (lemma, form, what it is) instead of working around it, and write a temporary exception
  with a `note=` if needed.

## 5. Self-check and measurement (mandatory before every push)

Build the tools in the engine repo (branch `french`):
`cargo build --release -p heinrich-lexicon-tools -p heinrich-cli`.

1. `heinrich-lexicon --lang fr validate fr/lexicon` – **zero errors**; every remaining warning is
   fixed or justified with a `note=`. Validate the whole lexicon (all letters), not only your
   shards, so that duplicates across authors show.
2. `heinrich-lexicon --lang fr dump fr/lexicon/verb/c.lex croître` for every new or changed
   entry, read in frames: *un/une ___, des ___*; *je ___, nous ___, ils ___, j'ai/je suis ___,
   je ___rai, il faut que je ___*; check which forms carry `Orth=Trad`/`Orth=Rect`.
   `cargo run -p heinrich-fr-morph --example conj -- FILE LEMMA` prints the tables tense by
   tense.
3. `heinrich-lexicon --lang fr coverage fr/lexicon fr/frequency/forms.tsv --uncovered <file>
   --top N` – token coverage per rank band and the most frequent missing forms as the next work
   list. Report the share of tokens the lexicon generates, in total and for your letters.
4. `heinrich-lexicon --lang fr stats fr/lexicon` – entries per part of speech and verb class.
5. Commit per wave with a summary (lemmas added, coverage, forms skipped by reason, entries
   with `conf` below 100), push, and send the numbers to the orchestrator.

## 6. Record

The PRs, their content and the review results are listed in [`README.md`](README.md). The
review statistics there are completed by the reviewer session.

# Authoring protocol for Latin lexicon entries

This is the working protocol for **author agents** (and humans) who write entries for the Latin
lexicon. It complements the format specification `Heinrich/docs/LEXICON_FORMAT_LA.md` (read §1,
§2, the section of your part of speech and the author guide §13 first; validation is §12) and
follows the German, English, French and Spanish protocols (`../../de/lexicon/AUTHORING.md`,
`../../en/lexicon/AUTHORING.md`, `../../fr/lexicon/AUTHORING.md`, `../../es/lexicon/AUTHORING.md`)
wherever Latin allows. It was written before the first author wave and records how the lexicon is
built (§2), so that the procedure can be traced later (`Heinrich/docs/LATIN.md`, "Provenance
record").

Heinrich treats Latin as a **school analysis tool** (`Heinrich/docs/LATIN.md` L-D1): the lexicon
feeds the form analysis, the grammar trainer, the construction hints and the scansion. The forms
must therefore be complete and correct, and **every naturally long vowel must be marked** (L-D3).
A wrong macron in a principal part is wrong in every generated form and in every scanned verse.

## 1. Clean-room rules (non-negotiable, identical to the other languages)

- **Never consult a third-party lexicon, word list, dictionary, grammar table or morphology
  tool.** That means:
  - no Lewis & Short, Georges, Stowasser, Pons, Langenscheidt or other school or online
    dictionaries;
  - no Wiktionary/kaikki, Whitaker's Words, Perseus/Morpheus, LASLA, Collatinus, UniMorph lat,
    Latin WordNet or the Latin Library or Perseus vocabulary tools;
  - no school vocabulary lists (Bamberger Wortschatz, adeo-Norm, Grundwortschatz lists of
    textbooks) and no textbook glossaries;
  - no web searches for genders, genitives, principal parts or vowel lengths.

  Do not open such files even if they are on disk. The repository `heinrich-eval` is off limits
  for authors.
- **Allowed sources:**
  - your own knowledge of Latin;
  - our own frequency counts (`../frequency/forms.tsv`, also for corpus evidence such as which of
    two spellings is more common);
  - the generator output (`heinrich-lexicon --lang la dump`);
  - the existing entries in this directory;
  - work lists of forms produced by our own tools (`heinrich-lexicon --lang la worklist`) or by
    the orchestrator from our own test texts. A work list only names forms. Every field of an
    entry, every macron included, is decided by the author.
- **The reviewer is a different agent.** It compares the lexicon with third-party lexica outside
  the repositories and reports only *which* lemmas and fields are disputed or missing, with a
  reason in its own words and statistics, **never the reference value** (no "should be `ē`", no
  target genitive). When an entry comes back as disputed, the author re-derives it from their
  own knowledge and the rules of the format and decides again; never ask for or guess the
  reference's answer. Comparison data is never committed (Heinrich `CLAUDE.md` rule 5). The
  reviewer checks vowel lengths with particular care (L-D4).
- **Norm:** classical Latin as taught in German schools (L-D2). The lexicon spelling is
  normative:
  - `v` for the consonant;
  - `i` for both vowel and consonant (no `j`);
  - `ae`/`oe`;
  - assimilated prefixes as the school texts write them.

  Archaic, poetic, late and medieval forms are tagged variants (format §2.1, §9), never the main
  form.
- **Proper names** of the school canon are lexicon entries (`propn`) with their inflection, since
  Latin has no separate names pack (`Heinrich/docs/LATIN.md`):
  - persons (`Caesar, Caesaris`, `Cicerō, Cicerōnis`);
  - gods (`Iuppiter, Iovis`, `Venus, Veneris`);
  - peoples, places, rivers (`Gallia`, `Rōma … loc`, `Rhēnus`).

  Write the ones you know to be common in school reading; do not try to be exhaustive.
- Everything you write is our own data. Notes, file headers and commit messages are in English;
  the entries are Latin.

## 2. Organisation and work packages

The lexicon is written in parallel by **three author sessions**, split by the first letter of
the lemma without macrons (format §10: `ōrātor` → `o`):

| authors | letters | also |
|---|---|---|
| a–d | `a`, `b`, `c`, `d` | all closed classes in `closed/`, whatever their letter: personal, demonstrative, relative, interrogative and indefinite pronouns, possessive determiners, numerals (cardinal, ordinal, distributive, numeral adverbs), prepositions, conjunctions, particles (`-que`, `-ne`, `-ve` as `part`, `nōn`, `nē`, `num`, `nōnne`), grammar adverbs of negation, interrogation, place and time reference (`ubi`, `unde`, `quō`, `hīc`, `ibi`, `nunc`, `tum`, `iam`); also `sum` and the irregular verbs `possum`, `prōsum`, `ferō`, `eō`, `volō`, `nōlō`, `mālō`, `fīō`, `edō` as `class=` entries in `closed/irregular.lex` (format §10), so that no other author's `verb/` shard is touched |
| e–o | `e` … `o` | – |
| p–z | `p` … `z` | – |

Roles:

- **Orchestrator session:** assigns the work, merges the PRs into the branch `latin`, measures
  and forwards work lists and review results.
- **L1 engine session:** owns the format and the generator (`Heinrich/docs/LEXICON_FORMAT_LA.md`,
  `crates/heinrich-la-morph`) and fixes the generator gaps the authors report.
- **Reviewer session:** a separate session that checks each PR (§1).

Authors never edit another author's files. The compounds of the irregular verbs (`abeō`,
`afferō`, `adsum`) belong to the author of their letter and use the `class=` of the simple verb.
Content adverbs (`saepe`, `semper`, `statim`, the adverbs generated through `adv`/`adv=`) stay with
their letter's author. A spelling variant (`var=`) belongs to the author of the main form's letter.

Rounds:

1. **Core waves.**
   - **Wave 1 (about 500 lemmas per author):** the most frequent words of the author's letters.
     Take the lowercase forms of `../frequency/forms.tsv` that the lexicon does not generate yet
     (`heinrich-lexicon --lang la worklist`), group them into lemmas and write the lemmas.
     Weight the columns `prose` and `poetry` above `late`, since school reading is classical.
   - **Wave 2 and later:** further frequency bands, then the vocabulary of the reading authors
     (Caesar, Cicero, Nepos, Ovid, Catullus, Vergil, Seneca, Pliny) from own knowledge. The target
     is about 5,000 lemmas in total (L-D3).
   - **After each wave:** validate (0 errors), check the generated forms of every new lemma (§5),
     commit, push, and report the number of lemmas and the coverage to the orchestrator. The
     first wave opens a draft PR against `latin`.
2. **Review round.** The reviewer posts its list of disputed and missing entries for each PR.
   The author decides each entry again and pushes the fixes on the same PR (or a new PR if the
   first one is merged).
3. **Text rounds.** The orchestrator sends unrecognised forms from our own test texts and from the
   frequency list, per letter. Authors keep only real Latin words.
4. **Rule-driven rounds.** Small tasks from the work on constructions, trainer and scansion
   (missing `intr`, deponents, defectives, lengths a verse shows to be wrong).

## 3. Output: entries in shards

- Write each lemma to its shard `<dir>/<letter>.lex` (format §10); keep shards sorted (`validate`
  warns).
- **One lemma per entry.** Inflected forms are never lemmas, and neither are forms with an
  enclitic (`-que`, `-ne`, `-ve`, `-cum`); the engine splits enclitics at run time.
- Regular words need no fields; irregular cells are written as **complete forms with macrons**
  (format §3.5), never as ending codes.
- Spelling variants are **one entry** (`var=`, tags, format §9). Never write the other spelling
  as an entry of its own.
- Homographs that differ in a vowel length are separate lemmas (`malum`/`mālum`, `levis`/`lēvis`);
  homographs with the same lengths and part of speech need `sense=`.
- Mark uncertainty honestly: `conf=` below 100 **and** a `note=` saying what is unsure, above all
  for a vowel length (`conf=80 note=length of the o in the perfect?`).

## 4. Decisions per entry

Follow the author guide (format §13). The points that need the most care:

- **Vowel lengths:**
  - every naturally long vowel in every principal part, including the hidden quantities before
    two consonants that you know (`rēxī`, `scrīptum`, `āctum`);
  - no breves;
  - diphthongs unmarked.
- **Nouns:**
  - genitive with its macrons;
  - gender;
  - the stem class of the third declension when it departs from the rule (`stem=`);
  - `pl_only`/`sg_only`, `loc` for towns and small islands;
  - Greek declension (`greek`).
- **Adjectives:**
  - all principal parts;
  - irregular or missing comparison;
  - the adverb (`adv`/`adv=`);
  - consonant stems (`vetus`).
- **Verbs:**
  - all four principal parts (`-` for a missing one);
  - deponents and semi-deponents;
  - `intr` for verbs without a personal passive;
  - irregular verbs through `class=`;
  - defectives and impersonals.
- **Register:** `style=` only when the whole entry is archaic, poetic, rare, late or medieval.
- **Generator gaps:** report them to the L1 session (lemma, form, what it is) instead of working
  around them; a written cell with `note=generator gap, reported` is the temporary fix.

## 5. Self-check and measurement (mandatory before every push)

Build the tools in the engine repository (branch `latin`):
`cargo build --release -p heinrich-lexicon-tools -p heinrich-cli`.

1. `heinrich-lexicon --lang la validate la/lexicon`: **zero errors**. Validate the whole lexicon,
   not only your shards, so that duplicates across authors show.
2. `heinrich-lexicon --lang la dump <shard> <lemma>` for every new or changed entry, read in the
   frames of format §13: *cum ___, sine ___*; *hodiē ___, herī ___, crās ___*; *sī ___*; *ā ___*.
   Check every macron once more.
3. `heinrich-lexicon --lang la coverage la/lexicon la/frequency/forms.tsv`: token coverage per
   rank band and the most frequent missing forms. Report the share of tokens the lexicon
   generates, in total and for your letters.
4. `heinrich-lexicon --lang la stats la/lexicon`: entries per part of speech and class.
5. Commit per wave with a summary, push, and send the numbers to the orchestrator.

## 6. Record

The PRs, their content and the review results are listed in [`README.md`](README.md). The
reviewer adds its method, its comparison sources (names and licences only) and its statistics per
round.

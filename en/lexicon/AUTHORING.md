# Authoring protocol for English lexicon entries

This is the working protocol for **author agents** (and humans) who write entries for the
English lexicon. It complements the format specification `Heinrich/docs/LEXICON_FORMAT_EN.md`
(read §1–§3, §8 and the checklist §11 first) and follows the German protocol
(`../../de/lexicon/AUTHORING.md`) wherever English allows.

## 1. Clean-room rules (non-negotiable, identical to German)

- **Never consult a third-party lexicon, word list, dictionary or inflection table**: no SCOWL,
  Hunspell/aspell/ispell dictionaries (en_US, en_GB, …), Wiktionary/kaikki, WordNet, UniMorph,
  Moby, CELEX, CMUdict, frequency lists (COCA, BNC, SUBTLEX, wordfreq, Google n-grams), Harper's
  dictionary, LanguageTool files, Merriam-Webster, Oxford, Cambridge, Collins or any other
  online dictionary, nor web searches for spellings or inflection tables. Do not open such files
  even if they are on disk (e.g. a scratch directory).
- Allowed sources: your own knowledge of English, our own frequency counts
  (`en/frequency/forms.tsv`, once it exists; you may grep it for corpus evidence such as whether
  `learnt` or `learned` is more common), the generator output (`dump`), and the existing entries
  in this directory.
- The reviewer is a different agent. It reports only *which* lemmas are disputed or missing,
  never the reference value. When an entry comes back as disputed, re-derive it yourself
  (corpus counts, rules); never ask for or guess the reference's answer.
- Everything you write is our own data. Notes are in English.

## 2. Input: a work list of forms

**Since M7** the main input is the complete, classified work list of real gaps (names, foreign
words, abbreviations and noise are filtered out), grouped into lemma candidates and split into
chunks of 500 for author agents; the pipeline is described in `de/lexicon/AUTHORING.md` §2.1
and `Heinrich/docs/LEXICON_TOOLS.md`:

```sh
heinrich-lexicon --lang en worklist en/lexicon en/frequency/forms.tsv --names de/names \
    --other-lexicon de/lexicon --other-forms de/frequency/forms.tsv \
    --rank 50000 --chunk 500 --out-dir <outside the repos>/worklists/m7/en
```

Real-word coverage per rank band: the same command line with `coverage --real-words` (no
`--rank`, `--chunk`, `--out-dir`). The form lists below remain for targeted work.

Work lists live in `worklists/batch-NNN.tsv` and are produced by

```sh
heinrich-lexicon --lang en next-batch en/lexicon en/frequency/forms.tsv --size 3000 \
    --exclude en/lexicon/worklists/batch-001.tsv … -o en/lexicon/worklists/batch-NNN.tsv
```

(always exclude all earlier batches). The columns are those of the German lists (`rank`, `form`,
`total`, `wiki`, `lit`, `gov`, `sentence_initial_ratio`, `flags`). Flags:

| flag | meaning | usual action |
|---|---|---|
| *(none)* | unknown to the lexicon | find the lemma, write the entry |
| `+Cap` | a mostly sentence-initial capitalized twin was merged in (`Because` → `because`) | write the lowercase lemma |
| `lc-known` | only a lowercase homograph is known (`Bill` while only `bill` exists) | a proper noun? write the `propn` |
| `compound` | a hyphenated form whose parts are known (`well-known`), or a contraction of a known word (`teacher's`, `don't`) | normally no entry (§4.4) |
| `abbr?` | all caps or a short vowelless word (`NASA`, `Mr`) | §4.6 |
| `name?` | internal capital letters (`iPhone`, `McDonald`) | §4.5 |
| `foreign?` | letters outside the English alphabet (`café`, `naïve`) | §4.7 |
| `hyphen` | hyphenated token with an unknown part | write the missing part, rarely the compound (§4.4) |
| `elided` | contains an apostrophe | contractions and possessives are handled by the engine; write the base word |
| `wiki` / `lit` / `gov` | ≥ 90 % of the occurrences come from one source | register hint |

## 3. Output: entries in shards

- Write each lemma to its shard `<dir>/<letter>.lex` (`noun/c.lex` for `cat`, `verb/t.lex` for
  `travel`); keep shards sorted, homographs adjacent.
- **One lemma per entry.** `walk`, `walks`, `walked`, `walking` → one `walk verb` entry.
- Regular words need no fields at all (`cat noun`, `walk verb`); write irregular principal parts
  as **complete real words** (`pl=children`, `past=went pp=gone`, `cmp=better sup=best`).
- American and British spellings are **one entry**: `color noun gb=colour`,
  `realize verb gb=realise|realize`, or a tagged variant `learnt[GB]` (format §8). Never write
  `colour` as a second entry.
- Mark uncertainty honestly: `conf=` below 100 **and** a `note=` saying what is unsure.
- Do not invent forms: `pl=-` only for uncountable nouns, with a note.
- The closed classes in `closed/` are hand-curated. If a work-list form looks like a missing
  closed-class word (pronoun, determiner, preposition, conjunction, auxiliary, numeral),
  **report it** instead of adding it elsewhere.

## 4. Decisions per form

### 4.1 Inflection of an existing lemma

```sh
grep -rn "^travel " en/lexicon/
heinrich-lexicon --lang en dump en/lexicon travel
```

If the lemma exists and the form should be generated, fix the entry (a missing variant
`past=dreamed|dreamt`, a missing `double`). If the format cannot express the form, **report a
generator gap** (lemma, form, what it is) instead of working around it.

### 4.2 New lemmas

Determine the lemma (singular, base form, positive), the part of speech and the irregular parts,
then follow the checklist (format §11). Typical cases:

- `-o`, `-f(e)`, `-man`, Latin/Greek nouns: check the plural (`potatoes`, `knives`, `women`,
  `criteria`, `analyses`); `validate` warns about the shapes.
- Verbs with a stressed last syllable double the consonant (`prefer` → `preferred`): `double`.
  Prefixed verbs (`understand`, `overcome`, `unplug`) take `prefix=` and every irregular form
  with the prefix.
- Adjectives: decide `cmp=er` (*bigger*), `cmp=more` (*more beautiful*), `cmp=er|more`, or the
  irregular words; add the `-ly` adverb with `adv=` when it exists.
- Participles used as adjectives (`interesting`, `tired`) are separate `adj` entries only if
  they are compared or have their own meaning; gerunds (`swimming`) are verb forms, not nouns,
  unless lexicalised (`building`, `meeting` with a plural).

### 4.3 Homographs and senses

Same lemma and part of speech with a different paradigm or meaning → `sense=` on both
(`lie verb past=lay pp=lain sense=recline` / `lie verb sense=untruth`). Noun and verb with the
same spelling are different parts of speech and need no sense (`practice noun` /
`practice verb gb=practise`).

### 4.4 Compounds

- Closed compounds (`notebook`, `weekend`) are ordinary entries.
- Hyphenated compounds whose parts are words (`well-known`): **no entry**. Entry only if a part
  is not a word, the plural is not on the last part (`passers-by`), or it is lexicalised
  (`check-in`).
- Open compounds (`ice cream`): no entry; make sure the parts exist.
- The graded vocabulary layer (`en/graded/`) can only grade lexemes, so open compounds are not
  graded (known limitation, `Heinrich/docs/GRADED_VOCAB.md`); closed compounds it needs
  (`classroom`, `homework`) are ordinary entries anyway.

### 4.5 Proper names

- `propn` entries for **geographic names** (countries, states, cities, rivers, continents),
  months and weekdays (`January`, `Monday`: `propn`, plural where
  used: `pl=Mondays`), and well-known institutions written as acronyms (`NASA propn`).
- Demonyms and language names are adjectives and nouns of their own (`English adj`,
  `German noun`); they are capitalized, so put them in the shard of their letter as usual.
- **Persons' first names and surnames: no entries** in phase 1.

### 4.6 Abbreviations

Write them with their periods and the flag `abbr`: `e.g. x abbr note=for example`,
`Mr. propn abbr`, `etc. x abbr`. Acronyms that inflect are nouns (`CD noun`).

### 4.7 Foreign words

Loanwords used as English words are normal entries (`café noun`, `naïve adj`); tokens of foreign-language passages get no entry. Parts of fixed
foreign phrases (`ad hoc`, `per se`) are `x foreign` with a note.

### 4.8 Varieties and regions

- Spelling differs → `gb=`/`us=` or `[US]`/`[GB]` (format §8). Check the classic patterns:
  `-or/-our`, `-er/-re`, `-ize/-ise` (British accepts both: `gb=realise|realize`), `-yze/-yse`,
  `-ense/-ence`, `-og/-ogue`, `-l/-ll` (`fulfill gb=fulfil`), `ae/oe` (`pediatric
  gb=paediatric`), single words (`gray/grey`, `tire/tyre`, `plow/plough`).
- Only the word differs (`lorry`/`truck`, `pavement`/`sidewalk`) → `region=GB` or `region=US`
  on the entry; both words are correct English and are accepted everywhere.

### 4.9 Derogatory terms (`style=offensive`)

Slurs and terms that are derogatory towards groups of people (by ethnicity, nationality,
religion, sexuality, gender or disability) are ordinary entries with `style=offensive`
(`style=archaic|offensive` for historical terms), so they are known words; the engine gives a
neutral hint in the `picky` tier only (`Heinrich/docs/LEXICON_FORMAT_EN.md` §13). Neutral
ethnonyms (`Roma`, `Jew`) are never marked. A lemma with a neutral sense gets its own
`sense=` or stays unmarked: a form is only hinted when every reading is marked (lowercase
`gypsy` is marked, the capitalized neutral `Gypsy` is a separate entry). `alt=` names a
neutral alternative (`_` for a space, `alt=Black_person`) only where one is established and
uncontroversial.

## 5. Self-check (mandatory before handing in)

1. Dump every new or changed entry and read every form:
   `heinrich-lexicon --lang en dump en/lexicon/verb/t.lex travel` – check *two ___*, *he ___*,
   *he ___ed*, *he has ___*, *he is ___ing*, *___er than*, and which forms are `Variety=US/GB`.
2. `heinrich-lexicon --lang en validate en/lexicon` – **zero errors**; every remaining warning
   is fixed or justified in the entry's `note=`.
3. With a frequency list: `heinrich-lexicon --lang en coverage en/lexicon en/frequency/forms.tsv
   --uncovered /tmp/u.tsv --top 5000` – the forms of your batch must no longer be uncovered,
   except the ones you deliberately skipped.
4. Commit the shards (one commit per batch) and write a short summary: entries added/changed,
   forms skipped by reason (`name`, `foreign`, `transparent compound`, `noise`, `generator gap`,
   `closed class missing`), and the lemmas with `conf` below 100.

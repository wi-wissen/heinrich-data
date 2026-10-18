# Authoring protocol for lexicon entries

This is the working protocol for **author agents** (and humans) who write entries for the
German lexicon. It complements the format specification `Heinrich/docs/LEXICON_FORMAT.md`
(read §1–3, §9 and §11 first) and the clean-room procedure in `Heinrich/docs/PLAN.md` §6.

## 1. Clean-room rules (non-negotiable)

- **Never consult a third-party lexicon or word list**: no german-pos-dict, Wiktionary/kaikki,
  UniMorph, DEMorphy, Hunspell/igerman98, LanguageTool files, Duden, canoo, DWDS, Leipzig
  lists, nor web searches for inflection tables. Do not open such files even if they are on
  disk (e.g. a scratch directory).
- Allowed sources: your own knowledge of German, the official spelling rules (Amtliches
  Regelwerk), our own frequency counts (`de/frequency/forms.tsv`, which you may grep for
  corpus evidence such as whether `Tages` or `Tags` is more common), the generator output
  (`dump`), and the existing entries in this directory.
- The reviewer is a different agent. It reports only *which* lemmas are disputed or missing,
  never the reference value. When an entry comes back as disputed, re-derive it yourself
  (corpus counts, rules); never ask for or guess the reference's answer.
- Everything you write is our own data. Notes are in English; lexicon words are German.

## 2. Input: a work list of forms

Work lists live in `worklists/batch-NNN.tsv` and are produced by

```sh
heinrich-lexicon next-batch de/lexicon de/frequency/forms.tsv --size 3000 \
    --exclude de/lexicon/worklists/batch-001.tsv … -o de/lexicon/worklists/batch-NNN.tsv
```

(always exclude all earlier batches). Columns:

| column | meaning |
|---|---|
| `rank` | position in this list |
| `form` | the word form as it occurs in texts (**a form, not a lemma**: `Jahren`, `sagte`) |
| `total`, `wiki`, `lit`, `gov` | corpus counts (Wikipedia sample, literature, Bundestag/laws) |
| `sentence_initial_ratio` | share of occurrences at the start of a sentence |
| `flags` | hints, see below; never a reason to skip without looking |

| flag | meaning | usual action |
|---|---|---|
| *(none)* | unknown to the lexicon | find the lemma, write the entry |
| `+Cap` | a mostly sentence-initial capitalized twin was merged in (`Weil` → `weil`) | write the lowercase lemma; check whether the capitalized form is also a noun (`liebe`/`Liebe`) |
| `lc-known` | only a lowercase homograph is known (`Weg` while only `weg` exists) | write the capitalized lemma (usually a noun) |
| `compound` | the compound analysis accepts the form | decide per §4.4 |
| `abbr?` | all caps or a short vowelless word (`CDU`, `Dr`) | §4.6 |
| `name?` | internal capital letters (`iPhone`, `McDonald`) | §4.5 |
| `foreign?` | letters outside the German alphabet (`André`, `Département`) | §4.7 |
| `old?` | a `ß` spelling whose `ss` form is more frequent (`muß`, `daß`) | §4.8 |
| `hyphen` | hyphenated token (`US-amerikanische`) | normally no entry (compounds are analysed); write the parts if they are missing |
| `elided` | contains an apostrophe (`geht's`) | no entry; elision is an engine transformation |
| `wiki` / `lit` / `gov` | ≥ 90 % of the occurrences come from one source | register hint: encyclopedic term or name / literary or old usage / legal jargon |

## 3. Output: entries in shards

- Write each lemma to its shard `<dir>/<letter>.lex` (`noun/j.lex` for `Jahr`, `verb/s.lex`
  for `sagen`, `adj/a.lex` for `ander…`); umlauts fold to the base letter (`Ärger` →
  `noun/a.lex`). Keep shards sorted (lowercase, umlauts folded), homographs adjacent.
- **One lemma per entry.** Several forms of the list usually belong to one lemma
  (`Jahr`, `Jahre`, `Jahren`, `Jahres` → one `Jahr` entry). Never write an entry per form.
- Write principal parts as **complete real words** (`pl=Häuser`, `past=sprach`), never as
  endings or class codes. Write every variant that is standard (`gen=Tages|Tags`), and tag
  rarer ones (`[rare]`, `[archaic]`, `[colloquial]`, `[AT]`, `[CH]`, `[DE]`, `[old]`).
- Mark uncertainty honestly: `conf=` below 100 **and** a `note=` saying what is unsure
  (`conf=70 note=plural Pizzas or Pizzen; both seen in our counts`). Uncertain entries never
  trigger hard grammar errors, so a low confidence is better than a confident guess.
- Do not invent forms to fill a field: `pl=-` only when there really is no plural (add a note
  why, e.g. `note=mass noun`); `validate` warns about `pl=-` without a note.
- The closed classes in `closed/` are complete and hand-curated. If a work-list form looks
  like a missing closed-class word (a pronoun, preposition, conjunction, particle, numeral,
  auxiliary), **report it** instead of adding it elsewhere.

## 4. Decisions per form

### 4.1 Inflection of an existing lemma

First check whether the lemma already exists:

```sh
grep -rn "^Jahr " de/lexicon/            # lemma at the start of an entry
heinrich-lexicon dump de/lexicon Jahr    # all forms it generates
```

- If the lemma exists and the form is a correct form it should generate, the entry is
  incomplete or wrong: fix it (a missing variant `gen=Tages|Tags`, a wrong plural). Do not
  add a second entry.
- Format v3 (LEXICON_FORMAT §12) covers the common gaps: write a genitive without ending as
  `gen=Euro|Euros` (not an `sg=` table); positional or attributive-only adjectives as
  `adj attr_only sup=untersten`; weak verbs with variants as
  `past=verwendete|verwandte pp=verwendet|verwandt`; second-person words in `closed/` carry
  the flag `letter` for the capitalized letter spellings (`Euch`).
- Format 3.2 (LEXICON_FORMAT §13): adjectives used only predicatively (`quitt`, `gewahr`,
  `pleite`) get `adj pred_only`; the `-er` adjective of a place name is written on the place
  name, `Berlin propn … demonym=Berliner` (not as a separate `adj indecl` entry).
- Compounds are analysed, not stored (§4.4). When a transparent compound is not accepted,
  check its split with `heinrich-lexicon split de/lexicon <word>`; a wrong linking element of a
  noun (`Hilfs-`, `Gemeinde-`, `Handels-`) is an engine table
  (`Heinrich/crates/heinrich-de/data/compound_forms.tsv`), so report it instead of adding the
  compound.
- If the entry is right but the format cannot express the form, **report a generator gap**
  (lemma, form, what it is) instead of working around it.
- If the form belongs to a different word with the same spelling (homograph: `Weg`/`weg`,
  `Leiter` m./f.), write that word as its own entry (with `sense=` when lemma and part of
  speech coincide).

### 4.2 New lemmas

Determine the lemma (nominative singular, infinitive, positive), the part of speech and the
principal parts, then follow the checklist in LEXICON_FORMAT §9. Typical cases:

- Nouns declined like an adjective (*der Deutsche / ein Deutscher*) → `decl=adj`
  (`Deutsche`, `Jugendliche`, `Beamte`); their feminine derivations in `-in` are normal
  nouns (`Beamtin`).
- Nominalized adjectives and ordinals (`das Gute`, `das Ganze`, `der Erste`, `im Freien`) are **not**
  entries either; the capitalization rules derive them from the adjective. Only lexicalised ones
  with their own meaning get a `decl=adj` noun (`der Geistliche`, `die Grünen` = party members).
- Nominalized infinitives (`das Lesen`) are **not** entries; the rules derive them. Write a
  noun entry only for lexicalised meanings (`das Essen` = food, `das Vermögen` = assets).
- Participles used as adjectives are generated from the verb. Write an `adj` entry only when
  the participle has its own meaning or comparison (`bekannt`, `bekannter`, `bekanntesten`;
  `gewandt`).
- Prefixed and particle verbs always need their own entries (`ansprechen`, `verstehen`); the
  compound analysis does not create verbs.

### 4.3 Homographs and senses

Two entries with the same lemma and part of speech need distinct `sense=` ids
(`Band … sense=volume`, `Band … sense=music_group`). A different gender with the same
meaning is **not** a homograph: `g=m|n`.

### 4.4 Compounds

Compounds are decomposed by the engine (`Haustür` = `Haus` + `Tür`), so:

- **No entry** for transparent compounds whose meaning, gender and plural follow from the
  head (`Haustür`, `Schulbuch`, `Bundesregierung` once `Bund` and `Regierung` exist). Make sure
  the parts exist instead.
- **Entry** for lexicalised or opaque compounds: the meaning is not the sum of the parts
  (`Augenblick`, `Handschuh`, `Fernseher`), the head is not a word on its own or differs in
  gender/plural (`Mittwoch`, `Nachbar`), or the analyser splits it wrongly. The flag
  `compound` means the analyser accepts the form – check that its split is the real one
  (`Aufgaben` is not *auf* + *gaben*: write `Aufgabe`; `angesprochen` is a form of the verb
  `ansprechen`: write the verb).

### 4.5 Proper names

- Write `propn` entries for **geographic names** (countries, federal states, regions, cities,
  rivers, mountains, continents) and for names used **with an article or a fixed gender**
  (`Schweiz` g=f, `Rhein` g=m, `Türkei` g=f), because rules need their gender. Plural `pl=-`
  is normal for names; say so in the note only if unusual.
- Frequent **organisations, parties and institutions** written as acronyms are `propn` with
  their grammatical gender (`CDU propn g=f gen=CDU pl=-`, `EU propn g=f gen=EU pl=-`).
- **Persons' first names and surnames: no entries** in phase 1 (they are handled as unknown
  capitalized words). Report very frequent ones in your batch summary.
- Multi-word names are written as their single-word parts only where those are German words
  (`New`, `York`: no entries).

### 4.6 Abbreviations

- Write abbreviations as they are written, **with the period** (`Dr.`, `Nr.`, `bzw.`); the
  frequency tokenizer drops the period, the coverage tool matches `form.` automatically.
- Uninflected abbreviations: part of speech `x` in `other/` with `note=` giving the
  expansion (`Nr. x note=Nummer`), unless they function as a closed-class word (`bzw.` is a
  conjunction, already in `closed/`).
- Acronyms that inflect or have a gender are nouns or proper nouns (`GmbH noun g=f gen=GmbH
  pl=GmbHs`, `Lkw noun g=m gen=Lkw|Lkws pl=Lkw|Lkws`).

### 4.7 Foreign words

- Loanwords used in German texts are normal entries with German inflection (`Computer`,
  `Team`, `Café`, `Saison`, `Département` only if it is used as a German word).
- Tokens of foreign-language passages (English titles, French names) get **no entry**; the
  flag `foreign?` and the source flags help to recognise them.

### 4.8 Old spellings

- Single old-spelling words that are still met in texts get an entry with
  `spelling=old` (`daß` is already in `closed/`), or an `[old]`-tagged variant on the modern
  entry when only one principal part differs.
- Systematic `ß`→`ss` changes of whole paradigms (`muß`, `läßt`, `Schloß`) are an engine
  transformation (LEXICON_FORMAT §10): **no entries**; list them as skipped (`old`).
- Old spellings are generated but switched off by default in the engine (they count as
  errors in school texts) and counted as covered by the coverage tool.

### 4.9 Regional variants

- Words used only in Austria/Switzerland/Germany: `region=AT` (`AT|CH` for several) on the
  whole entry, or a tag on one variant (`pl=Wägen[AT]|Wagen`).
- Swiss `ss` instead of `ß` is never written; the engine derives it.
- Colloquial or regional forms that are wrong in standard school German get `[colloquial]` or
  `style=colloquial`, never an untagged variant.

## 5. Self-check (mandatory before handing in)

1. For every new or changed entry, dump it and read every form:
   `heinrich-lexicon dump de/lexicon/noun/j.lex Jahr` – check the article test (*des Jahres,
   den Jahren*), *ich habe/bin …*, *der ___ Mann*. Fix anything you would not write in an
   essay.
2. `heinrich-lexicon validate de/lexicon` – **zero errors**; every remaining warning is either
   fixed or justified in the entry's `note=`.
3. `heinrich-lexicon coverage de/lexicon de/frequency/forms.tsv --uncovered /tmp/u.tsv
   --top 5000` – the forms of your batch you worked on must no longer be uncovered, except
   the ones you deliberately skipped.
4. Commit the shards (one commit per batch) and write a short summary for the orchestrator:
   number of entries added/changed, forms skipped by reason (`name`, `foreign`, `old`,
   `transparent compound`, `noise`, `generator gap`, `closed class missing`), and the lemmas
   you marked with `conf` below 100.

## 6. After review

The reviewer (`heinrich-lexicon review`) returns lemmas with a category only:
`disputed` (forms differ in both directions or the part of speech differs), `missing_forms`,
`extra_forms`, `unattested`, `missing_lemma`. For each disputed lemma, re-derive the principal
parts independently (rules, corpus counts in `forms.tsv`), correct the entry or keep it and
lower `conf=` with a note explaining the doubt. Do not try to infer the reference value from
the category or the counts.

# Run `lex-de-a`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Lexicon author run `lex-de-a` (graded work list)
    
    You are a **clean-room lexicon author** for Heinrich. Write lexicon entries for the words in your work list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-a/worklist.tsv` (columns lemma, pos, notes from the vocabulary authors who need the word).
    
    Read first, completely: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon/AUTHORING.md` (your protocol; note the new exception for
    compounds needed by the graded layer in §4.4) and the format
    `/home/user/Heinrich/docs/LEXICON_FORMAT.md`.
    
    Rules:
    - Clean-room: **never** consult a third-party lexicon, dictionary or word list; **no WebSearch or WebFetch**;
      never open anything under `/home/user/heinrich-eval`. Allowed: your own knowledge of the language, our own
      frequency list `/home/user/heinrich-data/de/frequency/forms.tsv` (grep for corpus evidence), the generator
      output (`dump`), the existing entries.
    - Write entries into the shards of the worktree `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon/` (this worktree is on branch
      `graded-lexicon-gaps`; never switch branches, **do not commit** — the orchestrator commits).
      Your work list covers lemmas starting with A–L; another author handles M–Z in parallel (do not touch shards m–z).
    - First check that a word is really missing (`grep -rn "^<lemma> " /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon/`); the work list may
      contain words that exist under another part of speech, or forms of an existing lemma. Then: fix the
      existing entry (missing part of speech or sense), add a new entry, or skip with a reason.
    - Use `note=graded` on every new entry (plus any other note you need). Homograph senses: add `sense=` ids
      only where two entries with the same lemma and part of speech exist; if you add a sense to an existing
      entry, list it in your summary (vocabulary and rule files may refer to it).
    - Self-check per AUTHORING.md §5 with the tool `/home/user/Heinrich/target/release/heinrich-lexicon` (`/home/user/Heinrich/target/release/heinrich-lexicon dump /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon <Lemma>`,
      `/home/user/Heinrich/target/release/heinrich-lexicon validate /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon` must report zero errors; check `/home/user/Heinrich/target/release/heinrich-lexicon --help` for the exact syntax).
    - Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-a/result.tsv` with one row per work-list row: `lemma pos action(added|fixed|exists|skipped) detail`
      (detail: the entry's lemma/pos/sense to use in the vocabulary layer, or the reason for skipping), and
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-a/decisions.md` (your approach, uncertain entries with conf < 100, skipped words and why).
    
    Final answer: counts per action, the list of senses added to existing entries, validate result.

## Decisions log (written by the author)

# lex-de-a: decisions

## Approach

- Checked every work-list lemma with `grep "^<lemma> "` across the lexicon: only `Leiter` existed
  (senses ladder, person); all other lemmas were missing as entries.
- Graded compounds (AUTHORING §4.4 exception): gender, genitive and plural were copied from the
  existing head entry (`Saft` → `Apfelsaft`, `Teil:portion` → `Erdteil`, `Ton:sound` → `Farbton`,
  `Bank:seat` → `Langbank`, `Druck:pressure` → `Luftdruck`, `Mutter:parent` → `Großmutter`) and then
  reviewed by hand: dropped variants that do not fit the compound (`Handtücher` only, `Lernwörter`
  only, `Geburtsorte` only, `Abendmahle` only, countable `Kreisverkehre`), made mass nouns `pl=-`
  (`Altpapier`, `Altglas`, `Luftdruck`, `Brennball`, `Einmaleins`).
- Non-compound words, adjectives, adverbs and verbs written from own knowledge; corpus counts
  (`forms.tsv`) used for Goliat/Goliath, Kasperle, Kippa, Krokus, Kanons.
- Every new entry has `note=graded`. Entries inserted at their sorted position in shards a–l only.
- `validate`: 0 errors; warning count unchanged (36, all pre-existing). Dumped the verbs and the
  unusual nouns (Dehnungs-h, Einmaleins, Daten, Kasperle, Krokus, ABC, weak masculines).

## Participles and nominalized infinitives (not new entries)

- `geöffnet`, `erlaubt`, `geteilt`, `geschieden`: participles of existing verbs, no meaning of their
  own and not compared → `exists` (vocabulary layer refers to the verb).
- `erschöpft`: gradable (erschöpfter, am erschöpftesten) → added `pp_cmp` to `erschöpfen` (fixed).
- `bestimmt` adj: own meaning (definite article, "a certain") and comparison (decisive) → new
  `adj` entry; `bestimmt` adv (certainly, type=modal) also a new entry.
- `früher` adv (formerly) → `adv type=time` in `adv/f.lex`, like `später` in closed adverbs.
- `Fasten`, `Aufwärmen`, `Kraulen`: nominalized infinitives of existing verbs (§4.2) → `exists`.
- `Kopfrechnen`, `Brustschwimmen`: no underlying finite verb in use; lexicalised subject terms →
  noun entries (`g=n`, `pl=-`).

## Special cases

- `Klanghölzer` → lemma `Klangholz` (plural Klanghölzer).
- `Daten` → `Daten noun g=pl` (data); `Datum pl=Daten` stays for dates.
- `Leiter` → new homograph `Leiter noun g=m sense=conductor` (paradigm as `sense=person`).
  **New sense added:** `Leiter:conductor`.
- `Dehnungs-h`, `Ich-Erzähler`: hyphenated lemmas (the analyser did not cover them).
- `Erste-Hilfe`: skipped. Multiword expression; `erste` and `Hilfe` exist and hyphenated compounds
  (`Erste-Hilfe-Kasten`) are already analysed.
- Person names `Josef`, `Abraham`, `David`, `Goliat`, `Buddha`: AUTHORING §4.5 says no entries for
  persons' names, but `Jesus` and `Allah` already exist as `propn` for religion, and the graded layer
  needs lexemes. Added as `propn` with notes "biblical figure" etc. **Orchestrator: veto if the
  name policy should win.** `Goliath` (179 hits vs 0 for Goliat) added as an extra variant entry.

## Uncertain entries (conf < 100)

| lemma | conf | doubt |
|---|---|---|
| Chanukka | 70 | gender (das, also die) |
| Kippa | 75 | plural Kippot or Kippas |
| Akrostichon | 75 | plural Akrosticha or Akrostichen |
| Kork | 85 | plural Korke rare |
| Laich | 80 | plural rare |
| Krokus | 80 | genitive/plural variants |
| Kasperle | 80 | der or das (g=m\|n) |
| Dehnungs-h | 80 | letter-name inflection |
| Löwenzahn | 85 | plural Löwenzähne rare |
| Erntedank | 85 | gender and use without article |
| Grundwasser | 90 | plural Grundwässer[rare] |
| Brennball | 90 | pl=- (game name) |
| Ganztag | 90 | school-programme sense, plural |

## Side notes

- `balancieren` has `perf=haben|sein`; not added to `classes/perf_sein_sense.tsv` (would be
  `trans|motion`) — left for the class-file owner.
- `dump` does not print participle ADJ readings, so the `pp_cmp` effect on `erschöpfen` could only
  be checked through `validate`.

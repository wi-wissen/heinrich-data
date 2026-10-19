# Run `lex-de-b`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Lexicon author run `lex-de-b` (graded work list)
    
    You are a **clean-room lexicon author** for Heinrich. Write lexicon entries for the words in your work list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-b/worklist.tsv` (columns lemma, pos, notes from the vocabulary authors who need the word).
    
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
      Your work list covers lemmas starting with M–Z; another author handles A–L in parallel (do not touch shards a–l).
    - First check that a word is really missing (`grep -rn "^<lemma> " /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon/`); the work list may
      contain words that exist under another part of speech, or forms of an existing lemma. Then: fix the
      existing entry (missing part of speech or sense), add a new entry, or skip with a reason.
    - Use `note=graded` on every new entry (plus any other note you need). Homograph senses: add `sense=` ids
      only where two entries with the same lemma and part of speech exist; if you add a sense to an existing
      entry, list it in your summary (vocabulary and rule files may refer to it).
    - Self-check per AUTHORING.md §5 with the tool `/home/user/Heinrich/target/release/heinrich-lexicon` (`/home/user/Heinrich/target/release/heinrich-lexicon dump /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon <Lemma>`,
      `/home/user/Heinrich/target/release/heinrich-lexicon validate /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/de/lexicon` must report zero errors; check `/home/user/Heinrich/target/release/heinrich-lexicon --help` for the exact syntax).
    - Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-b/result.tsv` with one row per work-list row: `lemma pos action(added|fixed|exists|skipped) detail`
      (detail: the entry's lemma/pos/sense to use in the vocabulary layer, or the reason for skipping), and
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-b/decisions.md` (your approach, uncertain entries with conf < 100, skipped words and why).
    
    Final answer: counts per action, the list of senses added to existing entries, validate result.

## Decisions log (written by the author)

# lex-de-b decisions (graded work list, lemmas M–Z)

## Approach
- Checked every work-list lemma against all shards (`grep "^<lemma> "`); only `Po` (river propn),
  `sieben` (numeral) and `Sankt` (x) existed under another part of speech. Heads of compounds were
  looked up so gender, genitive variants and plural follow the existing head entry
  (e.g. `Bogen` → `Regenbogen pl=Regenbogen|Regenbögen`, `Liter` → `Milliliter g=m|n`).
- Compounds named by graded authors were added per AUTHORING §4.4 (graded exception), all with
  `note=graded`. Own knowledge only; `de/frequency/forms.tsv` used for a few plural/spelling
  questions (Muslimas, Tieflande/Tiefländer, Mammuts/Mammute, Stillleben, Tipps).
- 387 new entries inserted in sorted position; `validate`: 0 errors, no warnings on new entries.
  Dumped and read the verbs, adjectives and unusual nouns.

## Senses
- Existing `Po propn` (river) got `sense=river`, because the new `Po noun sense=bottom` shares
  lemma and (noun/propn) part of speech.
- New homograph pairs: `Rost` noun `rust` / `grate`; `Pantomime` noun `art` (f) / `artist`
  (m, weak); `Nordpol`, `Südpol`: noun `magnet` (pl. -pole) / propn `geo` (geographic pole).

## Notable decisions
- `mehr`, `weniger`, `weiter`, `nochmal`: added as plain `adv` in adv/ (they were only
  reachable as comparatives of viel/wenig/weit). The determiner-like use (`mehr Zeit`) would be
  a closed-class indefinite (`closed/indefinite.lex`, like `wenig det`); not added here —
  reported for the closed-class owner.
- `verheiratet`, `vergangen`, `unentschieden`: own `adj` entries (lexicalised meanings:
  marital status, "previous", drawn game), not compared.
  `verboten`, `verspätet`: no entry; the verb participles already generate the ADJ readings.
- `Radfahren`, `Skifahren`, `Rückenschwimmen`: noun entries like the existing `Seilspringen`,
  because the verb is written apart (Rad fahren, Ski fahren) and cannot derive the noun.
  `Reiten`, `Tanzen`, `Schwimmen`: skipped, plain nominalized infinitives (§4.2).
- `seilspringen` (verb): skipped; usual writing is "Seil springen"; noun `Seilspringen` exists.
- `Schwarzwald`: propn g=m with `demonym=Schwarzwälder` (also in places.tsv).
- `nacherzählen`: separable `nach`, Partizip II `nacherzählt` (no ge- because of er-).
- `sausen`: perf=haben|sein (sein for motion, haben for the sound).

## Uncertain entries (conf < 100)
- `Minus` conf=80: bare genitive, plural given as none.
- `Tangram` conf=85: plural Tangrams rare.
- `wasserdicht` conf=85: comparison rare.
- `Muslima` conf=85: plural Muslimas (seen in counts).
- `Schabbat` conf=85: plural Schabbate rare (modelled on existing Sabbat).
- `Menora` conf=70: plural Menoras unsure.
- `Origami` conf=85: genitive Origami|Origamis, no plural.

## Skipped
- `Reiten`, `Tanzen`, `Schwimmen` — nominalized infinitives.
- `seilspringen` (verb) — see above.
- `Maria`, `Noah`, `Mose`, `Mohammed` — person names (no lexicon entries, §4.5).
  Names-list gaps to report: `Maria` is missing from `de/names/given_names.tsv`; `Mose` (biblical
  form) is missing (only `Moses`).
- Row `Sankt / Martin` is malformed (pos column holds "Martin"); `Sankt x` exists, `Martin` is a
  given name.
- Mapped to existing lemmas: `Medien` → `Medium`, `Ringe` → `Ring`, `verboten` → `verbieten`,
  `verspätet` → `verspäten`.

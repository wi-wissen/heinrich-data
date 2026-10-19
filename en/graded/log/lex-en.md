# Run `lex-en`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Lexicon author run `lex-en` (graded work list)
    
    You are a **clean-room lexicon author** for Heinrich. Write lexicon entries for the words in your work list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en/worklist.tsv` (columns lemma, pos, notes from the vocabulary authors who need the word).
    
    Read first, completely: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/en/lexicon/AUTHORING.md` (your protocol; note the new exception for
    compounds needed by the graded layer in §4.4 and the note on open compounds) and the format
    `/home/user/Heinrich/docs/LEXICON_FORMAT_EN.md`.
    
    Rules:
    - Clean-room: **never** consult a third-party lexicon, dictionary or word list; **no WebSearch or WebFetch**;
      never open anything under `/home/user/heinrich-eval`. Allowed: your own knowledge of the language, our own
      frequency list `/home/user/heinrich-data/en/frequency/forms.tsv` (grep for corpus evidence), the generator
      output (`dump`), the existing entries.
    - Write entries into the shards of the worktree `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/en/lexicon/` (this worktree is on branch
      `graded-lexicon-gaps`; never switch branches, **do not commit** — the orchestrator commits).
      Open compounds with a space (`ice cream`, `guinea pig`) get no entry: skip them with reason `open compound`. Multi-word expressions likewise.
    - First check that a word is really missing (`grep -rn "^<lemma> " /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/en/lexicon/`); the work list may
      contain words that exist under another part of speech, or forms of an existing lemma. Then: fix the
      existing entry (missing part of speech or sense), add a new entry, or skip with a reason.
    - Use `note=graded` on every new entry (plus any other note you need). Homograph senses: add `sense=` ids
      only where two entries with the same lemma and part of speech exist; if you add a sense to an existing
      entry, list it in your summary (vocabulary and rule files may refer to it).
    - Self-check per AUTHORING.md §5 with the tool `/home/user/Heinrich/target/release/heinrich-lexicon` (`/home/user/Heinrich/target/release/heinrich-lexicon dump /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/en/lexicon <Lemma>` with `--lang en` where the tool needs it,
      `/home/user/Heinrich/target/release/heinrich-lexicon validate /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-lexicon-gaps/en/lexicon` must report zero errors; check `/home/user/Heinrich/target/release/heinrich-lexicon --help` for the exact syntax).
    - Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en/result.tsv` with one row per work-list row: `lemma pos action(added|fixed|exists|skipped) detail`
      (detail: the entry's lemma/pos/sense to use in the vocabulary layer, or the reason for skipping), and
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en/decisions.md` (your approach, uncertain entries with conf < 100, skipped words and why).
    
    Final answer: counts per action, the list of senses added to existing entries, validate result.

## Decisions log (written by the author)

# lex-en decisions (graded work list, 107 rows)

## Approach
- Checked every lemma with `grep -rnE "^<lemma>\s"` in the worktree lexicon, plus the base lemmas
  (verbs behind participles, singulars behind plurals). Sources: own knowledge, `en/frequency/forms.tsv`
  counts, generator `dump`. No third-party lexica, no web.
- All 77 new entries carry `note=graded`. No existing entry was changed; **no `sense=` ids were added**
  (every new entry is a new lemma or a new part of speech for an existing lemma).
- Inserted into the shards in sorted order; `validate`: 0 errors, 1 pre-existing warning (X-ray verb).

## Notable choices
- Participial adjectives (pleased, shocked, convinced, …) are adj entries with `cmp=more` where they are
  gradable; non-gradable ones (married, divorced, disabled, haunted, paid, born, freezing, boiling,
  following, latest, reported, Aboriginal, part-time, full-time) have no `cmp`.
- `later adv`, `latest adj`, `further adv`: lexicalised lemmas although the generator already produces the
  forms as comparative/superlative of late / far (notes say so).
- `yet adv`, `inside adv`, `outside adv` put in `adv/` (type=time/place), not in the hand-curated
  `closed/adverbs.lex`; the orchestrator may want to move `yet` there (grammar-relevant with the perfect).
- Gerund nouns (bullying, smoking, streaming, training, surfing, warming) and hide-and-seek, outback:
  `pl=-` (uncountable).
- `glasses`, `customs`, `cornflakes`: `pl_only` (glasses/customs are also generated as plurals of
  glass/custom). `media`: own lemma `pl=-` (collective "the media"), also plural of medium.
- `flashlight`: `region=US` (British torch).
- Hyphenated adjectives (good-looking, open-minded, part-time, full-time, well-paid, eco-friendly) and
  nouns (double-decker, hide-and-seek): entries justified as lexicalised / part not a word (eco, decker).
- `Miss propn` added beside the existing lowercase `miss noun` (title); `Mr/Mrs/Ms` already exist as
  `Mr.`/`Mrs.`/`Ms.` propn abbr, which cover the period-less spellings.

## Uncertain entries (conf < 100)
- `cornflakes noun pl_only conf=90` – a singular *cornflake* exists but is rare.
- `media noun pl=- conf=90` – collective with singular or plural agreement; modelled as uncountable.

## Generator gap (reported)
- `good-looking` (better-looking, best-looking) and `well-paid` (better-paid, best-paid): comparison on
  the first part cannot be written, `sup=` must end in `-st`. Entries have no `cmp`; note documents it.

## Skipped (24)
- Open compounds (parts exist): ice cream, living room, pencil case, exercise book, guinea pig, teddy bear,
  board game, computer game, skipping rope, hot dog, swimming pool, Christmas tree, Father Christmas,
  Easter bunny, New Year, Mother's Day, Valentine's Day, Bonfire Night, Buckingham Palace, Tower Bridge,
  Big Ben (Ben is a first name: no entry).
- Multi-word expressions: thank you (thanks intj added), a lot.
- `according`: closed class – part of the multiword preposition *according to*; reported for the
  closed-class curator instead of an adj entry (the form is generated by `accord verb`).

## Exists (6)
statistics (statistic noun), lyrics (lyric noun), bagpipes (bagpipe noun, added in this run),
Mr/Mrs/Ms (Mr./Mrs./Ms. propn abbr).

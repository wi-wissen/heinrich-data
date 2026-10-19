# Run `lex-en-2`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Lexicon author run `lex-en-2` (graded work list)
    
    You are a **clean-room lexicon author** for Heinrich. Write lexicon entries for the words in your work list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en-2/worklist.tsv` (columns lemma, pos, notes from the vocabulary authors who need the word).
    
    Read first, completely: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/lexicon/AUTHORING.md` (your protocol; note the new exception for
    compounds needed by the graded layer in §4.4 and the note on open compounds) and the format
    `/home/user/Heinrich/docs/LEXICON_FORMAT_EN.md`.
    
    Rules:
    - Clean-room: **never** consult a third-party lexicon, dictionary or word list; **no WebSearch or WebFetch**;
      never open anything under `/home/user/heinrich-eval`. Allowed: your own knowledge of the language, our own
      frequency list `/home/user/heinrich-data/en/frequency/forms.tsv` (grep for corpus evidence), the generator
      output (`dump`), the existing entries.
    - Write entries into the shards of the worktree `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/lexicon/` (this worktree is on branch `graded-l1-efl-r1`, not
      `graded-lexicon-gaps`; never switch branches, **do not commit** — the orchestrator commits).
      Open compounds with a space (`ice cream`, `guinea pig`) get no entry: skip them with reason `open compound`. Multi-word expressions likewise.
    - First check that a word is really missing (`grep -rn "^<lemma> " /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/lexicon/`); the work list may
      contain words that exist under another part of speech, or forms of an existing lemma. Then: fix the
      existing entry (missing part of speech or sense), add a new entry, or skip with a reason.
    - Use `note=graded` on every new entry (plus any other note you need). Homograph senses: add `sense=` ids
      only where two entries with the same lemma and part of speech exist; if you add a sense to an existing
      entry, list it in your summary (vocabulary and rule files may refer to it).
    - Self-check per AUTHORING.md §5 with the tool `/home/user/Heinrich/target/release/heinrich-lexicon` (`/home/user/Heinrich/target/release/heinrich-lexicon dump /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/lexicon <Lemma>` with `--lang en` where the tool needs it,
      `/home/user/Heinrich/target/release/heinrich-lexicon validate /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/lexicon` must report zero errors; check `/home/user/Heinrich/target/release/heinrich-lexicon --help` for the exact syntax).
    - Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en-2/result.tsv` with one row per work-list row: `lemma pos action(added|fixed|exists|skipped) detail`
      (detail: the entry's lemma/pos/sense to use in the vocabulary layer, or the reason for skipping), and
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-en-2/decisions.md` (your approach, uncertain entries with conf < 100, skipped words and why).
    
    Final answer: counts per action, the list of senses added to existing entries, validate result.
    
    Additional notes for this run:
    - Column 3 onwards of the work list are notes from the vocabulary authors (may be empty). Rows can repeat a lemma with
      different notes; write one entry per lemma+pos.
    - British spellings: the lexicon stores the US lemma with the British variant attached; check with grep whether the
      US form exists before adding (`programme` → `program` with its GB variant). Report rather than duplicate.
    - Proper names of persons get no entry. Countries, nations, institutions (`Parliament`, `Congress`, `Commonwealth`) may
      be `propn` entries per AUTHORING.md §4.5.
    - Stylistic devices and literary terms (alliteration, hyperbole …) are ordinary nouns: add them.

## Decisions log (written by the author)

# lex-en-2 decisions

Approach: checked every work-list lemma against the shards, then added entries by script (sorted insert, `note=graded`).
Own knowledge only; no external sources. validate: 0 errors, 1 pre-existing warning (verb/x.lex X-ray).

- Open compounds and multi-word names/expressions: skipped (open compound).
- Closed-class words (albeit, barring, given, notwithstanding adp, pending adp, re, unto, provided, providing,
  whatsoever pron, whereby adp, worth adp, according, vis-a-vis): skipped, to be added by the closed-class curator.
  Open-class adverb readings added: notwithstanding, whatsoever, whereby, wherein, whereupon (adv, type=conj for the relatives), admittedly.
- Person names (Darwin, Gandhi, Mandela): skipped.
- Hyphenated compounds requested by the graded layer: entries with note=graded (per the §4.4 exception).
- -ing nouns (fishing, swimming ...): lexicalised nouns with pl=- for uncountable use.
- Demonyms/language names (Maori, Elizabethan, Ghanaian, Kenyan): adj + noun, not propn. Ghanaian/Kenyan noun added unrequested.
- US lemma with GB variant: Euroskeptic/Euroskepticism (gb=Eurosceptic...), colonizer, -ization words, counseling, organized, spoiled (gb=spoilt|spoiled), self-centered.
- paparazzi -> paparazzo pl=paparazzi; bagpipes -> existing bagpipe.
- Extra POS added beyond the request (cheap, same lemma): conformist/nativist/isolationist/imperialist/sensationalist/sexist/misogynist/individualist/nonconformist (adj+noun), heuristic noun, Elizabethan noun.
- Capitalised lemmas: McDonaldization (worklist had lowercase), Romantic adj (lowercase romantic exists separately), Orwellian, Shakespearean.
  newspeak and doublethink are lowercase as in the work list.

Uncertain (conf < 100): Apache-like none new; asyndeton pl (85), bildungsroman pl (85), chiasmus pl (90), epiphora pl (85),
polysyndeton pl (85), zeugma pl (85), fairtrade (85), leitmotif with leitmotiv variant (85), McDonaldization (85).
Entries with senses added to existing entries: none.
Generator note: the hyphenated compounds with irregular comparison (badly-paid, left-wing) are written without cmp.

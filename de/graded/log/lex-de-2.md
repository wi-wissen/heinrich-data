# Run `lex-de-2`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Lexicon author run `lex-de-2` (graded work list)
    
    You are a **clean-room lexicon author** for Heinrich. Write lexicon entries for the words in your work list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-2/worklist.tsv` (columns lemma, pos, notes from the vocabulary authors who need the word).
    
    Read first, completely: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/lexicon/AUTHORING.md` (your protocol; note the new exception for
    compounds needed by the graded layer in §4.4) and the format
    `/home/user/Heinrich/docs/LEXICON_FORMAT.md`.
    
    Rules:
    - Clean-room: **never** consult a third-party lexicon, dictionary or word list; **no WebSearch or WebFetch**;
      never open anything under `/home/user/heinrich-eval`. Allowed: your own knowledge of the language, our own
      frequency list `/home/user/heinrich-data/de/frequency/forms.tsv` (grep for corpus evidence), the generator
      output (`dump`), the existing entries.
    - Write entries into the shards of the worktree `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/lexicon/` (this worktree is on branch `graded-l1-efl-r1`, not
      `graded-lexicon-gaps`; never switch branches, **do not commit** — the orchestrator commits).
      Your work list covers all letters.
    - First check that a word is really missing (`grep -rn "^<lemma> " /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/lexicon/`); the work list may
      contain words that exist under another part of speech, or forms of an existing lemma. Then: fix the
      existing entry (missing part of speech or sense), add a new entry, or skip with a reason.
    - Use `note=graded` on every new entry (plus any other note you need). Homograph senses: add `sense=` ids
      only where two entries with the same lemma and part of speech exist; if you add a sense to an existing
      entry, list it in your summary (vocabulary and rule files may refer to it).
    - Self-check per AUTHORING.md §5 with the tool `/home/user/Heinrich/target/release/heinrich-lexicon` (`/home/user/Heinrich/target/release/heinrich-lexicon dump /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/lexicon <Lemma>`,
      `/home/user/Heinrich/target/release/heinrich-lexicon validate /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/lexicon` must report zero errors; check `/home/user/Heinrich/target/release/heinrich-lexicon --help` for the exact syntax).
    - Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-2/result.tsv` with one row per work-list row: `lemma pos action(added|fixed|exists|skipped) detail`
      (detail: the entry's lemma/pos/sense to use in the vocabulary layer, or the reason for skipping), and
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/lex-de-2/decisions.md` (your approach, uncertain entries with conf < 100, skipped words and why).
    
    Final answer: counts per action, the list of senses added to existing entries, validate result.
    
    Additional notes for this run:
    - Rows can repeat a lemma with different notes; write one entry per lemma+pos.
    - Participles used as adjectives (`verboten`, `geöffnet`, `verletzt`): the generator already produces participle forms
      of the verb; add an `adj` entry only if the adjective has its own meaning or comparison (AUTHORING.md §4.2), else
      record `exists` with the verb as detail.
    - Do **not** add separable verbs whose particle is an adjective (`kaputtgehen`, `kleinschreiben`, `großschreiben`,
      `wohlfühlen`): skip with reason `adjective particle (rule conflict)`.
    - `Tor` as football "goal": if you add a sense, give the existing entry a `sense=` as well and list both in your summary.
    - Nominalized infinitives (`Schwimmen`) get no entry (rules derive them).

## Decisions log (written by the author)

# lex-de-2 decisions

Approach: existence check per lemma via grep; compounds named by the graded layer added as entries (AUTHORING 4.4 exception) with gender/plural from the head;
participle adjectives left to the verb (action `exists`), except gradable ones where `pp_cmp` was added to the verb.

Senses added to existing entries: Gericht sense=court (new sense=dish), Verband sense=association (new sense=bandage). Tor: new sense=goal next to existing gate/fool.
Existing verbs got `pp_cmp`: beleben, empören, entsetzen, gefährden, verblüffen, verschmutzen, verwöhnen, spannen.
New adj `verlegen` (embarrassed) beside the verb verlegen (different POS, no sense needed).

Uncertain (conf < 100):
- seilspringen (70): perfect forms seilgesprungen / auxiliary uncertain; modelled as separable with particle `seil`.
- staubsaugen (70): modelled as inseparable weak verb (gestaubsaugt); separable use not modelled.
- Language names Arabisch, Persisch, Polnisch, Ukrainisch (80), same as Englisch/Deutsch.

Skipped: nominalized infinitives (Aufwärmen, Fasten, Kraulen, Reiten, Schwimmen, Tanzen); multiword Erste-Hilfe and Sankt Martin;
adjective-particle verbs (kaputtgehen, kleinschreiben, großschreiben, wohlfühlen).
Exists: Ringe, Kräuter, Medien, Klanghölzer (Klangholz), Einkaufsliste, nächst (via nah sup), zu (part degree), participles of existing verbs.
Mass/uncountable nouns have pl=- with note; Familienstand pl=- (plural practically unused).

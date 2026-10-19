# Run `en-efl-7-8`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-efl-7-8`
    
    Language: English (lexicon language `en`). Track: `efl` (English as a foreign language in German schools; English starts in grade 3).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - Both `grade=` and `cefr=` are required. Use the band ↔ CEFR guide in the README (3-4 → A1; 5-6 → A1 or A2; 7-8 → A2, some B1).
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-7-8/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Band **7-8**, levels **A2** (some **B1**). Output: one file per top-level topic group, named after the first topic's top-level id.
    Other authors cover 3-4 and 5-6 in parallel: list only words typically **introduced in grades 7-8**. Cover all topics the README names for 7-8 (friendship and feelings, media and technology, jobs and future plans, health, environment, adventures and stories, life in other English-speaking places, opinions and reasons), including abstract nouns, verbs and adjectives, linking words and adverbs typical of this stage. Target size: 900–1200 lexemes.
    
    ## Common rules for every graded-vocabulary author (clean-room)
    
    You are an author of Heinrich's graded vocabulary layer: for words of our own lexicon you record in which
    school grade band pupils typically learn them, their CEFR level where required, their topics and whether
    pupils should produce or only recognise them. You work **only from your own knowledge** of the language,
    of schools in Germany and of the topic areas of the curricula.
    
    Strict rules (violating any of them makes the data unusable):
    1. **Never consult a published word list** of any kind: no basic-vocabulary lists of German states, no
       exam, course-book or learner-dictionary word lists, no CEFR word profiles, no children's-book frequency
       lists, no Wiktionary, no dictionaries. **Do not use WebSearch or WebFetch at all.** Do not open any file
       outside the paths named below. Never open anything under `/home/user/heinrich-eval`.
    2. Your only inputs: the brief `README.md` and `topics.tsv` of your language (paths below), the lemma index
       of our own lexicon, our own lexicon files (`/home/user/heinrich-data/<lang>/lexicon/`) and our own
       frequency list (`/home/user/heinrich-data/<lang>/frequency/forms.tsv`, columns form, total, ...; you may
       grep it to check how common a form is). Read the README completely before you start.
    3. Use only lemmas of the lexicon (exact spelling and part of speech as in the lemma index). Use
       `lemma:sense` only where the index lists that `sense`. If a word you want is missing, or a homograph
       needs a sense the lexicon does not have yet, **do not invent it**: put it in your work list
       `missing.tsv` (columns `lemma pos note`, note = why/what sense) — lexicon authors will add it later.
    4. `src=ai` on every line. Never record where a word "appears" (no list names, no references).
    5. Write your decisions log `decisions.md` (English): how you approached the task, how you chose bands
       and levels, borderline cases, what you left out and why. This log is part of the clean-room evidence.
    
    Line format (one line per lexeme, columns separated by a tab or spaces):
    
    ```
    # lemma[:sense]  pos   fields
    Hund             noun  grade=1-2 topic=animals role=prod conf=95 src=ai
    ```
    
    Fields: `grade=` one of `1-2 3-4 5-6 7-8 9-10 11-13` (the band in which the word is typically
    **introduced**); `cefr=` `A1`..`C2`; `topic=` one or more ids of `topics.tsv` separated by `|` (use
    the most specific fitting id; several topics where the word clearly belongs to several); `role=prod`
    (pupils should write/use it themselves at that band) or `role=rec` (understand it); `conf=` 0–100, your
    own certainty about the band/level (be honest: borderline words get 60–75); `src=ai`.
    Each lemma+pos(+sense) at most once per output file. Group lines by topic with `#` comment headers,
    sorted alphabetically within a group.
    
    Method:
    - Go topic by topic through the catalogue entries relevant to your assignment. For each topic, think of
      the situations described in the README for your band and list the words pupils need there, from your
      own knowledge. Then check each candidate against the lemma index.
    - Explicitly include **function words** (articles, pronouns, prepositions, conjunctions, particles,
      question words, auxiliaries/modals, frequent adverbs) and **basic verbs and adjectives** — they are
      easily forgotten. Function words get topic `function.*`.
    - Do not stop at the obvious nouns: verbs and adjectives for the situations, too.
    - Band means *introduced*: a word pupils already know from an earlier band does not belong to a later
      band's list.
    - Self-check: run
      `python3 -I /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/tools/check_graded.py <lemma index> <topics.tsv> <track> <your files...> --missing <your dir>/missing_check.tsv`
      until it reports 0 errors (move words that are not in the lexicon to `missing.tsv` instead of keeping
      them). Then count your lines per band and topic and report the counts.
    
    Final answer to the orchestrator: counts per file/band/topic, the size of `missing.tsv`, and a
    5–10 line summary of your decisions. Do not commit or push anything; write only into your output
    directory.

## Follow-up message 1 (verbatim)

    Orchestrator: the lemma index was incomplete — adverbs the lexicon derives via `adv=` on adjectives (actually, probably, carefully …) are own `adv` lexemes and are now listed in the regenerated index (same path). Please re-check your `missing.tsv` against the new index: every entry that now exists, add as a normal line (band 7-8, your own judgement), remove it from `missing.tsv`, re-run the checker to 0 errors, append a short note to `decisions.md`, and report the new counts. Also note: might/could/would/should are forms (past) of the modal lemmas may/can/will/shall in our lexicon, so they are covered by those lemmas — drop them from `missing.tsv`. Additionally please split your output into one file per top-level topic id of each line's first topic (e.g. `health.tsv`, `function.tsv`, `anglophone.tsv`) instead of the three block files. Same clean-room rules as before.

## Follow-up message 2 (verbatim; the agent received a one-line pointer to this text)

    Orchestrator follow-up (logged as part of your run): lexicon authors have now written entries for most
    words of your `missing.tsv` (clean-room, following the lexicon protocol). The lemma index at the same path
    is regenerated. `now_available.tsv` in your output directory lists the rows of your `missing.tsv` whose
    lemma+pos now exist. For each of them, decide band/level/topic/role/conf from your own judgement exactly
    as in your original run and add a normal line (`src=ai`) to the right output file; check senses in the
    index (e.g. `Leiter:conductor` now exists). Remove the added rows from `missing.tsv` (keep the rest).
    Note: `großschreiben`, `kleinschreiben` and `kaputtgehen` were not added (a separable particle reading of
    the adjective interferes with a grammar rule); use other words if you need them. Re-run the checker to 0
    errors, append a "Revision" note to `decisions.md`, and report new counts. Same clean-room rules as before.

## Reviewer round 1 feedback (verbatim; aggregate numbers and patterns only)

Message:

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev1-en.md (you: band 7-8; output directory .../graded/runs/en-efl-7-8/).
    
    Second message (verbatim): Orchestrator addition to revision round 1: the 5-6 author moved some words out of 5-6 and lists them under "for 7-8" in the "Revision round 1" section of /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-5-6/decisions.md (hippo, kangaroo, panda, turtle, unicorn, yo-yo, eagle, budgie, notice, wonder, belong, appear, cover, except, nearby, typical). Read only that section. For each word you judge to be introduced in 7-8, add a line with your own level/topic/role/conf (`src=ai|rev`); words you judge not to be school vocabulary at all, list in decisions.md. Re-run the checker and report briefly.

Feedback file referred to:

    # Revision round 1 (English EFL), feedback from the internal reviewer — patterns only
    
    The reviewer compared the merged layer (bands 3-4, 5-6, 7-8; A1–B1) statistically with one CEFR-levelled reference
    outside the repositories. You receive only aggregate numbers and patterns in the reviewer's own words; you never receive
    reference entries, and you must not try to guess them. Revise **whole topics from your own knowledge**.
    This is round 1 of at most 2 against this reference.
    
    ## Numbers
    | reference level | covered | exact (covered) | ±1 (covered) | ours later | ours earlier | mean shift (ours − ref) |
    |---|---:|---:|---:|---:|---:|---:|
    | A1 | 84.9 % | 80.1 % | 99.1 % | 181 | 0 | +0.21 |
    | A2 | **59.4 %** | 66.8 % | 100 % | 96 | 154 | −0.08 |
    | B1 | 28.9 % (layer ends at grade 8; partly expected) | 28.0 % | 89.5 % | 0 | 467 | −0.82 |
    Confusion (rows reference, columns ours): A1→A1 730 / A2 173 / B1 8; A2→A1 154 / A2 504 / B1 96; B1→A1 68 / A2 399 / B1 182.
    Function words: 90.9 % of the reference's A1 function words are covered, only 74.2 % of them in band 3-4.
    Topics with the largest shift (levels, negative = ours earlier): **animals −0.95** (only 68 % within ±1), **toys −0.81**
    (76 %), clothes −0.56, food −0.54, health −0.53, academic −0.53, anglophone −0.51, fantasy −0.51, friends −0.49.
    Well calibrated: time, function, numbers, family, communication, thinking, music_arts, town.
    
    ## Patterns (reviewer's own words)
    1. A1 is good, A2 thin, B1 structurally thin. The layer covers 85 % of the reference's A1 but only 59 % of its A2:
       grades 5–6 lack the most.
    2. Two opposite shifts. About every fifth reference-A1 word is only on A2 with us (mostly band 5-6), while 72 % of
       reference-B1 words are already on A2 or A1 with us. The layer compresses the scale towards the middle: basic
       vocabulary rather too late, more demanding vocabulary rather too early.
    3. Animals and toys clearly too early: typically words for rarer or more exotic animals and for more specific toys that we
       put on A1 like core vocabulary. Similar but weaker: clothes, food, health, fantasy, friendship (about half a level early).
    4. Well calibrated: time, function words, numbers, family, communication, thinking, music/arts.
    5. Function words: 9 % of the reference's A1 function words are missing, and another sixth are only after band 3-4.
    6. Cultural and country words overlap little with the reference — a property of the reference, not an error of the layer.
    7. Lexicon: about 10 % of the reference could not be mapped to a lemma of our English lexicon; part of it are gaps in the
       lexicon itself (report candidates in `missing.tsv`).
    
    ## What to do (per band author)
    - **3-4 (A1):** add the core A1 vocabulary you left for 5-6 (basic vocabulary rather too late); include the remaining
      frequent function words; move rarer animals and specific toys/clothes/food words out of A1 (to 5-6/A2 or 7-8 by your
      judgement, i.e. remove them from your list and note them for that band in `decisions.md`).
    - **5-6 (A1/A2):** expand A2 substantially across all topics (the biggest gap), plus the basic words that are A1 but
      typically met first in grades 5-6; move overly specific animal/toy/clothes/food words later where appropriate.
    - **7-8 (A2/B1):** re-check level assignments: more demanding, abstract or formal words belong on B1 rather than A2;
      add B1 vocabulary for the 7-8 themes.
    For every line you add or change, set `src=ai|rev` (keep `freq` if present). Re-run the checker to 0 errors, append a
    "Revision round 1" section to `decisions.md`, report counts (added, level changed, removed/moved). Same clean-room rules
    (no web, no word lists, never the held-out repository). Missing lemmas to `missing.tsv`.

## Decisions log (written by the author)

# Decisions log – author run `en-efl-7-8`

## Inputs and method
- Inputs used: the brief (`en/graded/README.md`), `topics.tsv`, the lemma index `en_lemmas.tsv`, and the
  build/check script. No word list, dictionary, course book, CEFR profile or web source was consulted;
  no WebSearch/WebFetch; nothing under `heinrich-eval` was opened. The frequency list was not needed.
- I went through the eight 7-8 themes of the brief (friendship and feelings; media and technology; jobs
  and future plans; health and the body; everyday environment; adventures and stories; life in the USA,
  Scotland, Ireland, Australia; opinions and reasons) plus the grammar of this stage (present perfect,
  passive, conditional sentences, relative clauses, gerund/infinitive, reported speech, adverbs of
  manner) and the linking words needed for short opinion texts. For each situation I brainstormed the
  nouns, verbs, adjectives and function words pupils need, then checked every candidate against the
  lemma index.
- Draft size was about 1,470 candidates. To respect "band = introduced", I then removed every word I
  had myself rated as probably already known from grades 3-6 (draft conf 55 or lower, e.g. basic verbs
  like *happen, move, describe*, everyday nouns like *hospital, laptop, newspaper*, common animals) and a
  further hand-picked set of words I judged too basic on second look (*borrow, shout, strange, desert,
  website, luggage, grammar, vocabulary* …). A few low-confidence words were kept because they are
  uncertain rather than early (*thus, upon, analyze, evaluate, monarchy, Aborigine, gender, freeway,
  crutch, faint, fancy, determine*). Result: 1,176 lexemes.

## Bands and levels
- All lines are `grade=7-8`. CEFR: A2 for core productive vocabulary of the stage; B1 for abstract or
  register-heavier words that pupils meet now but fully master later (*consequence, attitude, evidence,
  sustainable, despite, whereas, moreover*). Overall ~74 % A2, ~26 % B1.
- `role=rec` for B1 words pupils mainly need to understand in texts (*whereas, throughout, habitat,
  wilderness, prescription*), place names other than the main countries, and cultural realia
  (*loch, tartan, clan, outback, boomerang*). Everything else is `prod`.
- Confidence: 70–80 for words clearly tied to 7-8 themes (*apologize, environment, recycle, career,
  embarrassed, bully, although*); 60–65 for borderline words that could also sit in 5-6
  (*app-era tech words, sunscreen, apartment-type US words*) or 9-10 (*hire, shift, prejudice, racism*).

## Topics and files
- Files: one per top-level topic id of each line's first topic (`function.tsv`, `actions.tsv`,
  `health.tsv`, `anglophone.tsv`, …; see revision note below; the first pass used three block files).
- Where a word clearly serves two topics I gave both (`afford` thinking|shopping, `guilty` feelings|law,
  `foreign` travel|countries, `bin` home|environment, `junk` food|health).
- US vocabulary (*sidewalk, subway, fall, vacation, candy*) went to `anglophone.us` or the everyday
  topic with a US flavour; the lexicon spells lemmas the American way (*behavior, neighbor,
  apologize, theater*), so I used those spellings.
- Grammar terms of this stage (*passive, gerund, clause, participle, tense, infinitive*) go to
  `language`; reading/mediation skills (*skim, scan, summarize, mediation*) go to `academic`.

## Borderline cases
- Present-perfect signal words (*already, ever, since, recently, lately*): kept at 7-8 with conf 60–75,
  as the tense is consolidated here although some schools start it in grade 6.
- Reflexive pronouns: kept at 7-8 (conf 70), as they are usually taught explicitly at this stage.
- Jobs: only the "less childlike" jobs (*electrician, plumber, lawyer, engineer, receptionist*); the
  primary-school jobs (*doctor, teacher, farmer, vet*) were left out as earlier.
- Australian animals (*kangaroo, koala*) and common wild animals were dropped as known from 5-6.
- `lie:untruth` (verb) and `tear:drop` (noun) use the senses the index provides.

## Left out / missing
- Multiword expressions (*point of view, first aid, peer pressure, global warming, social media,
  part of*) are not lemmas in the index; their head words were included where meaningful, and some
  are noted in `missing.tsv`.
- 109 entries in `missing.tsv`: mostly -ly adverbs (*actually, probably, unfortunately, carefully* …),
  participial adjectives (*embarrassing, relieved, stressed, haunted, polluted, endangered*),
  hyphenated adjectives (*part-time, open-minded, eco-friendly*), grammar terms (*adverb, gerund,
  infinitive, preposition*), the modal *might*, and nouns like *media, customs, lyrics, training*.
- Three missing parts of speech were replaced by the index's own analysis instead of being listed:
  *dozen* and *twice* as `num`, *conditional* as `adj`, *junk* as `noun`.

## Revision 1 (after the lemma index was regenerated)
- The regenerated index lists the adverbs derived from adjectives as their own `adv` lexemes. I re-ran
  the build against it: the 43 -ly adverbs that had been in `missing.tsv` (*actually, probably,
  carefully, unfortunately, environmentally* …) are now regular lines, with the band, level and
  confidence I had already given them in the draft (all 7-8; mostly A2, B1 for *eventually, slightly,
  rarely, frequently, generally, similarly, incredibly, successfully, environmentally*).
- `might` was dropped from `missing.tsv`: in our lexicon might/could/would/should are past forms of the
  modal lemmas may/can/will/shall, so they are covered by those lemmas. (`may` and `shall` are in the
  list at 7-8; `can` and `will` are earlier-band words and were not added.)
- To stay inside the 900–1200 target after the additions, I removed 19 more borderline, low-value
  words (rated conf 60 in the draft): *lean, march, slide, glance, sometime, someday, forwards,
  underneath, toward* (kept *towards*), *whatever* (determiner), *creepy, amaze, plaster, sweat, coral,
  semester, username, login, refund*.
- Output is now split into one file per top-level topic id of each line's first topic (41 files).
- New totals: 1,200 lexemes (879 A2 / 321 B1; 979 prod / 221 rec); `missing.tsv` has 65 entries
  (participial and hyphenated adjectives, grammar terms, some nouns, and parts of speech the lexicon
  lacks). The checker reports 0 errors and 0 warnings.

## Revision 2 (after lexicon authors added most words from `missing.tsv`)
- All 61 rows of `now_available.tsv` now exist in the regenerated index. I added each as a normal line at
  grade 7-8, using the level, topic, role and confidence I had given it in my original draft. None of the
  61 lemmas has a sense split in the index, so no `lemma:sense` keys were needed. Examples: participial
  adjectives in `feelings` (*embarrassing, relieved, stressed, terrified*; A2/B1 prod), `health`
  (*exhausted, swollen, disabled, balanced*), `jobs` (*part-time, full-time, well-paid, training*),
  grammar terms in `language` (*adverb, gerund, infinitive, preposition, perfect* as a noun, *reported*),
  `anglophone` (*kilt, bagpipe, outback, Aboriginal*), `past` (noun) and `latest` in `time`, and `pardon`
  (intj) in `communication`.
- `missing.tsv` keeps 4 rows that are still not in the index: *according* (better as part of the
  multiword "according to"), *statistics*, *lyrics*, *bagpipes* (*bagpipe* is now listed).
- The total is now 1,261, slightly above the 900–1200 target. I kept it like this rather than cutting
  further, because the added words are core 7-8 vocabulary (feelings adjectives and grammar terms).
- The checker reports 0 errors and 0 warnings. Totals: 930 A2 / 331 B1; 1,034 prod / 227 rec.

## Revision round 1 (reviewer feedback: patterns only)
- The feedback for band 7-8 was to put more demanding, abstract or formal words on B1 instead of A2, and
  to add B1 vocabulary for the 7-8 themes. I re-read my whole A2 list topic by topic and judged each word
  from my own knowledge only. I did not try to guess any reference entries.
- **Level changes (73 lines, A2 → B1):** words that are abstract, formal or mostly met in texts rather
  than used by pupils of this age. Examples: nouns for abstract concepts (*emotion, courage, freedom,
  community, government, possibility, statement, effect, generation, protection, punishment*), formal
  verbs (*communicate, inform, arrange, contain, prove*), text-work terms (*definition, structure,
  source, research, questionnaire, mediation*), formal adjectives (*available, valuable, equal,
  responsible, generous, loyal, wise, attractive*), technical words (*data, device, electronic,
  gadget, clause, participle*) and place or position words (*region, location, position, surface*).
  Concrete, everyday or emotionally central words for the themes stayed on A2.
- **Added (137 lines, mostly B1, many `role=rec`):** B1 words for each 7-8 theme:
  - feelings: *anxiety, confidence, furious, awkward, cope, encourage*
  - friendship: *conflict, misunderstanding, loyalty, rumor, influence*
  - media: *access, content, platform, virtual, addictive, anonymous*
  - jobs: *employment, candidate, skilled, flexible, teamwork, deadline*
  - health: *prevent, condition, lifestyle, habit, heal*
  - environment: *global, atmosphere, extinction, threat, protest, campaign*
  - adventures and stories: *challenge, risky, mission, suspense, twist*
  - English-speaking places: *landmark, settlement, heritage, rural, urban, election, vote*
  - opinions and reasons: *agreement, debate, issue, benefit, drawback, nevertheless, consequently,
    aware*
  - general: *various, specific, effort, progress, achievement, require, involve*
- Removed or moved to another band: none. The reviewer named animals/toys/clothes/food as too early.
  These concern the lower bands; my 7-8 list has only a handful of such words, all on A2 at 7-8.
- All added or changed lines carry `src=ai|rev`. `missing.tsv` gained 3 candidates (*cyberbullying*,
  *qualified*, *experienced*), so it now has 7 entries.
- The size is now 1,398 lexemes (858 A2 / 540 B1; 1,088 prod / 310 rec). This is above the original
  900–1200 target, because the review asked specifically for more B1 vocabulary at this band. The
  checker reports 0 errors and 0 warnings.

### Revision round 1, addition: words handed over by the 5-6 author
- I read only the "Revision round 1" section of the 5-6 decisions log, as instructed.
- **Added (7 lines, `src=ai|rev`):** each with my own level, topic, role and confidence.
  - At A2 prod: *hippo, panda, turtle, eagle* (animals), *kangaroo* (anglophone.commonwealth|animals)
    and *cover* (verb, actions.handling).
  - *budgie* at A2 rec, conf 55, as a minor pet word.
  - My first draft already had *eagle, kangaroo* and *cover*. I had removed them only because I thought
    they were learned earlier. Now that the earlier bands have dropped them, 7-8 is the right band.
- **Already on my list (7-8, A2), left unchanged:** *notice, wonder, belong, appear, except, nearby,
  typical*.
- **Judged not to be school vocabulary (not added):** *unicorn* and *yo-yo*. Both are niche words that
  are not taught on purpose in English lessons, so pupils meet them by chance.
- New size: 1,405 lexemes (865 A2 / 540 B1; 311 rec). The checker reports 0 errors and 0 warnings.

# Run `en-efl-3-4`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-efl-3-4`
    
    Language: English (lexicon language `en`). Track: `efl` (English as a foreign language in German schools; English starts in grade 3).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - Both `grade=` and `cefr=` are required. Use the band ↔ CEFR guide in the README (3-4 → A1; 5-6 → A1 or A2; 7-8 → A2, some B1).
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-3-4/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Band **3-4**, level **A1** (primary English). Output: one file per top-level topic group, named after the first topic's top-level id (e.g. `home.tsv`, `function.tsv`, `animals.tsv`).
    Cover all topics the README names for 3-4, plus **all of the most frequent function words** of English (articles, personal/possessive pronouns, the common prepositions, and/but/or/because, question words, be/have/do/can, frequent adverbs) and the basic verbs and adjectives. Remember primary English is mostly oral: many words are `role=rec`; words pupils say and write themselves are `role=prod`. Target size: 600–800 lexemes.
    
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

    Orchestrator: the lemma index was incomplete — adverbs the lexicon derives via `adv=` on adjectives (really, usually, well …) are own `adv` lexemes and are now listed in the regenerated index (same path). Please re-check your `missing.tsv` against the new index: every entry that now exists, add as a normal line to the right topic file (same rules as before: band 3-4, A1, your own judgement), remove it from `missing.tsv`, re-run the checker to 0 errors, append a short note to `decisions.md`, and report the new counts. Same clean-room rules as before.

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

## Decisions log (written by the author)

# Decisions log – author run en-efl-3-4 (band 3-4, A1)

## Approach
Worked only from my own knowledge of primary English in German schools (grades 3–4, mostly oral,
picture-, song- and rhyme-based). Inputs used: the en graded README, topics.tsv, the lemma index of our
lexicon, and a few look-ups in our own lexicon files (to see that British spellings are stored as `gb=`
variants of US lemmas). No word list, dictionary or web resource was consulted.

I went through the README's 3-4 situations (greetings and classroom routines, me/family/friends,
numbers/colours/shapes, body and clothes, animals and pets, food and likes/dislikes, home and furniture,
toys and games, school things, calendar/weather/time, festivals, simple actions and sports, stories and
songs), brainstormed the words a child needs in each, then added the function words (articles and
determiners, personal and possessive pronouns/determiners, common prepositions, and/but/or/because,
question words, be/have/do/can and a few receptive modals, frequent adverbs) and basic verbs and
adjectives. Each candidate was checked against the lemma index; absent ones went to missing.tsv.

## Bands, levels and roles
All entries: grade=3-4, cefr=A1. role=prod for words children say or copy themselves in typical primary
tasks (colours, numbers to 20, family, body, pets, food, clothes, school things, greetings, days, months,
seasons, weather words, core verbs like go, like, have got, can). role=rec for words they meet in
teacher talk, stories, songs and instructions but are not expected to use (e.g. repeat, match, tick,
always/never, because, will, must, tortoise, wizard). conf 90+ for undisputed core words, 60–75 for
words that are equally plausibly introduced in grade 5 (e.g. second/third, afraid, excited, homework,
sweater, coffee).

## Spelling
The lexicon stores US lemmas with British variants (`color gb=colour`, `gray`, `favorite`, `pajamas`).
I used those lemmas although German schools teach British spelling; the variant is attached to the lemma.
British-only words that exist as lemmas (rubber, jumper, biscuit, mum, maths, ladybird, crisp) are
included as prod; US-only equivalents were dropped (eraser, candy, truck) or kept only as rec (cookie, sweater).

## Borderline cases
- Ordinals: first prod; second/third rec only; fourth+ left for 5-6 (dates are a 5-6 topic).
- Tens above 50 and hundred are rec (counting games, not written).
- next adj is listed under prepositions (for "next to"); object pronouns (me, him, us, them) and
  these/those are not separate lemmas in the index, so they are covered by I/he/we/they/this/that.
- story used with sense `tale`; that pron with sense `dem`.
- Several polysemous nouns get two topics (chicken, fish: animals|food; egg, cake: food|celebrations).
- Removed after a first draft as more typical of 5-6: may, shall, if, celebrate, hobby, age, poem,
  hockey, volleyball, budgie, marble, block, cocoa, muffin, candy, mistake, correct, check, sour, lazy,
  lip, eraser, everyone, half, key, carpet, cage, wing, fog, truck, workbook. This also kept the run
  inside the 600–800 target.
- Shopping, town, jobs and transport are deliberately thin: they are 5-6 topics; only words that come up
  through toys, picture books and "what is it?" games (bus, train, plane, doctor, farmer, shop) are here.

## Left out / missing
Derived adverbs without their own lemma (really, usually, well), colour adjectives gold/silver, and
many compound nouns central to primary English (ice cream, living room, pencil case, guinea pig, teddy
bear, Christmas tree …), plus titles Mr/Mrs/Miss and thanks/thank you, are listed in missing.tsv for the
lexicon authors.

## Revision after the regenerated lemma index
The index now lists adverbs derived via `adv=` as own `adv` lexemes. Re-checked missing.tsv: really
(prod, conf 75), usually (rec, conf 65) and well (prod, conf 75; "very well", "sing well") now exist and
were added to function.tsv under function.adverb and removed from missing.tsv. The index has two `well adv`
rows without a sense (from good and from well); they are one lemma+pos, so one line. gold/silver are still
nouns only, and the compounds, titles and thanks/thank you are still absent, so they stay in missing.tsv.

## Revision (lexicon follow-up)
Lexicon authors added six of my missing words. Added from my own judgement, all grade=3-4 cefr=A1:
thanks intj (communication, prod, 92); Miss propn (communication|school, rec, 70 – children address
teachers this way in stories and British school scenes, but in German classrooms Mr/Mrs dominate);
cornflakes noun (food, prod, 80); hide-and-seek noun (toys|free_time, rec, 75); gold and silver adj
(qualities.colour, rec, 65 – stars, crowns, treasure in stories). Removed them from missing.tsv; the
remaining compounds, Mr/Mrs/Ms, thank you and "a lot" are still absent and stay listed.

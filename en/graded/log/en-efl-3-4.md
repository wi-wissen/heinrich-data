# Run `en-efl-3-4`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

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

## Follow-up message (verbatim)

    Orchestrator: the lemma index was incomplete — adverbs the lexicon derives via `adv=` on adjectives (really, usually, well …) are own `adv` lexemes and are now listed in the regenerated index (same path). Please re-check your `missing.tsv` against the new index: every entry that now exists, add as a normal line to the right topic file (same rules as before: band 3-4, A1, your own judgement), remove it from `missing.tsv`, re-run the checker to 0 errors, append a short note to `decisions.md`, and report the new counts. Same clean-room rules as before.

## Follow-up: lexicon entries added (verbatim; one-line pointer to this text)

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

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev1-en.md (you: band 3-4; output directory .../graded/runs/en-efl-3-4/).

Feedback file:

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

## Reviewer round 2 feedback, final (verbatim; aggregate numbers and patterns only)

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev2-en.md (you: band 3-4; output directory .../graded/runs/en-efl-3-4/). The 5-6 author works in parallel and lists words "for 3-4"; the orchestrator will pass them to you afterwards.

Feedback file:

    # Revision round 2 (final) — English EFL, patterns from the second statistical measurement
    
    This is the **last** revision against this reference; there will be no further measurement against it. Same rules as
    round 1: only aggregate numbers and patterns; revise from your own knowledge; never guess reference entries.
    
    Numbers after round 1 (before → after): coverage A1 84.9 → 88.6 %, A2 59.4 → 66.4 %, B1 28.9 → 34.6 %. Reference-A1
    words that are A2 with us: 173 → 211 (exact A1 agreement 80.1 → 76.8 %). B1: exact 28 → 36 %, shift −0.82 → −0.71.
    Overall Spearman 0.61 → 0.63. A1 function words in band 3-4: 74.2 → 81.1 %. Nouns 47.3 → 55.1 %, verbs 51.2 → 54.7 %
    (verb shift unchanged −0.26). Better: animals −0.95 → −0.70, toys −0.81 → −0.45, clothes, health, food. Worse:
    celebrations (±1 82.4 → 75.0 %), weather (−0.35 → −0.42), thinking (+0.09 → +0.17).
    
    Patterns (reviewer's own words):
    1. Keep extending A2 for grades 5–6, above all verbs and adverbs.
    2. Re-check this round's moves from A1 to A2: what is needed in the first two years of English belongs on A1 / 3-4.
    3. The B1 assignment works, but 64 % of the shared B1 words are still on A2 or A1 with us.
    4. Animals remain the topic with the largest shift.
    5. Newly added words in celebrations and weather are rather placed too early.
    6. Bring the remaining A1 function words from band 5-6 to 3-4.
    
    What to do: 3-4 author — patterns 2, 4, 6 (and 5 for your band). 5-6 author — patterns 1, 2 (words you moved from A1
    to A2: re-judge; words needed in the first two years: list under "for 3-4"), 5, 6 (list A1 function words that
    belong to 3-4 under "for 3-4" and remove them). 7-8 author — pattern 3 (A2 → B1 where more demanding), 5.
    `src=ai|rev`, checker to 0 errors, append "Revision round 2" to decisions.md, report counts.

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

## Revision round 1
Feedback (patterns only): band 3-4 placed rarer animals and specific toy/clothes/food/fantasy words too
early, left some core A1 words and frequent function words for later. Revised whole topics from my own
judgement; no reference entries were seen or guessed. All 3-4 lines stay A1; new lines carry `src=ai|rev`.

**Removed from 3-4 (73), suggested for the 5-6 author (A2) unless noted:**
- animals: crocodile, donkey, giraffe, goat, hen, owl, penguin, zebra, fox, bat, dinosaur, tail, feed
  (5-6, A1/A2 borderline); hippo, kangaroo, hedgehog, squirrel, ladybird, snail, worm, ant, tortoise,
  turtle, parrot, shark, whale, dolphin, panda, wolf (5-6 A2, the sea animals and wolf possibly 7-8).
  Kept on A1: the pets, farm basics (cow, pig, sheep, horse, duck, chicken) and the classic zoo set
  (lion, tiger, elephant, monkey, bear, snake, frog), plus bird, fish, insects bee/spider/butterfly.
- toys: kite, yo-yo, dice, slide, swing, scooter, skateboard, hide-and-seek (5-6, A2).
- clothes: blouse, sunglasses, pajamas, pullover, sweater, trainer (5-6, A2).
- food: pineapple, plum, melon, peach, cucumber, onion, pea, bean, ham, crisp, cookie, burger, pancake,
  popcorn, cornflakes, cola, honey, jam (5-6 "food in more detail", A2).
- fantasy: dragon, giant, fairy, wizard, unicorn, pirate, treasure, magic (5-6/7-8 stories, A2).
- qualities: brave, naughty, cute, scary (5-6/7-8, A2).

**Added (78):** remaining frequent function words (anything, everything, everyone, someone, somebody,
nobody, each, enough, if, than, until, through, without, may, later, soon, maybe, still, quite, tonight,
more adv, outside/inside/upstairs/downstairs adv) and core A1 words I had left for 5-6, mostly as rec
because primary pupils meet them in teacher talk before producing them: question (prod), answer, mean,
sentence, example; photo, phone (prod), film; town, city, village, hospital, cinema, country, world,
place, left (prod); minute, hour, half; age, person, son, daughter, job, hobby, holiday (prod); euro,
pound, expensive, cheap; begin, change, happen, use, choose, remember, forget, enjoy; different, same,
interesting, boring, difficult, sure, true, free, delicious, healthy, full, empty, high, open.
could/would/should are recorded in the lexicon as past forms of can/will/shall, so they are covered.

**Level changes:** none (band 3-4 is A1 throughout). New totals: 801 lines (486 prod, 315 rec).

## Revision round 2 (final)
Patterns addressed for band 3-4: 2 (re-check round-1 moves), 4 (animals still too early), 5 (celebrations
and weather too early), 6 (remaining A1 function words into 3-4). Own judgement only; new lines `src=ai|rev`.

- **Pattern 2:** re-judged my 73 round-1 removals. None is needed for the first two years of English
  beyond what is still on the list (core pets, farm and zoo animals, basic clothes and food), so none
  was restored. The 5-6 author's "for 3-4" list will be handled when the orchestrator passes it on.
- **Pattern 4, removed (6):** hamster, bee, butterfly, spider, frog, snake → 5-6, A2 (picture-book
  animals, but not core). Kept: animal, pet, dog, cat, mouse, rabbit, bird, fish, horse, cow, pig,
  sheep, duck, chicken, farm, zoo, lion, tiger, elephant, monkey, bear.
- **Pattern 5, removed (8):** foggy, stormy, storm, snowy → 5-6 weather, A2; costume, candle, pumpkin,
  Santa → 5-6 festivals, A2. Kept: Christmas, Easter, Halloween, birthday, party, present, witch, ghost,
  and sun/rain/snow/wind/cloud with sunny, rainy, windy, cloudy, hot, cold, warm.
- **Pattern 6, added (31):** pronouns some, any, all, both, many, much, other, which, myself, yourself;
  determiners most, little, few; shall; after and before as conjunctions; across, along; adverbs ago,
  already, ever, yet, almost, else, early, late, far, right, left; once, twice. Mostly rec (55–70):
  primary pupils hear them in teacher talk and stories; right/left (directions, body sides) are prod.
- **Level changes:** none (all A1). Totals: 818 lines (479 prod, 339 rec); removed 14, added 31.

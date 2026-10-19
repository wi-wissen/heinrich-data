# Run `en-efl-5-6`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-efl-5-6`
    
    Language: English (lexicon language `en`). Track: `efl` (English as a foreign language in German schools; English starts in grade 3).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - Both `grade=` and `cefr=` are required. Use the band ↔ CEFR guide in the README (3-4 → A1; 5-6 → A1 or A2; 7-8 → A2, some B1).
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-5-6/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Band **5-6**, levels **A1/A2**. Output: one file per top-level topic group, named after the first topic's top-level id.
    Another author covers 3-4 in parallel: list only words typically **introduced in grades 5-6** (when in doubt whether pupils already learned it in primary school, leave it out). Cover all topics the README names for 5-6, including function words that come only now and the verbs and adjectives needed to describe daily routine, people, places and past events. Target size: 900–1200 lexemes.
    
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

    Orchestrator note: the lemma index has just been regenerated (same path). It now also lists the adverbs the lexicon derives via `adv=` on adjectives (really, usually, carefully …) as `adv` lemmas. Before you finish, re-check any adverbs you put into `missing.tsv` against the new index and add those that now exist. Modal past forms (could, might, would, should) are forms of can/may/will/shall, not missing lemmas. Output: one file per top-level topic id of each line's first topic.

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

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev1-en.md (you: band 5-6; output directory .../graded/runs/en-efl-5-6/).
    
    Second message (verbatim): Orchestrator addition to revision round 1: the 3-4 author removed 73 words from A1 (rarer animals, specific toys/clothes/food, fantasy words, a few qualities) and suggested later bands for them in the "Revision round 1" section of /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-3-4/decisions.md. Read that section; for each word you judge to be introduced in 5-6, add it to your files with your own level judgement (`src=ai|rev`); list the ones you judge to belong to 7-8 or later in your decisions.md under "for 7-8". Include this in your report.

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

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev2-en.md (you: band 5-6; output directory .../graded/runs/en-efl-5-6/).
    
    Second message: Orchestrator addition to round 2: the 3-4 author removed 14 words and suggests 5-6/A2 for them: hamster, bee, butterfly, spider, frog, snake, foggy, stormy, storm, snowy, costume, candle, pumpkin, Santa. Decide each by your own judgement (add with `src=ai|rev` if 5-6; otherwise note the band in decisions.md). Include it in your report.
    
    Earlier message (after the 9-10 checker round): Orchestrator: the 9-10 author and a checker found words that belong to lower bands. They are listed under "for lower bands" (with a proposed band) in the "Checker round" section and in an earlier "Earlier-band gaps" note of /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/decisions.md. Read only those parts. For every word with proposed band 5-6 (or 3-4), decide by your own judgement whether it is introduced in 5-6; if yes, add it (`src=ai|rev`, your own level/topic/role/conf). Words you judge to be 3-4 or 7-8, list in your decisions.md under "handed on" with the band. Re-run the checker script and report counts briefly. Same clean-room rules.

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

# Decisions log: author run `en-efl-5-6`

Track `efl`, band 5-6, CEFR A1/A2. Clean-room: I worked only from my own knowledge of English, of English
lessons in German secondary schools (years 5 and 6) and from the inputs I was allowed to use: the brief
README, `topics.tsv`, the lemma index and a few spot-checks in our own lexicon files (to understand how
British spellings and `-ly` adverbs are stored). I used no word list, dictionary or web source and did not
open the evaluation repository. I did not look at the parallel 3-4 author's output.

## Approach

1. I went through the 5-6 topic areas in the README (daily routine, hobbies, school life and subjects,
   shopping and money, town/directions/transport, meals, holidays, birthdays, describing people and
   places, simple past events, pets and wild animals, British daily life). For each one I pictured the
   typical textbook situations of years 5 and 6 (a new school in Britain, a day in the life, a trip to
   London, a birthday party, shopping for a present, a school trip, a lost pet story) and listed the words
   pupils need there.
2. Function words and grammar-driven words got their own pass: question words that come with
   wh-questions (why, which, whose), simple-past signal words (ago, yesterday, last, then, suddenly,
   finally), frequency adverbs for the simple present (always, usually, often, sometimes, never),
   comparatives (than, more, most), some/any and compounds (something, anybody, nothing ...),
   possessive pronouns (mine, yours ...), reflexives (receptive or low confidence), prepositions of
   movement and place for giving directions (along, across, past, through, opposite, between),
   conjunctions for joining sentences (because, when, if, while, so, that), modals (must, may, shall,
   will for the future, `do` as auxiliary for questions and negation), ordinal numbers for dates.
3. Verbs and adjectives: I added the verbs for daily routine (wake, brush, wash, dress, leave, arrive,
   catch, miss), for telling past events (happen, fall, hurt, lose, find, break, hide, escape), for
   shopping (cost, pay, sell, spend, save), for describing people and places (tall, thin, curly, blond,
   friendly, shy, clever; noisy, busy, famous, modern) and evaluative adjectives (boring, exciting,
   terrible, amazing ...).
4. Every candidate was checked against the lemma index; the self-check tool reports 0 errors.

## Bands and levels

- **Band means "introduced in 5-6".** The main difficulty was overlap with primary English (3-4). I left
  out words I expect pupils to meet in grades 3-4: colours, numbers to 100, basic body parts and clothes,
  pets and zoo animals, basic food, rooms and furniture, toys, days/months/seasons, simple weather,
  festivals, basic action verbs and the most frequent function words. In a first draft I had ~40 such
  borderline items at confidence 45-55 (e.g. "breakfast", "party", "sea", "guitar", "think", "wear",
  "speak", "question", "angry", "hungry", "park", "walk", "know"); following the instruction "when in
  doubt, leave it out", I removed them all.
- **CEFR:** A1 for words of the very first secondary-school units and core everyday words (subjects,
  timetable, ordinals, cheap/expensive, because, than, usually); A2 for words that come later in year 6
  or are less frequent (reflexive pronouns, while, during, through, firework, temperature, suddenly).
  Result: 520 A1, 451 A2. No line above A2.
- **role:** `prod` by default; `rec` (116 lines) for words pupils meet in texts but are not expected to use
  actively at this stage (several, none, reflexives other than myself/yourself, whisper, lettuce,
  detention, assembly, budgie, fortnight, lorry, Thames, unfortunately ...).
- **conf:** 75-85 for words clearly tied to 5-6 units (hobby, subject, uniform, timetable, pound, penny,
  ago, because, opposite); 60-70 for typical but less certain items; 55 for borderline items that could
  equally be 7-8.

## Borderline cases

- British daily life: flat, underground/tube, queue, jumper, crisps, toast, beans, uniform, blazer,
  headteacher, assembly, detention, pound/penny. Several carry a second topic `anglophone.uk`.
- Health is mainly 7-8 according to the brief; I kept only what a "I'm ill today" or "an accident on the
  way to school" text needs (ill, sick, headache, hurt, accident, dentist, hospital, healthy).
- Jobs and media are 7-8 topics; I kept only a few words that appear in "my family" and "free time"
  texts (job, office, waiter, vet, newspaper, film, program).
- Scotland, Wales, Ireland are listed as receptive A2 (they appear on maps of Britain in 5-6), with low
  confidence; their culture belongs to 7-8.
- `hundred` was removed as likely primary; `thousand`, `million` kept.
- `p.m.` is listed (pos `x` in our lexicon); `a.m.` is missing from the lexicon.

## Lexicon conventions followed

- British and American spellings are one entry in our lexicon with the US lemma; I used the US lemma
  (neighbor, center, theater, favorite, program, yogurt, pajamas, mustache, kilometer) although the
  British form is the one taught.
- `practise` (BrE verb) is the verb `practice`.
- `-ly` adverbs: first missing from the index; after the index was regenerated with the derived
  adverbs, I added 16 of them (usually, really, quickly, slowly, suddenly, finally, carefully, luckily,
  unfortunately, badly, quietly, loudly, easily, happily, nearly, exactly).
- Modal past forms (could, would, might, should) are forms of can/will/may/shall and are not listed
  separately; `can` itself is primary vocabulary and left out.

## Left out / missing

`missing.tsv` lists 19 lexemes that pupils need in 5-6 but which our lexicon lacks or lacks in the needed
part of speech: adverb `yet`, `inside`, `outside`, `later`; noun `past`, `start`; adjectives `born`,
`married`, `disgusting`, `good-looking`; plural noun `glasses` (spectacles); `a.m.`; `guinea pig`,
`double-decker`; interjection `congratulations`; London and festival names (Big Ben, Buckingham Palace,
Tower Bridge, Bonfire Night).

## Output

One file per top-level topic id of each line's first topic (37 files, 971 lines). Within each file, lines
are grouped by their first topic under a `#` header and sorted alphabetically.

## Revision: words now available in the lexicon

Lexicon authors added 14 of the 19 entries in `missing.tsv`. I graded each one from my own judgement,
using the same criteria as in the original run, and added it to the file for its first topic:
- `yet` adv (A2, 60), `inside`/`outside` adv (A1, 60, space), `later` adv (A1, 70, past-event
  sequencing), `past` noun (A2, rec, 60), `start` noun (A2, 55).
- `born` adj (A1, 75, self), `married` adj (A2, 65, family), `disgusting` adj (A2, rec, 55),
  `good-looking` adj (A2, rec, 55), `glasses` noun (A1, 70, body|self).
- `a.m.` x (A2, 60, clock), `double-decker` noun (A2, 70, transport|anglophone.uk),
  `congratulations` intj (A2, 65, celebrations|communication).
`missing.tsv` now keeps only the 5 lexemes that are still absent: guinea pig, Big Ben, Bonfire Night,
Buckingham Palace and Tower Bridge. New total: 985 lines (525 A1, 460 A2; 866 prod, 119 rec).
The checker reports 0 errors.

## Revision round 1

Feedback (aggregate numbers and patterns only, no reference entries): A2 is thin, and band 5-6 lacks the
most. Animal, toy, clothes and food words sit too early. Some reference-B1 words are already on A2 with us.
I revised whole topics from my own knowledge and did not try to guess reference entries. Every added or
changed line carries `src=ai|rev`.

**Added: 425 lines.**
- *Words removed from 3-4 that I judge to be introduced in 5-6 (42).* I read the 3-4 author's "Revision
  round 1" section and added these, all at A2:
  - animals: crocodile, donkey, giraffe, goat, hen, penguin, zebra, bat (rec), dinosaur, snail, worm,
    ladybug (the lexicon lemma for "ladybird"; rec)
  - toys: kite, dice, slide (rec), swing (rec), scooter, hide-and-seek (rec)
  - clothes: blouse, pullover, sweater
  - food: cookie, popcorn, cornflakes, pineapple, plum (rec), melon, peach (rec), honey, jam
  - fantasy: dragon, giant, fairy (rec), wizard, pirate, treasure, magic
  - qualities: scary
  - Already on my list: owl, fox, tail, feed, hedgehog, squirrel, ant, tortoise, parrot, shark, whale,
    dolphin, wolf, skateboard, sunglasses, pajamas, trainer, cucumber, onion, pea, bean, ham, crisp,
    burger, pancake, cola, brave, naughty, cute. I set those still on A1 to A2 (see "Level changed").
- *A2 expansion across all topics (383), plus a few A1 words met first in 5-6* (thanks, video, the pronoun
  `all`):
  - function words: probably, actually, even, anyway, indoors/outdoors, abroad, beside, `as` (adp and
    sconj), both/each as pronouns
  - home and bathroom items: towel, toothbrush, kettle, drawer, furniture ...
  - food in more detail: cherry, corn, muffin, jar, tin, mug, bill ...
  - clothes and accessories: suit, sandal, button, jewelry, ring, wallet ...
  - school subjects and items: biology, religion, exam, quiz, grade, notebook ...
  - everyday technology: laptop, app, website, password, download ...
  - health: cold, cough, flu, fever, medicine, sore ...
  - extended family and friends: grandchild, niece, boyfriend, visitor ...
  - town, transport and travel: store, post, tram, railway, seaside, camp ...
  - simple jobs: firefighter, hairdresser, chef, nurse ...
  - nature: ocean, desert, pond, planet ...
  - A2 verbs: apologize, behave, book, continue, disappear, hug, lock, recycle, repair, unpack, freeze ...
  - adjectives: large/medium, messy, tidy, wooden, striped, pleased, relaxed, honest ...
  - a few more countries: Greece, China, Russia, Japan, Portugal and their adjectives where common

  Most of these are `conf` 55-60. Rarer or regional words are `rec`.

**Level changed: 18 lines, A1 → A2.** These are words that are too specific for A1: fox, dolphin,
goldfish, chess, ketchup, pancake, ham, cola, yogurt, crisp, burger, bean, pajamas, trainer, cute,
headache, dentist, underground.

**Removed: 10 lines (judged to be introduced in 7-8 or later).**
- Rarer animals: eagle, budgie.
- Words that are more B1 than A2, and that I had placed too early: notice, wonder, belong, appear, cover,
  except (adp), nearby, typical.

**For 7-8 (from the 3-4 removals, not added by me):**
- hippo, kangaroo (Australia unit), panda, turtle: rarer or exotic animals.
- unicorn: a niche fantasy word.
- yo-yo: a niche toy, probably not taught explicitly at all.

Plus my own removals listed above: eagle, budgie, notice, wonder, belong, appear, cover, except, nearby,
typical.

**Overlap with 3-4.** The 3-4 author added about 65 core words to A1 that I had listed for 5-6 (for
example anything, everything, someone, nobody, if, than, until, through, without, soon, maybe, still,
tonight, sentence, example, photo, town, city, hospital, minute, hour, euro, pound, cheap, expensive,
happen, remember, forget, enjoy, different, boring, difficult, delicious, healthy). I kept my lines.
Where both bands list a word, the merge should keep the earlier band. I did not remove them myself so as
not to lose coverage if the 3-4 lines change again.

**missing.tsv:** I added 12 rows:
- activity nouns in -ing: shopping, swimming, fishing, cycling, skating, sailing, climbing, jogging
- shampoo
- adjectives broken and lost
- hot dog

New totals: 1400 lines (510 A1, 890 A2; 1182 prod, 218 rec), 40 files. This is above the original target
because the revision asked for substantial A2 expansion. The checker reports 0 errors.

## Checker round (words proposed by the 9-10 author and checker for lower bands)

I read only the "For lower bands" list and the earlier-band gaps note in the 9-10 decisions log. Then I
decided each item from my own judgement.

**Added to 5-6 (14 lines, `src=ai|rev`):** absent adj (A2, rec), reply noun (A2), help noun (A1),
sleep noun (A2), score noun (A2), form noun (A2, rec), play noun (theatre, A2), online adj (A2, rec),
test verb (A2, rec), end verb (A2), trick noun (A2), machine noun (A2), vampire noun (A2, rec),
superhero noun (A2, rec).

**Handed on:**
- To 7-8, from the items proposed for 5-6:
  - fear (verb)
  - so (sconj, "so that")
  - sneeze (noun)
  - tip (noun; the senses are ambiguous)
  - tune (noun)
- To 7-8, from the gaps that came without a proposed band:
  - nouns: cost, record, care, need, tool, use
  - adjectives: close, neat, bossy, grumpy, dumb, adorable, uncomfortable
  - adverbs: sadly, safely, secretly, rudely, gladly
  - names: Canada, India, Africa (the wider English-speaking world is a 7-8 theme)
  - zombie
- To 9-10 or not taught: bloody (a swear word).
- The items the 9-10 author proposed for 7-8 I left to the 7-8 author.

New totals: 1414 lines (511 A1, 903 A2; 1190 prod, 224 rec). The checker reports 0 errors.

## Revision round 2 (final)

Feedback: patterns only. I revised from my own judgement. Every changed or added line carries
`src=ai|rev`.

**Pattern 2: re-judging my round-1 moves from A1 to A2.**
- In round 1 I moved 18 words from A1 to A2. I re-judged them and moved 16 back to A1, keeping them in
  band 5-6: burger, ketchup, pancake, yogurt, cola, ham, bean, crisp, pajamas, trainer, chess, headache,
  dentist, goldfish, underground, cute. These are basic words of the first secondary units. They are A1
  in level, but they are not needed in the first two years of English.
- fox and dolphin stay on A2, because animals are still the topic with the largest shift.
- For 3-4: I judged none of the 18 to be primary core vocabulary.

**Pattern 6: A1 function words for 3-4, removed from 5-6 (43 lines).**
- **For 3-4** (core of the first two years: possessive determiners, basic quantifiers, place
  prepositions, question words, `do`-questions, everyday adverbs and the some/any/every/no compounds):
  - determiners: our, their, every, other, much
  - pronouns: anything, everybody, everyone, everything, nothing, somebody, someone, something
  - prepositions: between, up, down, near
  - conjunctions: if, than
  - question words: when (adv), why (adv)
  - auxiliary: do (aux)
  - adverbs: together, too, really, maybe, soon, more
  - noun: lot (in "a lot (of)")
- **Removed as duplicates of the 3-4 author's own additions:**
  - nobody, each (det), enough (det), until (adp), through, may
  - later, still, quite, tonight, upstairs, downstairs, inside (adv), outside (adv)

  Keeping them in both bands would only contradict the earlier band.

**Pattern 5: celebrations and weather words placed too early.**
- Removed 7 lines and handed them on **for 7-8**: decoration, parade, carnival, mask (celebrations);
  icy, heat, forecast (weather).
- Raised to A2: candle, foggy, storm. hamster is raised to A2 as well, for pattern 4 (animals).

**Words the 3-4 author removed in this round:**
- Added to 5-6 at A2: bee, butterfly, spider, frog, snake (all prod, conf 60) and pumpkin (rec).
- Already on my list: hamster (now A2), foggy and storm (now A2), stormy, snowy, costume, candle (now A2).
- Not added: Santa. I judge it to be 3-4 (the Christmas topic of primary English), so I hand it back
  **for 3-4**.

**Pattern 1: more A2 verbs and adverbs (71 lines).**
- 52 verbs, including: cycle, dry, earn, improve, lift, measure, organize, post, pour, pretend, remind,
  ring:sound, sign, stick, surprise, disagree, divide, lie:untruth, breathe, and receptive kitchen and
  household verbs (chop, peel, stir, sweep, iron, wipe).
- 19 adverbs: correctly, aloud, hard, politely, fortunately, hopefully, seriously, mostly, properly,
  clearly, backwards, forward, ahead, heavily, angrily, nicely, beautifully; plus fast and well (adverb,
  A1).

**Counts for this round:** 77 lines added (6 from the 3-4 removals, 71 verbs and adverbs); 20 lines with
a level change (16 back to A1, 4 to A2); 50 lines removed (43 for 3-4, 7 for 7-8).

New totals: 1441 lines (490 A1, 951 A2; 1176 prod, 265 rec), 39 files. The checker reports 0 errors.

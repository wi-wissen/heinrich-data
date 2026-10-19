# Run `en-efl-5-6`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

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

## Follow-up message 1 (verbatim)

    Orchestrator note: the lemma index has just been regenerated (same path). It now also lists the adverbs the lexicon derives via `adv=` on adjectives (really, usually, carefully …) as `adv` lemmas. Before you finish, re-check any adverbs you put into `missing.tsv` against the new index and add those that now exist. Modal past forms (could, might, would, should) are forms of can/may/will/shall, not missing lemmas. Output: one file per top-level topic id of each line's first topic.

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

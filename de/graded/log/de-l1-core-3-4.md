# Run `de-l1-core-3-4`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-l1-core-3-4`
    
    Language: German (lexicon language `de`). Track: `l1` (German as a first language).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - `grade=` is required; leave out `cefr=`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-l1-core-3-4/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Area `core`, band **3-4** only (third and fourth grade). Output file: `core.tsv`.
    Another author covers band 1-2 in parallel: list only words that are typically **introduced in grades 3-4**, not the basic words of grades 1-2 (when in doubt whether a word is 1-2, leave it out of your list). Cover all topics the README names for band 3-4 (neighbourhood and town, traffic, shopping and money, jobs, festivals, nature, media, living together, feelings and character in more detail, time relations, causes and consequences, verbs of saying and moving, school life), including the function words that typically come only now (e.g. less frequent conjunctions, prepositions and adverbs). Target size: 600–900 lexemes. Mostly `role=prod`.
    
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

## Follow-up message 1 (verbatim; the agent received a one-line pointer to this text)

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

# Decisions log – author run `de-l1-core-3-4`

Track `l1`, area `core`, band 3-4, output `core.tsv` (898 lexemes), work list `missing.tsv` (137 rows).

## Inputs and method
- Inputs used: the brief (graded README), `topics.tsv`, the lemma index of our own lexicon, and the
  checker script. No word lists, dictionaries, web search or other external sources; nothing under
  heinrich-eval was opened. The frequency list was not needed.
- I went through the band 3-4 situations of the brief one by one (way to school and traffic education
  incl. the cycling test, neighbourhood and town, shopping and pocket money, adults' jobs, festivals
  through the year, nature walks and simple experiments, media use and letters/e-mail, class council and
  rules of living together, finer feelings and character for story writing, time relations and
  causes/consequences for retelling and reasoning, exact verbs of saying and moving for narrative
  writing, everyday school life and working techniques) and wrote candidates from my own knowledge,
  plus function words that typically enter written language only now (subordinating conjunctions such
  as obwohl/nachdem/sobald/sodass/falls, the dass spelling, genitive-type prepositions wegen/trotz/
  während/statt, indefinite and directional adverbs, wo+preposition question words, relative der).
- First draft had about 1,550 candidates. Each was checked mechanically against the lemma index; words
  not in the lexicon (mostly compounds such as street-furniture, traffic and school compounds) went to
  `missing.tsv`, wrong part-of-speech guesses (adverbial adjectives like plötzlich, häufig; selbst/selber
  as adverbs) were corrected to the lexicon's POS. Homographs use the lexicon's senses
  (Bank:financial, Kiefer:pine, Ton:sound, Flur:hall, Plastik:plastic, überlegen:think,
  schaffen:manage was dropped later, erschrecken:intransitive, wiegen:weigh, der:rel).

## Trimming to the target size
- Following the instruction "when in doubt whether a word is 1-2, leave it out", I removed every
  candidate I had given confidence 60 or lower because it might already be a grade 1-2 word (e.g. common
  animals, basic household objects, everyday food, very common verbs). Exceptions kept with conf 60-65:
  dass, sondern, jemand, niemand, plötzlich, relative der — their written use is typical of 3-4.
- I removed words I judged to belong rather to 5-6 or later (abstract nouns such as justice, culture,
  origin, tradition; finer emotion words such as despair, shame; formal speaking verbs; detailed
  anatomy, which also belongs to the subject areas), and thinned the topics the brief does not name for
  this band (home, food, body, health, people, play, travel) to the words that typically come with new
  3-4 situations (person description, recipes, simple first aid, club sports, class trips).
- Tree and bird species, crafting materials and tools were reduced to the most typical nature-walk and
  handicraft words; science and maths terms are left to the subject-area authors.

## Roles and confidence
- Almost everything is `role=prod` (882): pupils are expected to use these words in their own retellings,
  letters, reports and descriptions. `role=rec` (16) for words pupils mostly meet in texts or signs
  (Lebensraum, Recycling, Energie, Gegenwart as tense term, oberhalb/unterhalb, derselbe, jener, solcher,
  einander, relative der, weswegen, Fahrgast, Fahrer context words, etc.).
- Confidence: 80-85 for core traffic-education and class-council words and the central conjunctions;
  75 default; 65-70 for words that could equally be 1-2 or 5-6 (e.g. Bahnhof-type town words, Geschäft,
  meistens, wählen).

## Borderline cases
- Umzug is listed once with two topics (town|celebrations: moving house and the lantern/carnival parade).
- seitdem and während appear twice with different POS (sconj/adv, sconj/adp), as allowed.
- Words left out despite fitting the topics because I consider them 1-2: Ampel, Auto, Bus, Geld, kaufen,
  Polizei, Feuerwehr, Weihnachten, Ostern, Geburtstag, weil, wenn, aber, oder, ob (borderline, dropped).

## missing.tsv
137 lemmas I wanted but the lexicon does not contain (mostly compounds such as Zebrastreifen, Radweg,
Fahrradhelm, Verkehrszeichen, Rathaus, Taschengeld, Klassenrat, Einkaufszettel, Hausnummer,
Postleitzahl, Inhaltsverzeichnis; and a few simplex words such as leidtun, stapeln, auswendig,
verheiratet). They are not in `core.tsv`; lexicon authors can add them, after which they should be
graded 3-4.

## Revision (follow-up: newly available lemmas)
- The lexicon authors added most words of my work list; `now_available.tsv` listed 131 of the 137 rows.
- For each of them I kept the judgement from my original draft (band 3-4, topic, role, confidence were
  written before the lexicon check and had only been set aside because the lemma was missing), and
  re-generated `core.tsv` from the same draft with the regenerated index. No new senses were needed;
  no existing line changed.
- `core.tsv` now has 1,029 lexemes (1,006 prod, 23 rec), above the 600–900 target, because the
  added words are mostly band-typical compounds (traffic, town, school, shopping, festivals) that I
  had wanted from the start; I did not drop other words to compensate.
- `missing.tsv` keeps the 6 rows still absent: geöffnet, Kräuter, Medien, verspätet, geschieden,
  kaputtgehen (not added because of a grammar-rule conflict; zerbrechen already covers the meaning).
- Checker: 0 errors, 0 warnings.

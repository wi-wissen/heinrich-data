# Run `de-l1-core-1-2`

Author: an AI agent (the project's stronger model; identifier not recorded, CLAUDE.md rule 8). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-l1-core-1-2`
    
    Language: German (lexicon language `de`). Track: `l1` (German as a first language).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - `grade=` is required; leave out `cefr=`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-l1-core-1-2/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Area `core`, band **1-2** only (first and second grade). Output file: `core.tsv`.
    Cover the general vocabulary children learn to read, write and use actively in grades 1-2: all topics of the 'General vocabulary' block of the catalogue that the README names for band 1-2 (self, body, family, people, home, food, clothing, school, play, animals, plants, nature, weather, time, numbers, colours, space, feelings, celebrations, simple actions and qualities). **All of the most frequent ~100–150 function words must be in this band** (articles, personal and possessive pronouns, common prepositions, und/oder/aber/weil/dass/wenn, question words, sein/haben/werden and the modal verbs, frequent adverbs like hier, da, jetzt, heute, nicht, auch, sehr, noch, schon). Target size: 600–850 lexemes. Mostly `role=prod`.
    
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

# Decisions log – run `de-l1-core-1-2` (L1 German, area `core`, band 1-2)

## Inputs and method

- Inputs used: the brief `README.md`, `topics.tsv`, the lemma index `de_lemmas.tsv` (to check spelling,
  part of speech and senses) and our own frequency list `forms.tsv` (only its top ~260 forms, to confirm
  that no very frequent function word was forgotten). No published word list, dictionary or web source
  was used; WebSearch/WebFetch were not used; `heinrich-eval` was not opened.
- I went through the general-vocabulary topics of the catalogue one by one and, for each, imagined the
  situations the brief names for grades 1-2 (talking and writing about oneself, family, friends, home,
  the school day, toys, animals, food, clothes, the body, weather and seasons; naming things; simple
  actions and feelings; counting and comparing). I listed nouns, then deliberately the verbs and
  adjectives needed in those situations, then the function words.
- First draft: about 990 candidates. The check against the lemma index found 28 compounds/words not in
  the lexicon; they went to `missing.tsv`. To reach the target size (600–850) I then removed about 125
  candidates that I judged more likely to be *introduced* in grades 3-4 or later, or that are regional /
  peripheral (see below). Final: 850 lexemes, all `role=prod`, all `grade=1-2`.

## Function words

- All articles (der, ein), personal pronouns including formal Sie, the reflexive sich, man, possessive
  determiners (mein … euer), dieser/jeder/kein/all/viele/beide/paar/bisschen, etwas/nichts/jemand/
  niemand, the common prepositions and their contractions (am, im, ins, ans, beim, vom, zum, zur),
  und/oder/aber/denn/sondern, weil/dass/wenn/als/ob/wie/bis, the particles nicht/ja/nein/doch/mal/schon/
  zu/gar/eigentlich, the question words, sein/haben/werden and the six modal verbs (as `aux`), and the
  frequent adverbs of place, time, manner and degree.
- I compared against the top of our own frequency list only to catch omissions; that led me to add
  selbst, nun, dafür, damit (adv), sonst, darum, gerade and the pronoun use of `all` (alles).
  Formal/written-register words (jedoch, sowie, etwa, deren, dessen, während) were left for later bands.
- `damit` (adv), `nun`, `sondern`, `sonst`, `dafür` got conf 60-70: frequent, but children use them
  actively only towards the end of grade 2.
- Relative `der:rel` was left out (relative clauses in writing are a 3-4 topic); demonstrative
  `der:dem` was included (conf 75) because it is constant in children's speech.
- Missing in the lexicon: `mehr`, `weniger`, `weiter` (adv), `nochmal` → `missing.tsv`.

## Numbers

- Cardinals 0-20, the tens up to 90, hundert; ordinals erste–fünfte; einmal/zweimal; halb, Hälfte,
  letzt, viel, Zahl. The compound cardinals 21-99 were deliberately not listed one by one: they are
  regular, productive forms and belong more naturally to the `math` area (numbers to 100); listing 72
  of them would distort the core list. tausend and zehnte were dropped as 3-4.

## Bands, confidence and borderline cases

- Confidence 90-99: words every first-grader uses (body parts, family, colours, basic verbs).
  80-89: clearly grade 1-2 but sometimes a little later in writing. 60-79: borderline between 1-2 and 3-4
  (e.g. Geschwister, Gewitter, Hälfte, gerade, Viertel, ängstlich, aufgeregt).
- Day names, months and seasons are all 1-2 (calendar work in grades 1-2); months conf 82 since some
  are written correctly only in grade 2.
- A few words outside the brief's listed 1-2 topics were included because they are everyday words of
  six-year-olds: Auto, Bus, Zug, Ampel, Flugzeug, Schiff, Boot (traffic); Straße, Stadt, Dorf,
  Kindergarten, Supermarkt, Schwimmbad (town); Geld, Euro, kosten (money); Polizei, Polizist,
  Feuerwehr (jobs). The fuller traffic/town/shopping/jobs vocabulary is left to band 3-4.
- Homographs: used senses Mutter:parent, Junge:boy, Rock:skirt, Hut:hat, Morgen:daytime, See:lake,
  Orange:fruit, Pony:horse, Tor:gate (goal in football), wachsen:grow.
- Decke (ceiling/blanket) has no sense split in the lexicon; listed once under home.
- `role=prod` throughout: at this band the core list is by definition the vocabulary children are
  expected to use and write themselves.

## Left out (judged 3-4 or later, regional or peripheral)

- Body/health details: Stirn, Backe, Ellenbogen, Knochen, Haut, Blut, Zeh, Schmerz.
- Household details: Balkon, Keller, Herd, Ofen, Regal, Teppich, Spiegel, Kissen, Becher, Schüssel,
  Flur, Computer.
- Less central food: Erbse, Paprika, Zwiebel, Pflaume, Traube, Joghurt, Müsli, Kaffee, Pommes, Würstchen.
- Clothing details: Strumpf, Knopf, Turnschuh.
- Animals/plants beyond the familiar: Hirsch, Delfin, Hai, Wal, Dinosaurier, Mücke, Meerschweinchen,
  Pfote, Feder, Flügel, Futter, Stall; Ast, Busch, Strauch, Stamm, Wurzel, Samen, Blüte, Tulpe, Tanne,
  Kastanie, Gänseblümchen.
- Nature/weather: Natur, Luft, Bach, Insel, Teich, Höhle, Welle, Schatten, Hagel.
- Feelings/abstract: Gefühl, Mut, Schreck, Liebe, stolz, trösten, erschrecken.
- Celebrations: Advent, Silvester, Karneval (Fasching kept), Feier, Einladung, Engel, Nikolaus.
- Others: Sohn, Tochter, Cousin, Cousine, Herr, Nachbar, Gast, Alter, Riese, Ritter, Zauberer, Karte,
  Seil, Film, Kirche, Laden, Park, Cent, Bäcker, Bauer, Unterricht, Kreide, Ranzen, wichtig, schwierig,
  schmal, golden, bitter, glatt, wild, schwach, doppelt, einige, irgendwo, nebenan, weggehen,
  zurückkommen, reparieren, schieben, flüstern.
  Many of these are known orally in grades 1-2 but are typically introduced for reading/writing in 3-4.

## Missing lemmas

32 entries in `missing.tsv`: mostly everyday compounds that the lexicon does not yet contain
(Kinderzimmer, Wohnzimmer, Schlafzimmer, Badezimmer, Mittagessen, Abendessen, Apfelsaft, Zahnbürste,
Handtuch, Spielzeug, Sandkasten, Schneemann, Regenbogen, Tannenbaum, Sonnenblume, Löwenzahn, Regenwurm,
Handschuh, Schlafanzug, Unterhose, Badehose, Uhrzeit, Adventskalender, Christkind, Großmutter,
Großvater), the simplex Erdbeere and Po, and the adverbs mehr, weniger, weiter, nochmal.

## Revision (follow-up: lemmas now available)

- All 32 rows of `missing.tsv` now exist in the regenerated lemma index (`now_available.tsv`). I added
  each one to `core.tsv` with the band, topic and confidence from my original judgement: grade 1-2, `role=prod`,
  `src=ai`, filed under the topic noted in `missing.tsv`. Po exists only with a sense split (noun `bottom`
  vs. the river as propn), so it is listed as `Po:bottom`. Tannenbaum went to plants only and
  Schneemann to weather only (one line per lemma).
- `mehr` (conf 90) and `weniger` (conf 80) went to `numbers` (comparing quantities); `weiter` went to
  `function.adverb` and `nochmal` to `time.relations`. These close the function-word gaps noted earlier.
- `missing.tsv` now has only its header row. The checker reports 0 errors.
- The new size is 882 lexemes, slightly above the 600-850 target. I kept the additions because they
  are core grade 1-2 words (rooms, meals, everyday clothing, mehr/weniger) that were left out only
  because the lexicon lacked them. I did not move any other word out in exchange.
- `großschreiben`, `kleinschreiben` and `kaputtgehen` were not part of my list; nothing to replace.

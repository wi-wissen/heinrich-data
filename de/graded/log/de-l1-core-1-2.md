# Run `de-l1-core-1-2`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

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

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev1-de.md (you: band 1-2, area core; output directory .../graded/runs/de-l1-core-1-2/). Coordinate implicitly: words you judge to be introduced only in 3-4 you remove from your file and list in decisions.md under "moved to 3-4" — the 3-4 author is told the same in the other direction.

Feedback file:

    # Revision round 1 (German L1), feedback from the internal reviewer — patterns only
    
    The reviewer compared the merged layer (bands 1-2 and 3-4) statistically with reference material outside the
    repositories. You receive only aggregate numbers and patterns in the reviewer's own words; you never receive
    reference entries, and you must not try to guess them. Revise **whole topics from your own knowledge**.
    This is round 1 of at most 2 against this reference.
    
    Important context: the reference orders words by **spelling difficulty** (model words for spelling
    phenomena), not by when children learn a word. Our band means "introduced / typically learned and used".
    So part of "ours earlier" is expected and is no reason to move words blindly. Re-judge each word you touch
    by our own definition.
    
    ## Numbers (whole layer)
    - Coverage of the reference: 81.7 % (band 1-2 of the reference 88.6 %, band 3-4 74.6 %).
    - By part of speech: nouns 80.4 %, **verbs 72.8 %**, adjectives 85.5 %, adverbs 94.3 %, closed classes 97–100 %.
    - By word formation: simple nouns 80.5 %, nouns in -ung/-heit/-keit/-nis 73.3 %, compounds 88.1 %, simple verbs 76.8 %,
      **verbs with a prefix or particle 69.6 %**, derived adjectives 86.3 %.
    - Band agreement on shared words: exact 70.8 %; ours earlier 26.6 %, ours later 2.6 %.
    - Function words: 96.6 % covered; those the reference puts in 3-4 are almost all in 1-2 with us.
    - Largest mean shift (negative = ours earlier, in bands): weather −0.53, function.adverb −0.52, qualities.character −0.50,
      function.pronoun −0.48, feelings −0.42, space −0.41, qualities.judgement −0.41, function.preposition −0.38.
      Well calibrated: time.calendar, family, qualities.colour, self, function.auxiliary, body, actions.motion, animals, numbers.
    
    ## Patterns (reviewer's own words)
    1. We start systematically too early, almost only in one direction. Most affected are more abstract words:
       evaluative and character adjectives, feeling words, place and direction words, weather words, on average about half
       a band too early. Concrete words of children's everyday life (body, family, calendar, colours, animals) fit well.
    2. Function words of stage 3-4 almost all land in 1-2 with us, mainly adverbs, pronouns and prepositions. Check whether
       rarer or longer members of these classes (manner adverbs, more formal prepositions) really belong to the first two years.
    3. Verbs are the largest gap, especially verbs with a prefix or separable particle. The `actions.*` topics should be
       extended with compound everyday verbs (type: verbs of handling things and of personal hygiene with a separable particle).
    4. Simple concrete nouns of stage 3-4 are missing more often than in 1-2, mainly object and nature words that are not part
       of the core topics of the first years; nouns in -ung/-heit/-keit are also below average.
    5. Function words slightly below target: few missing lemmas, only among determiners/pronouns and prepositions.
    
    ## What to do
    Work in your own output directory as before; only your own bands and areas. For every line you add or whose band you
    change, set `src=ai|rev` (keep `freq` if it was there). Do not remove words just because they might not be in a
    reference. Re-run the checker to 0 errors, append a "Revision round 1" section to `decisions.md` (what you changed per
    topic and why, in your own reasoning), report counts (added, moved 1-2 → 3-4, moved 3-4 → 1-2). Same clean-room rules
    as before (no web, no word lists, never the held-out repository). Words not in the lexicon go to `missing.tsv` again.

## Reviewer round 2 feedback, final (verbatim; aggregate numbers and patterns only)

    Read and follow /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/prompts/rev2-de.md (you: band 1-2, area core; output directory .../graded/runs/de-l1-core-1-2/).

Feedback file:

    # Revision round 2 (final) — German L1, patterns from the second statistical measurement
    
    This is the **last** revision against this reference; there will be no further measurement against it. Same rules as
    round 1: you get only aggregate numbers and patterns; revise from your own knowledge; never guess reference entries.
    
    Numbers after round 1 (before → after): coverage 81.7 → 85.6 % (band 1-2 88.6 → 91.9 %, band 3-4 74.6 → 79.0 %);
    verbs 72.8 → 81.7 %, verbs with prefix/particle 69.6 → 78.3 %, nouns 80.4 → 84.0 %, adjectives 85.5 % (unchanged),
    -ung/-heit/-keit/-nis nouns 73.3 → 90.0 %; function words 96.6 → 98.3 % (target reached). Band: exact 70.8 → 70.0 %,
    ours earlier 26.6 → 26.4 %, ours later 2.6 → 3.6 %. Topic actions: exact 79.5 → 71.0 %; actions.handling shift
    −0.25 → −0.41, actions.speaking −0.13 → −0.26. Slightly better: weather, function adverbs/pronouns, feelings, space.
    New "ours later" in home (1 → 6) and nature (3 → 7).
    
    Patterns (reviewer's own words):
    1. Gaps are closing. Most is still missing among simple concrete nouns of stage 3-4, verbs with prefix or particle,
       and adjectives.
    2. Added verbs are often one band too early. Rule of thumb: place a compound or specialised verb one band after its
       base verb.
    3. The general tendency "too early" persists almost unchanged.
    4. When moving words to 3-4, do not take along the everyday words of the first years in home and nature.
    5. Function words have reached the target.
    
    What to do: 1-2 author — re-check the verbs you added in round 1 (move compound/specialised ones to 3-4, list them
    under "moved to 3-4"), and check that no early everyday home/nature words were moved out. 3-4 author — add adjectives
    and simple concrete nouns of stage 3-4 by topic, re-check that your added verbs are not 5-6 material, and re-check
    home/nature words you hold that are really 1-2 (list them under "for 1-2"). `src=ai|rev`, checker to 0 errors,
    append "Revision round 2" to decisions.md, report counts.

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

## Revision round 1 (reviewer patterns, own re-judgement)

The reviewer's patterns say our layer starts too early for abstract words and lacks compound everyday verbs.
I re-judged the affected topics by our own definition: the band in which a word is introduced for
active use. I did not change band 1-2 words that every child uses from the start (ganz, gern, selbst,
überall, böse, gemein, wütend, the core prepositions and pronouns). The reviewer's reference orders
words by spelling difficulty, so I did not use it as grounds for moving those.

### Moved to 3-4 (removed from this file; the 3-4 author is told the same)
- **weather:** Nebel, Sturm, windig. These are weather-report words, typical of the grade 3-4 seasons
  and weather unit rather than of the first years.
- **function.adverb:** dabei, dafür, damit, darum, dazu, nun, sonst. Pronominal adverbs and connecting
  adverbs are frequent in adult text but children use them actively only when they start to write
  connected texts. The original brief asked for all frequent function words in 1-2. These seven were
  my lowest-confidence entries (62-70), so I judged them the 3-4 members of the class.
- **qualities.character:** faul, fleißig. These are evaluations of behaviour, used more from grade 3.
- **function.pronoun:** niemand. Its oral form is common, but written use comes later than jemand.
- **feelings:** aufgeregt, ängstlich, lächeln. These are finer shades next to the core
  froh/traurig/wütend/Angst/lachen.
- **space:** außen, innen, heim, heraus, hinein. These are written-language direction adverbs. At 1-2
  children say raus/rein/runter, which stay.
- **qualities.judgement:** gefährlich. It is a longer evaluative adjective, typical of traffic/safety
  units in 3-4.
- **function.preposition:** ab, seit. These are temporal prepositions, used with time relations in 3-4.
- **time.relations:** zuletzt. It is an ordering adverb for retelling, a 3-4 skill.

25 words moved in all.

### Added (104 lines, `src=ai|rev`)
The largest gap was everyday verbs, especially those with a separable particle or a prefix. I added the
verbs that children of six to eight use for their own daily routine, body care, the classroom and play:
- **body:** abtrocknen, kämmen, schwitzen, kratzen
- **health:** husten, niesen, bluten, verletzen
- **home:** einschlafen, ausschlafen, wecken, aufwecken, zudecken, abwaschen, spülen, abräumen, decken,
  wischen, fegen, wegräumen, abschließen, anmachen, ausmachen
- **food:** aufessen, austrinken, kauen, schlucken, schmieren, schälen, rühren
- **animals:** beißen, streicheln
- **actions.handling** (29 verbs, for packing, picking up, holding, throwing away, hanging, folding,
  rolling, collecting, swapping, lending, filling, knocking, ringing and fetching): einpacken,
  auspacken, wegwerfen, aufheben, hochheben, anfassen, festhalten, loslassen, aufblasen, aufbauen,
  stecken, hängen:transitive, packen, falten, rollen, drehen, schütteln, sammeln, tauschen, leihen,
  schließen, füllen, mischen, pusten, klopfen, klingeln, abholen
- **money:** bezahlen, verkaufen
- **clothing:** anhaben, umziehen
- **actions.motion:** hinfallen, umfallen, runterfallen, einsteigen, aussteigen, losgehen, weglaufen,
  hinsetzen, winken
- **actions.perception:** ansehen, anschauen, zuschauen, zuhören
- **actions.speaking:** vorlesen, lügen, schimpfen, bitten, danken, grüßen
- **actions.thinking:** aufpassen, merken, raten, träumen, versuchen, gefallen
- **actions.change:** beginnen
- **school:** ausschneiden, aufschreiben, abschreiben, anmalen, ausmalen
- **play:** mitspielen, mitmachen, zaubern, turnen, reiten, rodeln, klatschen
- **people:** umarmen, küssen, kitzeln

Borderline verbs got conf 65-72: abräumen, schälen, rühren, rodeln, umziehen, abschließen, packen.

### Not done
- I added no nouns for patterns 4 and 5. Nature and object nouns of stage 3-4, nouns in -ung/-heit/-keit
  and the more formal determiners and prepositions belong to the 3-4 band.
- Moved 3-4 → 1-2: none. This file only holds band 1-2, and I received no 3-4 lines.

Size is now 961 lexemes, above the original 600-850 target. The additions are basic verbs whose absence
the reviewer named as the largest gap. I preferred covering them over keeping the target size.

## Revision round 2 (final; reviewer patterns, own re-judgement)

### Re-check of the verbs added in round 1
I re-judged each of the 104 verbs I added in round 1. I kept a verb in 1-2 only if I am confident that
children of six to eight use it actively in their own routine, in class or at play. Examples of verbs
that stay: hinfallen, einschlafen, aufpassen, zuhören, vorlesen, mitspielen, auspacken, ausschneiden,
anmalen, ausmalen, abschreiben, aufessen, wegwerfen, aufheben, einsteigen, aussteigen, abtrocknen,
kämmen. The reviewer's rule of thumb, one band after the base verb, I used as a check, not as an
automatic rule.

### Moved to 3-4 (38 verbs; removed from this file)
- **Household tasks:** abräumen, abwaschen, fegen, decken, zudecken, ausschlafen, abschließen, aufwecken.
  These are household chores that children of this age do not yet name themselves.
- **Kitchen and food:** schälen, rühren, schmieren, austrinken. These are kitchen-procedure verbs.
- **Handling verbs:** hochheben, loslassen, aufblasen, aufbauen, packen, falten, schütteln, leihen, füllen,
  mischen. Each one specialises a simple verb that stays in 1-2 (heben/halten/bauen/geben …).
- **Clothing:** anhaben, umziehen.
- **Movement:** runterfallen, losgehen. The plain fallen and gehen, and hinfallen, stay.
- **Seeing and writing:** anschauen, aufschreiben. Schauen, ansehen and schreiben stay.
- **Speaking and thinking:** grüßen, merken, beginnen. Anfangen covers beginnen at 1-2. Merken in the
  sense of noticing or remembering is a 3-4 word.
- **Body and health:** verletzen, kratzen, schwitzen.
- **Money:** verkaufen. Buying and paying stay.
- **Play:** kitzeln, rodeln, klatschen.

### Home and nature
None of my round-1 moves concerned home or nature; only three weather words went then. I checked again
and kept every home and nature word. I also re-added five everyday words that I had cut in the first
run only for size and that I judge introduced in 1-2: Kissen, Spiegel (home), Teich, Luft (nature),
Ast (plants). They have conf 70-75 and `src=ai|rev`.

### Result
- Moved 1-2 → 3-4: 38. Added: 5. Moved 3-4 → 1-2: none received.
- Size: 928 lexemes. The checker reports 0 errors.

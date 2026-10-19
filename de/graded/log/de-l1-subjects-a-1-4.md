# Run `de-l1-subjects-a-1-4`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-l1-subjects-a-1-4`
    
    Language: German (lexicon language `de`). Track: `l1` (German as a first language).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - `grade=` is required; leave out `cefr=`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-l1-subjects-a-1-4/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Areas `math` and `science` (primary general studies: nature, the body, materials, simple physics and technology), bands **1-2 and 3-4**. Output files: `math.tsv`, `science.tsv`.
    Include the subject terms pupils use in grades 1-4 in these subjects (operations, shapes, measures and units, place value; habitats, animals and plants as subject matter, the body and health, materials, water, air, weather phenomena, electricity, magnetism, sun and moon, simple machines, experimenting). Words that are general everyday vocabulary (Hund, Baum) belong to `core` authors — include them only if they are typical subject terms. Use `role=rec` for terms pupils mainly understand. Target size: 250–450 lexemes.
    
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

## Decisions log (written by the author)

# Decisions – author run `de-l1-subjects-a-1-4`

Areas `math` and `science` (primary general studies), bands 1-2 and 3-4, track `l1`.

## Inputs and approach

- Read the brief (`README.md`) and `topics.tsv` completely; used only the lemma index of our own
  lexicon to check candidates. No web access, no published word lists, no dictionaries, no other runs'
  files, nothing under `heinrich-eval`.
- Went topic by topic through the catalogue entries that fit primary maths (`math.numbers`,
  `math.arithmetic`, `math.geometry`, `math.measures`, `math.data`, `math.reasoning`) and primary
  general studies (`science.method`, `bio.*`, `chem.substances`, `chem.reactions`, `phys.*`, `tech`,
  plus `weather`, `health`, `environment`, `geo.water` where these were the most specific fit).
  For each topic I pictured the typical lessons (number-space work with place-value material, the
  times table, written methods, shape and solid sorting, symmetry folding, measuring and weighing,
  tally charts and dice games; senses, skeleton and organs, teeth and nutrition, the hedgehog and
  squirrel units, the forest storeys, early bloomers and seeds, material sorting, floating and
  sinking, melting and evaporating, simple circuits, magnets, moon phases, levers and tools,
  experiment protocols) and wrote down the words pupils hear and use there, then checked each
  against the index.
- First draft was ~870 candidates; 225 were not in the lexicon (mostly compounds) and went to
  `missing.tsv`; the remaining ~650 were cut to 441 to meet the 250–450 target.

## Bands, roles, confidence

- `1-2` for words used from the first lessons of a unit (Zahl, Ziffer, Einer/Zehner, plus/minus/mal,
  Dreieck, Kugel, Lineal, Zentimeter, Thermometer, Magnet, Igel, Wurzel, schmelzen).
  `3-4` for the expansion beyond 100 (Tausender, Million, runden, überschlagen), written methods
  (schriftlich, untereinander), the Latin operation names, solids (Quader, Zylinder, Kegel),
  symmetry, measures beyond cm/m, chance (wahrscheinlich, unmöglich), and in science for habitats,
  organs, nutrients, materials and their properties, circuits, magnet poles, planets, levers.
- `role=rec` for terms pupils mainly meet in teacher talk or textbooks (Quotient, Faktor, Differenz,
  Pipette, Becherglas, Amphibie, Pubertät, Bestäubung, Elektrizität, Auftrieb, isolieren); `prod` for
  terms pupils write in their own tasks and reports.
- Confidence 85–95 for core unit words, 60–75 for borderline band choices (Latin operation names,
  Milliarde, Raute, Durchmesser, Umfang, Pipette, Auftrieb, isolieren).
- No entries in 5-6 or later: a few 5-6 candidates (Prisma, Radius, Gleichung, Aggregatzustand,
  Kohlendioxid, Klima, Wirbeltier) were removed because they are outside my bands and are introduced
  later.

## Borderline cases

- `plus`/`minus` used with pos `cconj` (the index has no adverb); `mal` as `adv`; `durch` as `adp`.
  `geteilt` (in "geteilt durch") is not in the index as an adjective → missing.tsv with a note.
- `mehr`/`weniger` are comparatives of `viel`/`wenig` (core vocabulary) → left out.
- `lösen` appears in both files (solving a task in maths, dissolving in science); the lexicon has no
  sense split, so both entries use the bare lemma.
- `Leiter` needs a sense "electrical conductor"; the index has only ladder/person → missing.tsv
  instead of a wrong sense.
- `Kiefer:pine`, `Ton:clay`, `Tau:dew`, `wiegen:weigh`, `wachsen:grow` used with the listed senses.
- `Celsius` only exists as `propn`; kept as propn (as in "Grad Celsius").
- `Körper` (geometric solid) and `Netz` (net of a solid) recorded without sense although the
  geometric sense is distinct; a sense split may be wanted later.

## What I left out and why

- General everyday words that core authors cover: Wasser, Luft, Feuer, Regen, Schnee, Wind, Wolke,
  Sonne-like everyday weather words were cut except where they are clearly unit terms (Sonne, Mond,
  Erde, Stern kept for the astronomy unit); everyday animals (Biene, Spinne, Schnecke, Reh), everyday
  body words (Herz, Blut, Magen), everyday materials (Glas, Papier, Sand), bicycle parts (traffic,
  core 3-4), common tools (Hammer, Säge), general school words (Aufgabe, Frage, Antwort, richtig,
  falsch, Beispiel, Regel).
- Some rarer subject words trimmed for size (Niere, Leber, Volt, Spannung, Komet, Roggen/Hafer/Gerste,
  Molch, Libelle).
- Many central compounds are missing from the lexicon (Einmaleins, Zahlenstrahl, Stellenwerttafel,
  Tauschaufgabe, Würfelnetz, Strichliste, Säulendiagramm, Stromkreis, Nahrungskette, Winterschlaf,
  Sinnesorgan, Wasserkreislauf, Mondphase, Regenbogen, Haustier, …): all are in `missing.tsv` with
  the topic and intended band, for the lexicon authors.

## Revision (lexicon follow-up)

- The lexicon authors added most rows of `missing.tsv`, and the lemma index was regenerated.
  `now_available.tsv` listed 222 rows. For each I set band, topic, role and confidence from my
  own judgement, using the same criteria as in the first pass. In practice they match what I had
  planned for these words before they had to be moved to `missing.tsv`.
- Added 217 lines: 82 to `math.tsv` and 135 to `science.tsv`. Electrical conductor is now
  recorded as `Leiter:conductor` (3-4, rec).
- Not added: Feststoff, Kondensation, Magnetfeld, Isolator and Umlaufbahn. I place their
  introduction in 5-6, which is outside this run's bands; this is the same rule I applied to other
  5-6 words in the first pass. They were removed from `missing.tsv`, because they are now in the
  lexicon.
- `missing.tsv` now keeps only Erste-Hilfe (needs a multiword entry) and geteilt ("geteilt durch").
- Size: 658 lexemes in total (math 250, science 408), above the 250–450 target. These additions
  are among the most typical subject terms of the units (Einmaleins, Zahlenstrahl, Stromkreis,
  Nahrungskette, Winterschlaf, Wasserkreislauf …). They count for more than the generic words cut
  in the first pass, so I kept them all and did not trim further without the orchestrator's go-ahead.

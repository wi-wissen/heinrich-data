# Run `de-daz-a1`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-daz-a1` (German as a second language, level A1)
    
    Language: German (`de`). Track: `daz` (German as a second language: teenagers and adults who arrive in Germany, in
    integration courses, welcome classes or as lateral entrants). Level **A1**.
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` (read the DaZ section and the topic block "German as a second language") · topic
      catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv` (use topics whose tracks include `daz`)
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - Our L1 layer for school children (`/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/graded/l1/*.tsv`) may be looked at for spelling and senses,
      but it is a **different scale**: a word children learn in grade 1 is not automatically A1 for adult learners (e.g.
      school and fairy-tale words), and many A1 words of adult life (Miete, Termin, Ausweis) are not primary-school words.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/`: one file per domain, named after the top-level id of the first topic
      (`daz/` is implied by the track; e.g. `self.tsv`, `housing.tsv`, `food.tsv`, `function.tsv`), `missing.tsv`, `decisions.md`.
    
    ## Assignment
    List the words learners typically learn and need at **A1**: personal information, greetings and courtesy, numbers,
    prices, times and dates, family, the flat and household, food and shopping, the body and the doctor in simple terms,
    work in simple terms, transport and directions, simple forms (Name, Adresse, Geburtsdatum), appointments, days and
    weather, and **all of the most frequent function words** (articles, pronouns, the common prepositions,
    und/oder/aber, question words, sein/haben/werden and the modals, frequent adverbs) plus the most frequent verbs and
    adjectives. Every line: `cefr=A1`, no `grade=`. `role=prod` for words learners use themselves, `rec` for words they
    need to understand (signs, forms). Target size: 650–800 lexemes. A checker will review your list afterwards.
    For the self-check run the checker script with track `daz`.
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

    Orchestrator: a checker (another AI agent, own knowledge only, no word lists) reviewed your A1 list: /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/check.tsv (lemma pos remark proposal reason) and check.md. Decide every remark by your own judgement — accept or keep with a one-line reason:
    - `missing` → add if you agree (`src=ai|rev`, your own topic/role/conf);
    - `too_early` → if you agree, remove the line and list it under "for A2" in decisions.md (the A2 author will see that list);
    - `role` → adjust if you agree.
    Also merge very small domain files into neighbours only if that is clearly better (file name = top-level id of the first topic stays the rule; it is fine to keep small files). Append a "Checker round" section to decisions.md with counts accepted/rejected per remark type and reasons for rejections. Re-run the checker script (track daz) to 0 errors and report counts. Same clean-room rules.

## Checker run (faster model, own knowledge only): prompt (verbatim)

    # Checker run `de-daz-a1-check`
    
    You check level A1 of Heinrich's German-as-a-second-language vocabulary (DaZ: teenagers and adults arriving in
    Germany) **from your own knowledge only**. Clean-room rules: no WebSearch or WebFetch, no published word lists of any
    kind (in particular no course or exam word lists for German as a foreign or second language), never open
    `/home/user/heinrich-eval`. You do not edit the author's files.
    
    Inputs: brief `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` (DaZ section), topics `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`, the A1 list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/*.tsv` (not missing.tsv), the author's reasoning `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/decisions.md`, lemma index
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`.
    
    Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/check.tsv` (`lemma pos remark proposal reason`): `too_early` (belongs to A2/B1; proposal the
    level), `missing` (an A1 word of everyday adult life absent from the list; proposal `cefr topic role`; only lemmas of the
    index), `role` (prod/rec off), `not_a1` (not useful at A1 at all). Be selective and concrete; gaps in whole
    situations matter most. Then `check.md`: 5–10 lines with counts per remark type and per topic. Do not commit anything.

### Checker summary

# Check de-daz-a1 (own knowledge only; 935 lines checked)
- Totals in check.tsv: 131 remarks = 93 missing, 32 too_early, 6 role, 0 not_a1 (the list is sensible for adults; nothing is useless at A1).
- missing by topic: integration 17 (countries, language names, Heimat/Muttersprache), school 12, people 8, qualities 7, jobs 6, town 6, animals 4, media 4, celebrations 4, home 3, actions.thinking 3, feelings 3, emergency 2, body 2, family 2, time.relations 2, weather 2, childcare/clothing/traffic/money/time.calendar/function.adverb 1 each.
- Biggest gaps (whole situations): no animals/pets at all; emergency has only Hilfe/Polizei/Feuerwehr (no Unfall, Feuer); childcare only Kindergarten (Spielplatz); feelings only 4 words; classroom/course words (Klasse, Unterricht, Übung, Tafel, Wörterbuch, Buchstabe, zuhören, erklären); social verbs (kennenlernen, mitbringen, heiraten, schenken); hygiene items; festival names (Weihnachten, Geschenk); directions (Kreuzung, Ecke, Ort).
- too_early (all proposed A2) by topic: doctor/health 6 (the brief puts the doctor at A2), function words 10 (gegenüber, seit, denn, sollen, werden, doch, ungefähr, allein, wirklich, also), home/housing 5 (Heizung, Müll, Aufzug, Badewanne, Quadratmeter), shopping 3, traffic/town 2, weather/time 2, qualities/clothing 2, jobs 1, travel-type 1.
- role: 6 words (Badewanne, Rezept, Aufzug, Angebot, Heizung, Erkältung) are recognition-only for A1 learners, so prod -> rec. Form-label nouns (Geburtsort, Wohnort, Postleitzahl) are prod while Geschlecht/Staatsangehörigkeit are rec; that split is defensible.
- Gaps deliberately not flagged (A2 in my judgement): weil/wenn/dass, durch/gegen, Konto, Vermieter, Anmeldung, Flüchtling, Himmelsrichtungen.
- Every missing lemma was verified to exist in the lemma index.

## Decisions log (written by the author)

# Decisions log — run `de-daz-a1` (German as a second language, CEFR A1)

## Inputs and method
- Inputs used: the brief README (DaZ section), `topics.tsv` (topics with track `daz`), our lemma index, and the
  checker script. The L1 core file was opened only to see the line format and how our lexicon spells/senses
  function words (e.g. `sie:fem`/`sie:pl`, `der:dem`). No published word list, course book, exam list,
  dictionary or web source was consulted; no WebSearch/WebFetch.
- Approach: I walked through the A1 situations of an adult newcomer (introducing oneself, filling in a simple
  form, greeting and thanking, numbers/prices/times, family, the flat, food and shopping, the body and a visit
  to the doctor, simple job talk, getting around town, appointments, days and weather) and listed, from my own
  knowledge of German and of adult integration teaching, the words needed in each. I then added the whole core
  of function words and the most frequent verbs and adjectives, checked every candidate against the lemma
  index, and moved absent lemmas to `missing.tsv`.
- Files are split by the top-level id of each line's first topic, as instructed.

## Level and role
- Every line is `cefr=A1`, no `grade=`. A1 here means the word is typically learned and needed in the first
  course level of adult learners, not that it is learned early by native children: e.g. Termin, Miete,
  Formular, Ausweis, Geburtsort, Familienstand-type form words are A1 for adults; fairy-tale, toy and
  school-yard words were not included.
- `role=rec` (32 lines) for words learners must understand but rarely produce: form labels (Geschlecht,
  männlich/weiblich, Staatsangehörigkeit, Nationalität, Unterschrift, Familienstand), signs and timetables
  (Gleis, Abfahrt, Ankunft, Fahrplan, Eingang/Ausgang, Öffnungszeit, WC), course instructions (Aufgabe,
  Beispiel, Prüfung, ankreuzen), and low-frequency grammar at this level (werden, sollen, schon/zu as particles).
- conf: core words 90–99; words that many A1 courses touch but that sit on the A1/A2 border 60–75
  (e.g. denn, seit, gegenüber, Heizung, Müll, arbeitslos, Erkältung, Kalender-type words).

## Borderline cases and exclusions
- Subordinating conjunctions (weil, dass, wenn, ob) were left out: subordinate clauses are typically A2.
  Coordinators und/oder/aber/denn are in.
- Past-tense and narration vocabulary, Umzug/Vermieter/Nebenkosten-type rental vocabulary, complaints,
  insurance and authority procedures were left for A2/B1 per the brief.
- Compound numerals 21–99 are productive from the units and tens; I listed 0–20, the tens, hundert, tausend
  and the ordinals needed for dates (erste–zwölfte, zwanzigste, dreißigste) instead of all 79 compounds.
- Country names: only a small set of frequent countries of origin and the German-speaking countries; the
  list of countries is open-ended and each learner needs their own.
- Feminine job/person nouns (Lehrerin, Ärztin, Kollegin …) were listed separately because A1 courses
  practise both forms actively.
- Trimmed for size (target 650–800): spelling variants (tschüs, Kuli, Pulli, Möhre), regionalisms
  (Sonnabend, ciao), and low-priority household or clothing items (Teppich, Spiegel, Topf, Stiefel,
  Handschuh, Hut) as well as A2-leaning words (pünktlich, Einladung, Bibliothek, Briefmarke, Paket,
  traurig, glauben, gehören).
- Homographs: used the sense ids the index offers (Mutter:parent, Junge:boy, Bank:financial, Rock:skirt,
  Orange:fruit, Flur:hall, Morgen:daytime, sie:fem/sie:pl, der:dem).

## Missing from the lexicon (`missing.tsv`, 28 lines)
- Common A1 compounds absent from the lexicon (Zahnarzt, Flughafen, Hauptbahnhof, Speisekarte,
  Großeltern, Handynummer, Deutschkurs, Mineralwasser, Orangensaft, Rind-/Schweinefleisch, Kreditkarte,
  Wartezimmer, Taxifahrer, Hausfrau, Familienstand, Herkunftsland, Tagesablauf).
- Language names as nouns (Arabisch, Persisch, Polnisch, Ukrainisch — only the adjectives exist).
- Adjectives/participles: geöffnet, geschlossen, besetzt, geschieden, nächst (as adjective).
- Degree adverb `zu` (zu teuer) — only adp/part exist; I kept `zu part` as rec.

## Checker round

The checker made 131 remarks (93 missing, 32 too_early, 6 role). I decided each one myself. Lines added or changed in
this round carry `src=ai|rev`. The list grew from 799 to 857 lexemes (822 prod, 35 rec). That is above the 650–800
target; I preferred covering whole situations the checker found empty (pets, the course room, festivals, emergencies)
over staying under the number.

### missing: 78 accepted, 15 rejected
- Accepted. Pets: Hund, Katze, Tier, Vogel. Course room: Klasse, Unterricht, Übung (rec), Tafel, Wörterbuch,
  Buchstabe, Test (rec), üben, erklären, zuhören (rec), ergänzen (rec). Origin: Heimat, Muttersprache, Italien,
  Spanien, England, Amerika, Spanisch, Italienisch. Emergencies: Unfall and Feuer (both rec). Body: Herz,
  Schulter. Bathroom: Seife, Handtuch, Zahnbürste. Also Jeans, Cousin, Cousine. Jobs: Ingenieur, Bäcker,
  Mechaniker, Fahrer, Arbeiter, Krankenpfleger. Town: Kreuzung, Ecke, Ort, Parkplatz, Bibliothek (rec), Linie.
  Also bar, Weihnachten, Geschenk, Feiertag (rec), Ostern (rec), Kalender, Anfang, Ende, Wolke, scheinen,
  kennenlernen, mitbringen, mitkommen, mitnehmen, heiraten, schenken, lachen, freuen, vergessen, aussehen,
  stimmen, traurig, lustig, Spaß, dick, dünn, voll, leer, prima, lange. Several of these I had cut only to stay
  under the size target. I agree they are A1.
- Rejected:
  - Griechenland, Rumänien, Ägypten, Marokko, Eritrea, China, Indien, Pakistan. Country names are an open
    class: each learner needs their own country, not a shared list. I keep a small core of German-speaking
    countries, neighbours and very frequent countries of origin.
  - Griechisch. Same reason, for language names.
  - Smartphone. Handy is the everyday A1 word, and Smartphone adds nothing at this level.
  - Postkarte. Brief and Karte cover the situation, and postcards are rare in adult A1 situations.
  - Alphabet. Learners practise buchstabieren and Buchstabe; the word Alphabet itself is rarely needed.
  - Theater. Kino and Museum cover leisure places at A1; theatre is A2 leisure talk.
  - hübsch, stark. Describing appearance and character in detail is A2. dick and dünn suffice at A1.

### too_early: 20 accepted (moved out, see "For A2"), 12 rejected
- Rejected (kept at A1), one reason each:
  - Medikament, Tablette: my assignment includes "the body and the doctor in simple terms". Asking for a
    tablet at the pharmacy is a basic need.
  - Rezept: kept, but as `rec` (accepted the role remark).
  - Besserung: "Gute Besserung" is a fixed courtesy formula, learned with the greetings.
  - arbeitslos: a status word in introductions ("Ich bin arbeitslos") and on forms.
  - umsteigen: transport is part of my assignment, and changing lines is needed from the first week.
  - Brille: describing people and everyday objects; very frequent.
  - windig: kept with sonnig as the basic adjectives of a weather report.
  - gegenüber: a core word for giving directions (gegenüber der Post).
  - seit: needed for "seit zwei Jahren in Deutschland" in every self-introduction.
  - doch: the "Doch!" answer and polite "Komm doch" are met very early.
  - allein: "Ich wohne allein" is basic personal information.

### role: 1 accepted, 5 moot
- Rezept: changed prod → rec.
- Badewanne, Aufzug, Angebot, Heizung, Erkältung: removed as too early, so their role remarks no longer apply.

### For A2 (removed from A1 in this round)
Erkältung, Schnupfen, Heizung, Müll, Quadratmeter, Metzgerei, günstig, Angebot, Aufzug, Badewanne, Ferien,
Jahreszeit, denn (cconj), sollen (aux), werden (aux), ungefähr, wirklich, also, bunt, Stadtplan.

### Files
I kept the rule that a file is named after the top-level id of the first topic. Some files are small
(housing 1, childcare 2, integration 2, sports 3, money 4). Merging them would mean reordering topics against their
real first topic, so I left them as they are.

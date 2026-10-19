# Run `de-daz-a2`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-daz-a2` (German as a second language, level A1)
    
    Language: German (`de`). Track: `daz` (German as a second language: teenagers and adults who arrive in Germany, in
    integration courses, welcome classes or as lateral entrants). Level **A2** (sequential: A1 is finished).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` (read the DaZ section and the topic block "German as a second language") · topic
      catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv` (use topics whose tracks include `daz`)
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - Our L1 layer for school children (`/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/de/graded/l1/*.tsv`) may be looked at for spelling and senses,
      but it is a **different scale**: a word children learn in grade 1 is not automatically A1 for adult learners (e.g.
      school and fairy-tale words), and many A1 words of adult life (Miete, Termin, Ausweis) are not primary-school words.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a2/`: one file per domain, named after the top-level id of the first topic
      (`daz/` is implied by the track; e.g. `self.tsv`, `housing.tsv`, `food.tsv`, `function.tsv`), `missing.tsv`, `decisions.md`.
    
    ## Assignment
    **Already learned at A1** (finished): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/*.tsv` (not missing.tsv/check.tsv). Read it first and do not repeat
    any of these words. Hints (not a must): the "For A2" list in the "Checker round" section of `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/decisions.md`.
    
    List the words learners typically add at **A2**: routine situations in more detail — appointments and phone calls,
    the doctor and pharmacy, finding and renting a flat (ads, contract, deposit, neighbours), work and job search in simple
    terms (application, CV, shift, salary), shopping and complaints, banks and post, authorities and forms
    (Anmeldung, Antrag), children's school and kindergarten, public transport and travel, leisure and invitations,
    health and the body in more detail, describing people and past events (Perfekt verbs), weather and seasons, feelings
    and opinions in simple terms, and the function words of A2 (weil, dass, wenn, ob, deshalb, trotzdem, seit, während …).
    Every line: `cefr=A2`, no `grade=`. Target size: 1,100–1,400 lexemes. A checker will review your list afterwards.
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

## Checker run (faster model, own knowledge only): prompt (verbatim)

    # Checker run `de-daz-a2-check`
    
    You check level A2 of Heinrich's German-as-a-second-language vocabulary (DaZ: teenagers and adults arriving in
    Germany) **from your own knowledge only**. Clean-room rules: no WebSearch or WebFetch, no published word lists of any
    kind (in particular no course or exam word lists for German as a foreign or second language), never open
    `/home/user/heinrich-eval`. You do not edit the author's files.
    
    Already learned at A1 (finished): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a1/*.tsv` (not missing/check files).
    Inputs: brief `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` (DaZ section), topics `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`, the A2 list
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a2/*.tsv` (not missing.tsv), the author's reasoning `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a2/decisions.md`, lemma index
    `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`.
    
    Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-daz-a2/check.tsv` (`lemma pos remark proposal reason`): `too_early` (belongs to B1 or later; proposal the level), `too_late` (belongs to A1, which lacks it), `missing` (an A2 word of everyday adult life absent from this list and from A1; proposal `cefr topic role`; only lemmas of the
    index), `role` (prod/rec off), `not_a2` (not useful at A2 at all). Be selective and concrete; gaps in whole
    situations matter most. Then `check.md`: 5–10 lines with counts per remark type and per topic. Do not commit anything.

### Checker summary

# Check of de-daz-a2 (from own knowledge; A1 list and lemma index used for comparison)
- Counts in check.tsv: missing 144, too_early 88, not_a2 28, role 8 (all proposed rec), too_late 2. Total 270 remarks on 1,232 lexemes plus gaps.
- missing by topic: actions 27 (frequent Perfekt/office verbs: nennen, anbieten, annehmen, abnehmen, bedeuten, versuchen, verwenden), traffic 13, home 13, qualities 12, authorities 10, function 10 (kaum, zwar, falls, sobald, solange, sodass, weniger), shopping 7, doctor 6, housing 6, clothing 6, time 5, emergency 4, rest 1-3 each.
- too_early (B1) by topic: function 18 (wo- compounds, entweder, erstens/zweitens, sowieso, schließlich, obwohl/trotz/seitdem/nachdem), integration 10, actions 9, qualities 8, workplace 7, banking 4 (Zinsen, Kredit, Schulden, brutto/netto), thinking 4, authorities 4; abstract nouns (Vergangenheit, Tradition, Qualität, Beziehung) throughout.
- not_a2: 28, mostly rare foods (food 12), rare body and family words, farm animals; role: forms and letter words (Kündigung, Behörde, Bescheid, Reklamation, Schwangerschaft, Kredit) should be rec.
- too_late: only Zuhause/zuhause belong to A1.
- Whole-situation gaps: the lexicon lacks the key compounds, so doctor (Kopfschmerzen, Hausarzt, Krankenwagen), offices (Personalausweis, Aufenthaltserlaubnis, Wartenummer), job search (Lebenslauf, Vorstellungsgespräch), rental (Mietvertrag, Nebenkosten) and bank (Bargeld, Girokonto) stay thin; nothing more can be done until the index grows (author's missing.tsv already lists them).
- Missing proposals are only lemmas present in the index; compounds absent from the index are not listed.
- Overall the list is sound at A2; the main fix is moving the abstract B1 layer out and adding the everyday verbs/adverbs above.

## Decisions log (written by the author)

# Decisions log — run `de-daz-a2` (German as a second language, CEFR A2)

## Inputs and method
- Inputs used: the brief README (DaZ section), `topics.tsv` (topics with track `daz`), our lemma index, the finished
  A1 run (`de-daz-a1/*.tsv` and its decisions log, to avoid repeats and to pick up its "For A2" list) and the checker
  script. No published word list (no course-book, exam, integration-course or CEFR list), no dictionary and no web
  source was consulted; no WebSearch/WebFetch. The L1 layer was not needed and not opened.
- Approach: I walked through the A2 situations of an adult newcomer who has finished A1: making, cancelling and moving
  appointments, phone calls and messages; the doctor, symptoms and the pharmacy; flat ads, viewing, the rental contract,
  deposit, service charges, house rules, neighbours, moving house; job search, application, CV, shifts, wages and the
  workplace; shopping, offers, returns and complaints; the bank, payments and the post office; authorities, registration
  and applications; the children's daycare and school; public transport, the car and travel; leisure, clubs, invitations
  and festivals; describing people (appearance, character), feelings, the weather and seasons; telling past events
  (the Perfekt verbs of daily routine, motion, handling and communication). For each I listed the words from my own
  knowledge, then added the A2 function words (subordinators, connecting adverbs, pronominal adverbs, more prepositions
  and particles). A small script checked every candidate against the lemma index and the A1 list and wrote the files,
  one per top-level id of the line's first topic.

## Level, role, confidence
- Every line is `cefr=A2`, no `grade=`. 1,233 lexemes, 1,209 prod / 24 rec.
- `role=rec` for words learners meet on forms, letters and signs but rarely produce at A2: Frist, Probezeit, brutto/netto,
  Zinsen, Dauerauftrag, Haftpflichtversicherung, Aufenthaltstitel, Wohnsitz, Meldebescheinigung, Elterngeld, Wohngeld,
  Sozialamt, Asyl, Einschreiben, Verbot, Umleitung, Anschluss, Diebstahl, verschreiben, zuordnen,
  innerhalb/außerhalb, werktags, Hinweis, the relative pronoun `der:rel`.
- conf: core A2 words 85–97 (weil, dass, deshalb, erzählen, Vermieter, Bewerbung, Erkältung, Heizung, Angebot);
  most situational words 65–80; words on the A2/B1 border 55–60 (obwohl, seitdem, trotz, Behandlung, Betreuung,
  specialised job names, Kredit, Standesamt-type office names, rarer foods and clothes).

## Borderline cases
- Taken over from the A1 "For A2" list: Erkältung, Schnupfen, Heizung, Müll, Quadratmeter, Metzgerei, günstig,
  Angebot, Aufzug, Badewanne, Ferien, Jahreszeit, denn (cconj), sollen, werden, ungefähr, wirklich, also, bunt,
  Stadtplan. All are in this run.
- obwohl, trotz, seitdem, während, nachdem: subordinate and concessive structures are usually consolidated at B1, but
  they are introduced at A2, so I kept them with conf 55–70.
- Country and language names were not extended (open class, as in A1).
- Smartphone (rejected at A1) is in at A2: digital devices and apps are part of A2 everyday talk.
- Homographs: hängen with both senses (transitive/intransitive, the stellen/stehen pairs of A2); übersetzen:translate,
  überlegen:think, schaffen:manage, Teil:portion, Steuer:tax, Schild:sign, Zoll:customs, See:lake, Gehalt:salary,
  Hut:hat, Bauer:farmer, Bar:pub, Gefallen:favor, Plastik:plastic.
- Adverbial words that the lexicon lists only as adjectives were entered with the lexicon's part of speech
  (wirklich, plötzlich, wahrscheinlich, sicher adj); zweimal/dreimal as num, selbst/selber as adv, gar as part.
- Feminine forms were listed where they matter in A2 situations (Vermieterin, Patientin, Kundin, Erzieherin,
  Teilnehmerin, Sachbearbeiterin …), not systematically for every job.
- Left out as B1 or later: abstract society and politics words (Regierung, Gesetz, Wahl), argumentation vocabulary
  (jedoch, allerdings, nämlich, Voraussetzung), contract and insurance detail beyond the basics, and rarer
  household/clothing items.

## Missing from the lexicon (`missing.tsv`, 141 lines)
- Most gaps are everyday compounds central to A2 situations: rental (Nebenkosten, Mietvertrag, Warm-/Kaltmiete,
  Hausordnung, Wohngemeinschaft), jobs (Lebenslauf, Vorstellungsgespräch, Teilzeit, Arbeitsvertrag, Stundenlohn),
  doctor (Hausarzt, Kinderarzt, Krankenwagen, Notfall, Notruf, Kopf-/Hals-/Bauchschmerzen), offices (Personalausweis,
  Reisepass, Bürgeramt, Ausländerbehörde, Aufenthaltserlaubnis, Wartenummer), bank (Bargeld, Kleingeld, Trinkgeld,
  Kontonummer, Girokonto, EC-Karte), household and clothing compounds (Schreibtisch, Briefkasten, Regenschirm,
  Rucksack, Handtasche), Führerschein, Motorrad, Reisebüro, Einzel-/Doppelzimmer, Integrationskurs, Sprachkurs.
- Senses: Tor needs a 'goal' sense. Participle adjectives absent: verletzt, getrennt, verboten, geboren, gestreift,
  möbliert. Verbs: staubsaugen, kaputtgehen, wohlfühlen.
- Because of these gaps the doctor, job_search, banking and authorities files are smaller than the situations warrant;
  they should grow once the lexicon adds the compounds.

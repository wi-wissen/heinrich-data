# Run `de-l1-subjects-b-1-4`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-l1-subjects-b-1-4`
    
    Language: German (lexicon language `de`). Track: `l1` (German as a first language).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`
    - Lemma index of our lexicon (columns lemma, pos, sense, file): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - `grade=` is required; leave out `cefr=`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-l1-subjects-b-1-4/` (write your .tsv files, `missing.tsv`, `decisions.md` there)
    
    ## Assignment
    
    Areas `history`, `geography`, `politics` (incl. economy), `religion_ethics`, `arts_music`, `sports`, `computing` and `language` (terms of German lessons), bands **1-2 and 3-4**. Output files: `history.tsv`, `geography.tsv`, `politics.tsv`, `religion_ethics.tsv`, `arts_music.tsv`, `sports.tsv`, `computing.tsv`, `language.tsv` (economy terms go to `politics.tsv` with `economy.*` topics).
    Include the subject terms of grades 1-4 (then and now, local history, maps and orientation, home region, rules and class council, festivals and stories of religions, colours/techniques/instruments/songs, running/jumping/ball games/swimming, devices and internet safety, letters/syllables/parts of speech/sentence parts/text types as German primary schools name them). Use `role=rec` for terms pupils mainly understand. Target size: 300–500 lexemes.
    
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

# Decisions log – author run de-l1-subjects-b-1-4 (L1, subject areas B, bands 1-2 and 3-4)

## Inputs and method
- Inputs used: the brief README.md, topics.tsv, the lemma index of our lexicon, and (once) our own
  noun/verb lexicon files to see how the homographs `Tor` and `bewegen` are split. No word lists, no web,
  no dictionaries, nothing under heinrich-eval, no other author run's output.
- I went area by area (history, geography, politics/economy, religion/ethics, arts/music/drama, sports,
  computing, German-lesson terms) and, for each topic id, imagined the primary-school lessons named in the
  brief (then and now, local history, maps and orientation, home region, class council, festivals and
  stories of religions, colours/techniques/instruments/songs, running/jumping/ball games/swimming,
  devices and internet safety, letters/syllables/parts of speech/sentence parts/text types) and wrote down
  the words pupils meet there, from my own knowledge.
- First draft: about 1,500 candidates. Checked against the lemma index; 368 candidates are not in our
  lexicon (mostly compounds typical of primary school: Wortart, Satzzeichen, Fragezeichen, Selbstlaut,
  Schwimmbrille, Völkerball, Stadtplan, Gottesdienst, Wasserfarbe ...). They went to `missing.tsv`, not
  into the files.
- Second step, cutting to the 300–500 target: the untrimmed checked list had about 1,100 lexemes. I
  removed (a) everyday vocabulary that the `core` runs cover anyway (gut, helfen, malen, Schere, Ball
  verbs like laufen/werfen, Geld, Buch, lesen, Wald, Fluss, links/rechts ...), (b) duplicates across
  files (each lemma kept in the one area where it is most at home, e.g. Meinung in politics, Strophe in
  both music and language because both lessons use it in different ways, Quelle in history only), and
  (c) low-value or late items (rare instruments, art-history words, four-case names kept but marked rec).
  Result: 500 lines.

## Bands
- 1-2 only for terms that are clearly worked with in grades 1-2: letters/sounds/syllables/rhyme, Einzahl/
  Mehrzahl, Artikel/Begleiter, the Christian festivals and their figures, basic instruments, gymnastics
  apparatus, swimming basics, first devices (Computer, Handy, Tablet), Ritter/Burg/Schloss.
- Everything that the brief places in 3-4 (maps, home region, Germany, class council, parts of speech
  with Latin names, tenses, sentence parts, text types, internet and safety, other religions) is 3-4.
- History and politics as such start in 3-4 general studies, so almost all those terms are 3-4.

## Role and confidence
- `role=rec` for terms pupils mostly meet in teacher talk or texts and do not yet write themselves:
  Jahrtausend, Generation, Ausgrabung, Demokratie, Regierung, Gesetz, Minderheit, Kompromiss, Datenschutz,
  Nominativ/Genitiv/Dativ/Akkusativ, Gewissen, Vergebung, Rabbiner, Imam, etc.
- conf 85–95 for unmistakable early terms, 70–80 for typical 3-4 subject terms, 55–65 for borderline ones
  whose introduction depends strongly on the state or teacher (cases, Kompromiss, Rabbiner, Gemeinderat).

## Borderline cases
- `Tor` (goal): the lexicon has `Tor:gate` (neuter) and `Tor:fool`; the football goal is the neuter noun
  with identical forms, so I used `Tor:gate`. A separate "goal" sense might be worth adding.
- `bewegen:move` (not :induce); `Ton:clay` in art.techniques, `Ton:sound` in music.theory; `See:lake`,
  `Bank:financial` were considered — See was dropped later as core, Bank:financial kept in economy.
- `Nordsee`, `Arktis`, `Nikolaus` are nouns in our lexicon, `Olympia` a proper noun; I followed the index.
- Partizipial adjectives (erlaubt, verboten, vergangen, bestimmt, erschöpft) are not separate adjective
  lemmas; listed in missing.tsv rather than invented.
- Old school names for parts of speech (Namenwort, Tunwort, Wiewort, Fürwort ...) and sentence-part names
  (Satzgegenstand, Satzaussage) are missing from the lexicon; Begleiter is present and kept.

## Left out
- Function words: none added in these subject files — the core runs cover them for bands 1-2 and 3-4;
  only the temporal adverb `damals` (history.method) is here. `früher` (adverb) is missing in the lexicon.
- Core everyday words (see above), sports equipment that is general play vocabulary (Fahrrad, Roller,
  Schlitten), fairy-tale figures (Hexe, Riese, Zwerg), and federal-state/city names beyond Berlin.

## Revision (follow-up: lexicon entries now available)
- `now_available.tsv` listed 349 rows of my missing list as now present in the regenerated index. I judged
  each one as in the original run; band, topic, role and confidence come from my original draft judgement
  for that word (written before the lexicon check), unchanged.
- Added 279 lexemes: history 19, geography 24, politics 18, religion_ethics 24, arts_music 38, sports 50,
  computing 9, language 97. Most are the primary-school compounds that carry these subjects (Wortart,
  Satzzeichen, Fragezeichen, Selbstlaut/Mitlaut, Silbenbogen, Umstellprobe, Aussagesatz, Wortfamilie,
  Bildergeschichte, Steckbrief, Klassenrat, Kinderrecht, Stadtplan, Windrose, Gottesdienst, Zuckerfest,
  Wasserfarbe, Grundfarbe, Blockflöte, Völkerball, Schwimmabzeichen, Purzelbaum, Passwort-related terms ...),
  plus `früher` (adv, 1-2), `vergangen`, `bestimmt`, `unentschieden`, `rücksichtsvoll`, `auswendig`.
- Senses: `Nordpol:geo`, `Südpol:geo`, `Pantomime:art` (the art form, not the performer).
- Not added although now available (70): I applied the same trimming rule as in the first run, so I left out
  everyday or core words (Handtuch, Postkarte, Einkaufsliste, Geldbeutel, Feiertag, Radfahren ...), spelling
  doublets and rarer variants (Xylophon next to Xylofon, Tuwort/Hauptwort/Zeitwort next to Tunwort/Namenwort,
  Wachsmalkreide), and marginal items (Stillleben, Staffelei, Akrostichon, Rondell, Ich-Erzähler,
  Startblock, Platzverweis, Kostenfalle, Lautgebärde, Silbenkönig ...). These were removed from
  missing.tsv as they are no longer missing.
- missing.tsv now has 19 rows: lemmas still absent (noun readings Aufwärmen, Fasten, Kraulen, Reiten,
  Schwimmen, Tanzen; Ringe; Klanghölzer; seilspringen; participle adjectives erlaubt, verboten, erschöpft;
  proper names Maria, Mose, Noah, Mohammed, Sankt Martin) and großschreiben/kleinschreiben, which will not
  be added; their content is covered by Großschreibung/Kleinschreibung. I fixed a malformed `Sankt Martin` row.
- Size: 779 lexemes now, above the 300–500 target. The extra rows are almost all core subject terms that
  were missing only because the lexicon lacked them; I chose not to cut original rows again to compensate.
  If the target is strict, the best cuts are the 3-4 language grammar/old-name doublets and sports equipment.

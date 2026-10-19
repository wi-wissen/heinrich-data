# Run `de-seam`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `de-seam` (band seams, own frequency signal)
    
    Language: German (`de`). Track: `l1`.
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/de/graded/topics.tsv`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/de_lemmas.tsv`
    - The merged layer so far (bands 1-2 and 3-4, all areas): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/merged/de/l1/*.tsv` — read it to see what is already there.
    - Input: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-seam/gaps.tsv` (columns rank, lemma, pos(s)): lemmas among the 3,000 most frequent forms of **our own** frequency list that the layer does not contain yet. This list is our own data, derived only from our counts and our lexicon.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/de-seam/`: `core.tsv` (and subject-area files with the same names as in the merged layer if a gap word is clearly a subject term), `later.tsv`, `decisions.md`.
    
    ## Assignment
    
    Several authors wrote bands 1-2 and 3-4 in parallel; at the seam between them, words fell through because each assumed the other had them. Go through every gap word and decide from your own knowledge:
    - introduced in **1-2** or **3-4** → write a normal line (`src=ai|freq`, topic, role, conf) into `core.tsv` (or the subject file);
    - introduced only in **5-6 or later**, or not school vocabulary at all (administrative, parliamentary, legal jargon, old spelling such as `daß`) → one line in `later.tsv`: `lemma pos band-or-none short reason` (no layer entry now; later bands are authored later).
    Frequency alone is not a reason for an early band: a word frequent in parliamentary or legal texts may still be learned late. Decide by when children typically learn and use the word. Pick the right part of speech when the index lists several (e.g. an adverb and a particle reading); you may add several lines for different parts of speech.
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

## Decisions log (written by the author)

# de-seam – decisions log (L1 German, seam between bands 1-2 and 3-4)

## Inputs and approach
- Inputs used: the graded README and topics.tsv, our lemma index, the merged layer (to see what exists),
  and `gaps.tsv` (our own frequency ranks of lemmas missing from the layer). No word list, dictionary,
  web source or held-out set was consulted.
- Every one of the 724 gap lemmas was judged individually from my own knowledge of how primary-school
  children speak, read and write. Frequency only selected the candidates; it never decided the band.
  Words frequent because of parliamentary minutes, legal texts, encyclopaedic or sports reporting
  (Sitzung, Fraktion, Verordnung, gemäß, Maßnahme, Legislaturperiode, Antragsteller …) went to `later.tsv`.
- Layer entries carry `src=ai|freq` (author judgement, candidate surfaced by our frequency signal).
- Result: 213 layer lines (core 200, subject files 9), 538 lines in `later.tsv`
  (5-6: 205, 7-8: 189, 9-10: 123, 11-13: 1, none: 20).

## Band criteria
- **1-2:** words children use themselves when talking about family, home, school, play, fairy tales:
  kinship (Sohn, Tochter), everyday places (Bahnhof, Park, Post, Brücke, Turm, Hof), feelings (Lust, Liebe,
  Traum, gefallen), core verbs (bleiben, lassen, beginnen, versuchen, sterben, stimmen, fehlen, zahlen),
  frequent pronominal/directional adverbs used in speech (davon, darauf, dahin, herum, vorbei),
  aufs, los ("Was ist los?"), Prinz and Geist from stories.
- **3-4:** the widened world of the README: jobs of adults (Firma, Kollegin, Fischer, Schneider,
  Architekt, Zimmermann, Meister), town and traffic (Zentrum, Eingang, Fahrzeug, Halle), media
  (Serie, Zeitschrift, Album), school routines (Thema, Prüfung, prüfen, einsetzen, Mühe, Partner, AG,
  the grade word ausreichend), the remaining pronominal adverbs (darüber, daran, darin, daraus, darunter,
  dagegen), quantifiers (einige, wenige), modal particles children use (bloß; wohl/eben only rec).
  Formal "Ihr" as determiner gets 3-4 because letter writing starts there.
- **later.tsv 5-6:** general school language and abstract nouns (Begriff, Abschnitt, Zusammenhang,
  Möglichkeit, Situation), written connectors (jedoch, allerdings, zwar, indem, sowie), formal verbs
  (erhalten, befinden, enthalten, bestehen), history/geography starters (Volk, Reich, Armee, Bevölkerung).
- **later.tsv 7-8 / 9-10:** argumentative and administrative vocabulary, politics and economy
  (Partei, Parlament, Wirtschaft, Unternehmen at 7-8; Koalition, Grundgesetz, Behörde, Finanzierung at 9-10).
- **none:** old spelling (daß), abbreviations (FC, GmbH, ISBN), administrative jargon with no school use
  (Maßgabe, Einvernehmen, Erteilung, Eintragung, Bekanntmachung, Übermittlung, Antragsteller,
  unverzüglich, Verordnung), dated or pejorative words (Fräulein, Weib), regional colloquial langen,
  rare adjectival participles (gewesen, geworden), Hochstift, the ethnonym sense of Rom.

## Parts of speech and senses
- Several readings were split: eben (adv 1-2, particle 3-4 rec, adj → later 5-6); bloß (particle 3-4,
  adj → later); Ihr det 3-4 prod, pron 3-4 rec; einige/wenige both det and pron at 3-4.
- Senses: Teil:piece 1-2 / Teil:portion 3-4; schaffen:manage 1-2 / schaffen:create later; Leiter:ladder
  1-2 / Leiter:person 3-4; Band:ribbon 3-4, other Band senses later; Steuer:wheel 3-4 rec, Steuer:tax
  later; Halle:building 3-4; all Mark and Bund senses later.
- Subject files: Komponist (arts_music, music.history), Bischof (religion_ethics), Region (geography,
  rec), ergeben and Spalte (math), durchführen and feststellen (science.method, as used for experiments
  in general studies), Finale and Meisterschaft (sports).

## Borderline cases (conf 55–65)
AG (ambiguous with the company form; school-club reading dominates for children), irgend, fort, rein,
Gegensatz, vermutlich, Universität, Professor, Journalist, Mitarbeiter, Teufel, nutzen, verwenden,
erfüllen, Steuer:wheel, Region. Kept rec where children mainly meet them in texts.
Left later despite some early contact: Präsident (news, but taught in politics 5-6), Prozent (maths
after primary), Graf/Gräfin (fairy tales mention them, but history teaches them), Gelegenheit, Position,
Saison, Kampf, Schlacht, Ehe, Pflege.

## Missing / sense splits (missing.tsv, 2 lines)
- Gericht: the dish sense is early vocabulary, the court sense late; without a sense split the lemma
  was placed by its later sense in `later.tsv`.
- Verband: bandage (first aid, early) vs. association (late); same treatment.
Other unsplit polysemous nouns (Vorstellung, Aussprache, Berliner, Wiener, Gang) were put in
`later.tsv` by their dominant later reading; a sense split could move one reading earlier.

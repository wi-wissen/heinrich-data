# Run `en-seam`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-seam` (band seams, own frequency signal)
    
    Language: English (`en`). Track: `efl` (English as a foreign language in German schools; English starts in grade 3). `grade=` and `cefr=` are required (3-4 → A1; 5-6 → A1/A2; 7-8 → A2, some B1).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - The merged layer so far (bands 3-4, 5-6 and 7-8): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/merged/en/efl/*.tsv` — read it to see what is already there.
    - Input: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-seam/gaps.tsv` (columns rank, lemma, pos(s)): lemmas among the 3,000 most frequent forms of **our own** frequency list that the layer does not contain yet. This list is our own data, derived only from our counts and our lexicon.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-seam/`: one file per top-level topic id of the first topic, same names as in the merged layer, `later.tsv`, `decisions.md`.
    
    ## Assignment
    
    Several authors wrote bands 3-4, 5-6 and 7-8 in parallel; at the seam between them, words fell through because each assumed the other had them. Go through every gap word and decide from your own knowledge:
    - introduced in **3-4**, **5-6** or **7-8** → write a normal line (`src=ai|freq`, grade, cefr, topic, role, conf) into the topic file;
    - introduced only in **9-10 or later**, or not school vocabulary at all (administrative, parliamentary, legal jargon, government or statistics jargon) → one line in `later.tsv`: `lemma pos band-or-none short reason` (no layer entry now; later bands are authored later).
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

# Decisions log: author run `en-seam` (English, EFL track)

## Approach

- Inputs used: the brief `README.md`, `topics.tsv`, our lemma index `en_lemmas.tsv`, the merged layer
  (bands 3-4, 5-6, 7-8) and `gaps.tsv`. No published word list, no dictionary, no web access, nothing
  under the evaluation repository was opened. All judgements come from my own knowledge of English and
  of English lessons in German schools.
- I first checked every gap lemma against the index (parts of speech, senses) and against the merged
  layer. None of the 640 gap lemmas had any entry in the merged layer under any part of speech.
- Then I went through every gap lemma and every part of speech the gap list names (some with
  several) and made one decision per lemma+pos: an entry for band 3-4, 5-6 or 7-8, or a line in
  `later.tsv` with band 9-10, 11-13 or `none`.
- Guiding question: "When does a German pupil in English lessons first meet and need this word, in
  this part of speech?" Frequency in our corpus was not a reason on its own: the gap list is dominated
  by administrative, legal, parliamentary, statistical and economic vocabulary (provision, accordance,
  census, subsection, compliance, pursuant, constituency ...), which went to `none` or to a late band.

## Bands and levels

- 3-4 / A1: only words that belong to the core of primary English (thing, question as a noun, fire).
- 5-6 / A1-A2: concrete everyday nouns and classroom words that the topic list of 5-6 needs
  (information, website, video, radio, transport, railway, camp, tour, store, bill, gold, silver,
  wood, earth, air, sight(s), unit, title, meaning, writing, reading, Latin as a school subject),
  some function words (cannot, till, even as an adverb, forward as an adverb) and frequent task-
  instruction verbs (design, sort, raise one's hand, type).
- 7-8 / A2-B1: words for the 7-8 themes (media, jobs, health, environment, other English-speaking
  places, stories): power, global, system, safety, product, event, meeting, university, college,
  county, mayor, minister, nationality adjectives (African, Indian, Asian, Russian, Japanese, Greek,
  Dutch), fashion, style, studio, award, league, penalty, Olympic, kill, evil, grave, crew, setting.
  Most of these are `role=rec` because pupils mainly need to understand them at that stage.
- 9-10 and 11-13 (later.tsv): abstract B1/B2 nouns and verbs, argument and text-analysis words,
  politics, economy, law and history vocabulary, formal adverbs (subsequently, respectively, merely).
- `none`: legal, administrative, parliamentary and statistics jargon, abbreviations (para, reg, CDP,
  LLC, VAT), rare verb conversions (case, war, gas, captain, crew, shore ... as verbs), and archaic or
  rare senses (fell, worst as a verb, ring in the "encircle" sense).
- CEFR: 3-4 → A1; 5-6 → A1 or A2; 7-8 → A2 for concrete words, B1 for more abstract ones.
- `src=ai|freq` on every entry, as the run prompt asks (the lemma came from our own frequency signal,
  the band decision is my own).

## Parts of speech and senses

- Noun/verb pairs were split: often the noun is early and the verb late (fire, question, store,
  bill, power, transport, radio, video), sometimes both are early (land, camp, clear, iron, heat).
- Nationality words: adjective and noun both entered at 7-8 (Chinese adjective at 5-6 because of
  food); religious and ethnic labels of US/UK society (Hispanic, Latino, Catholic, Jewish) went to 9-10,
  where those topics are dealt with; Roman to 5-6 (Romans in Britain is a common early topic).
- `lead`: the index has an undifferentiated noun and verb senses `guide` and `metal`; only
  `lead:guide verb` was entered (7-8, rec). `ring`: `ring:sound verb` at 5-6, `ring:encircle` to none.
- `found` exists only in the sense "establish" → 9-10 (history of colonies); the past tense of
  "find" is a form of "find", not this lemma.
- `toward` (US spelling) entered at 7-8 as receptive; `honor` and `labor` (US spellings) went later
  with their abstract meanings.

## Borderline cases (conf 50-60)

ground (verb, "grounded"), regard (noun, only "best regards" in letters), multiple ("multiple
choice"), opening ("opening hours"), limit ("speed limit"), resolution ("New Year's resolution"),
spot (verb, "spot the differences"), case (noun, "in case"), sudden ("all of a sudden"), upper,
expression ("useful expressions"), toward, aid ("first aid"). For each I picked the band of its most
child-relevant use and set low confidence. Words such as section, being, living, saying, education,
principal (US school head) and secondary were close calls between 7-8 and 9-10.

## Output

- 191 entries in 45 topic files (3 in band 3-4, 71 in 5-6, 117 in 7-8), covering 165 of the 640 gap
  lemmas; 677 lemma+pos lines in `later.tsv` (374 → 9-10, 195 → 11-13, 108 → none).
- Two topic files are new compared with the merged layer: `literature.tsv` (setting) and
  `politics.tsv` (vote, minister); they follow the same naming rule (top-level id of the first topic).
- `missing.tsv` is empty: every lemma and sense used exists in the index. The checker reports
  0 errors, 0 warnings.

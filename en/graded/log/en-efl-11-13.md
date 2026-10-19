# Run `en-efl-11-13`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-efl-11-13` (sequential: bands 3-4 to 9-10 are finished)
    
    Language: English (`en`). Track: `efl`. Band **11-13** (upper secondary up to the Abitur), levels **B2**, receptive **C1**
    (`role=rec` for words pupils mainly need to understand).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - **Already introduced** (bands 3-4 to 9-10, finished and merged): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/merged-en-3-10/*.tsv`. Read them first.
      Do not repeat any of these words.
    - Hints (our own data, not a must): the "for 11-13" list in the "Checker round" section of
      `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/decisions.md`, and the lines with band 11-13 in `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-seam/later.tsv`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-11-13/`: one file per top-level topic id of the first topic, `missing.tsv`, `decisions.md`.
    
    ## Assignment
    Cover every topic the README names for 11-13 (globalisation and migration, politics and democracy in the UK and the USA,
    ethics and science, post-colonial literature and the Commonwealth, media and manipulation, the American Dream, utopia
    and dystopia, analysing and interpreting literature and non-fiction, stylistic devices, argumentative writing) and lift
    every other topic to B2: abstract and academic vocabulary, formal linking words, words for analysis and evaluation.
    `cefr=B2` for the productive core, `C1` (mostly `rec`) for clearly advanced words. Target size: 2,000–3,000 lexemes.
    A checker will review your list afterwards and may send you concrete remarks.
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

    Orchestrator: a checker (another AI agent, own knowledge only, no word lists) reviewed your band: /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-11-13/check.tsv and check.md. Decide every remark by your own judgement — accept or keep with a one-line reason:
    - `missing` with band 11-13 → add (`src=ai|rev`, your own level/topic/role/conf).
    - `missing` with a lower band, and `too_early` that you accept → remove from your band files (if present) and write them into a separate file `lower.tsv` in your output directory, as normal graded lines with **your own** judgement of the right lower band (`grade=` 5-6, 7-8 or 9-10) and level, `src=ai|rev`. The lower bands are finished; the orchestrator merges `lower.tsv` directly (earliest band wins if a word already exists). Words you judge to be in 3-4 go there too.
    - `not_school` → remove if you agree.
    - `level` → adjust if you agree.
    Append a "Checker round" section to decisions.md (counts accepted/rejected per type, reasons for rejections). Re-run the checker script to 0 errors (include lower.tsv in the check) and report counts. Same clean-room rules.

## Checker run (faster model, own knowledge only): prompt (verbatim)

    # Checker run `en-efl-11-13-check`
    
    You check one band of Heinrich's English graded vocabulary (English as a foreign language in German schools)
    **from your own knowledge only**. Clean-room rules: no WebSearch or WebFetch, no published word lists of any kind,
    never open `/home/user/heinrich-eval`. You do not edit the author's files.
    
    Inputs:
    - Brief and band/CEFR guide: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md`; topics: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lower bands (already finished, merged): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/merged-en-3-10/*.tsv`
    - The band to check (band 11-13 (B2, receptive C1)): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-11-13/*.tsv` (not missing.tsv); the author's reasoning: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-11-13/decisions.md`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    
    Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-11-13/check.tsv` with one line per remark, columns
    `lemma pos remark proposal reason`:
    - `too_early` / `too_late`: the word belongs to another band (proposal: the band);
    - `level`: the CEFR level is off (proposal: the level);
    - `missing`: a word typically introduced in band 11-13 (B2, receptive C1) for one of the band's topics is absent from this band and from
      all lower bands (proposal: `grade cefr topic role`); only lemmas of the lemma index;
    - `not_school`: not school vocabulary at this stage.
    Be selective and concrete: remark only where you are fairly sure (no stylistic preferences). Aim at the gaps first:
    whole groups of common words missing for a topic matter most. Then write a 5–10 line summary (`check.md`) with
    counts per remark type and per topic. Do not commit anything.

### Checker summary

# Check of band 11-13 (en-efl-11-13)

Counts (check.tsv): too_early 93, too_late 0, level 12, not_school 108, missing 149.

Overall: coverage is very good. My probes of about 1,100 typical B2/Abitur words (topic words for globalisation, politics, ethics, media, utopia/dystopia, literary analysis, stylistic devices, law, history, economy, environment, plus general academic vocabulary) found only about 100 absent lemmas that exist in the lemma index; most gaps are isolated words, not whole groups. Spelling variants (rumour, ageing, offence, labour) and hyphenated compounds are not in the index and were not reported.
Missing per topic: thinking 18, politics 13, history 13, science 9, technology 8, society 7, qualities 6+, health 5, global 5, feelings 5, actions.change 5. About 40 "missing" items are earlier-band words absent from all lower bands (knowledge, marriage, strength, difficulty, poetry, universe, noun, verb, weapon, machine, error, instruction ...), proposed for 5-6 to 9-10; the rest are B2 words (nuance, erode, backlash, mobilize, trajectory, constraint, versatile, plight ...) and rec history/law terms (armistice, enlightenment, renaissance, embezzlement ...).
too_early (93): B1 words that belong to 9-10 or earlier: basic evaluative/feeling words (dreadful, amusing, disgust, enjoyment, optimism), general adjectives and adverbs (endless, unclear, surprising, newly, commonly), health basics (pregnancy, injection, dose, infant), history/story words (warrior, troop, tomb, peasant, servant), grammar terms (plural, continuous, irregular), UN, chancellor.
not_school (108): jargon of administration, finance and law (payroll, rebate, felony, plaintiff, subpoena, indictment, injunction), CLIL science terms (RNA, electron, oxide, wavelength), specialised military terms (battalion, cavalry, artillery), specialised medical terms, and archaic/legalese adverbs (heretofore, forthwith, thereof, perchance).
level (12): rhetoric, representation, consciousness, disparity, NGO, tariff, thereby, mercy, ethos, pathos are better B2 than C1 rec; therein and lest are better C1.
No too_late remarks: the band is not misplaced beyond the Abitur level apart from the not_school items.

## Decisions log (written by the author)

# Decisions log: author run `en-efl-11-13` (English, EFL, band 11-13, B2 with receptive C1)

## Inputs used
Only the brief (`en/graded/README.md`), `topics.tsv`, the lemma index of our own lexicon, our own frequency
list (`heinrich-data/en/frequency/forms.tsv`), the finished and merged lists of bands 3-4 to 9-10 (to exclude
words already introduced), and our own hint files (the "for 11-13" list in the 9-10 decisions log and the
11-13 lines of `en-seam/later.tsv`). No published word list, dictionary, course book, exam list or CEFR
profile was consulted; no web access was used; nothing under `heinrich-eval` was opened. All candidates and
all level/role/topic judgements come from my own knowledge of English and of upper-secondary English lessons
in Germany (Oberstufe up to the Abitur).

## Method
1. **Topic pass (from memory).** For every 11-13 topic of the brief I wrote candidate words per situation:
   globalisation and migration (outsourcing, remittances, asylum procedures, multicultural society);
   politics and democracy in the UK and the USA (constitution, checks and balances, Congress, elections,
   monarchy, devolution, Brexit, polarisation); ethics and science (genetic engineering, cloning, AI,
   euthanasia, research ethics); post-colonial literature and the Commonwealth; media and manipulation
   (spin, distortion, fact-checking, echo chambers, whistleblowers); the American Dream (self-reliance,
   upward mobility, disillusionment); utopia and dystopia (totalitarian control, surveillance,
   indoctrination, conformity); analysing literature and non-fiction (narrative perspective, plot
   structure, characterisation, connotation, ambiguity); stylistic devices; argumentative writing
   (claim, concession, rebuttal, fallacy, formal linkers). Also law, society/class/gender, history of empire
   and slavery, economy, environment at B2.
2. **General B2 lift.** To lift the general layers I went through the lemmas of our own lexicon that no
   band has yet, ordered by our own frequency list, in chunks of 600-1,300, and picked by my own judgement
   the abstract, academic, evaluative and formal words a B2/C1 learner needs (e.g. abstract nouns like
   implementation, prevalence, reluctance; verbs like undermine, alleviate, reconcile; adjectives for
   evaluation like robust, viable, detrimental; degree and linking adverbs). The frequency list served only
   to order what I reviewed; the decision for every word is my own. About 7,500 lexicon lemma entries were looked
   at this way; most were rejected (technical, administrative, regional, proper-name derived, or clearly
   earlier-band).
3. A script checked every candidate against the lemma index (exact spelling and POS) and against the merged
   lower bands: 1,097 candidate hits were already introduced in 3-4 to 9-10 and were dropped; duplicates
   within my list keep the first (most specific) topic.
4. Hand review: trimming of technical science/maths/IT words, demotion of literary and very formal words to
   C1 rec, topic fixes for linking/degree adverbs (`function.adverb|thinking`), then the checker until
   0 errors.

## Bands, levels, roles, confidence
- Everything is `grade=11-13`.
- `cefr=B2 role=prod` (2,304 lines) for the productive core: words pupils should use in analyses,
  comments, argumentative essays, mediation and discussions (e.g. legitimacy, polarize, sustainable,
  convey, implicit, nonetheless).
- `cefr=B2 role=rec` (188 lines) for B2 words met mainly in texts: legal and military terms, medical and
  natural-science terms (velocity, chronic, psychiatric, warrant, tribunal).
- `cefr=C1 role=rec` (341 lines) for clearly advanced words: literary/old-fashioned vocabulary from
  classic texts (forlorn, mirth, haughty, wretched, thou/thy/ye), very formal connectors and legal
  register (hitherto, henceforth, thereupon, aforementioned, forthwith, heed), specialised political
  and literary-theory terms (hegemony, prerogative, juxtaposition, connotation, diction).
- Confidence: 70 for B2 prod, 65 for B2 rec, 60 or lower for C1 and for borderline words (55 for words
  whose school relevance I am less sure of, 50 for archaic or legalese adverbs).
- Spelling: the lexicon uses US spellings; British variants (analyse, criticise, fulfil, centre, metre,
  offence, rumour, ageing) were mapped to the US lemma where it exists, and not listed as missing.

## Topic assignment
The first topic is the most specific area in which the word is taught. Text-analysis and argument
vocabulary goes to `thinking` (591 lines: abstract nouns, evaluative adjectives, adverbs of argument) and
`academic` (198: working with texts, data and sources); stylistic devices go to `language`, literary
analysis to `literature`. Generic evaluative and character adjectives use `qualities.judgement` /
`qualities.character`; verbs of change and process use `actions.change`. One file per top-level id of the
first topic. Small files (fantasy, school, transport with one word each) are kept as they are.

## Borderline cases and exclusions
- **Earlier-band gaps excluded.** Some words that no lower band has are clearly learned before 11-13; I did
  not list them here and leave them to the orchestrator: e.g. nasty, rotten, greedy, unfamiliar, unwell,
  untrue, unwanted, confusing, unpopular, playful, harmless, naked, dusty, everyday, textbook, millionaire,
  thunderstorm, weapon, poetry, hate (noun), flat (adj), stream, worldwide (adj), upload, desktop, setup,
  font, byte, reset; also basic nouns that occur in 11-13 expressions only as parts (bubble, filter, echo,
  drain).
- **Technical words dropped.** Maths, chemistry and IT terms that belong to CLIL or science subjects rather
  than to English lessons (integer, coefficient, isotope, polymer, oxidation, perpendicular, algebra,
  encryption-type IT terms, rare diseases) and administrative legal jargon (indemnity, forfeiture,
  appellant, writ, arrears).
- **Kept as B2 although frequent in our corpus:** formal words like provision, behalf, compliance,
  threshold, respectively; they are typical of the formal register pupils meet in non-fiction at 11-13.
- **Kept as C1 rec:** archaic pronouns thou/thy/thine/ye (Shakespeare and older poetry in the Abitur
  syllabus), median/subsection/accordance (statistics and legal texts used in mediation tasks).
- Multi-word expressions (American Dream, checks and balances, stream of consciousness, echo chamber,
  filter bubble, brain drain, melting pot, House of Commons, Jim Crow, civil rights movement) have no lemma
  in the lexicon; their parts were checked singly and fragments were not put into `missing.tsv`.
- Proper names whose lower-case lemma exists (Congress/congress, Senate/senate, Parliament/parliament,
  Crown/crown, Constitution/constitution) were not reported as missing.

## missing.tsv
320 lemmas I wanted but the lexicon lacks (or lacks in that part of speech), grouped by note:
- stylistic devices and literary terms: alliteration, hyperbole, euphemism, oxymoron, onomatopoeia,
  understatement, anaphora, assonance, enjambment, couplet, quatrain, pentameter, soliloquy, aside (noun),
  subplot, denouement, foreshadowing, antihero, epiphany, catharsis, bildungsroman, modernism, romanticism,
  postmodernism, intertextuality, ...;
- political, social and media terms: populism, plutocracy, totalitarianism, xenophobia, sexism,
  patriarchy, meritocracy, consumerism, multiculturalism, secularism, cyberbullying, clickbait, deepfake,
  dystopia (only dystopian exists), demagogue, gerrymandering, filibuster, suffragette, quango, ...;
- participial adjectives and -ing nouns (biased, marginalized, deprived, impoverished, polarized,
  globalized, devastated, lobbying, polling, trafficking, framing, ...);
- hyphenated compounds (left-wing, right-wing, working-class, self-made, self-reliant, first-person,
  coming-of-age, post-truth, law-abiding, narrow-minded, ...);
- formal function words (albeit, whereby, wherein, whereupon, provided/providing as conjunctions,
  notwithstanding, admittedly, whatsoever, unto, vis-à-vis, thee);
- proper names (Labour, Oxbridge, Windrush, Bollywood, Mandela, Gandhi, Raj, UNICEF, Maori, ...).
`missing_check.tsv` is the checker's output and is empty (0 missing members in the topic files).

## Checker round

I went through all 362 remarks in `check.tsv` and decided each one by my own judgement, without word
lists. Lines I added or changed carry `src=ai|rev`.

| remark type | accepted | kept / rejected |
|---|---|---|
| too_early | 91 | 2 |
| level | 12 | 0 |
| not_school | 100 | 8 |
| missing (band 11-13) | 98 | 0 |
| missing (lower band) | 51 | 0 |

- **too_early:** I agree that these are B1 words met by grade 10 (basic feeling and evaluation words, health
  basics, history and story words, grammar terms). They were removed from the band files and written to
  `lower.tsv` with the proposed band (A2 for 5-6, B1 for 7-8 and 9-10). The grammar terms plural,
  continuous and irregular got the topic `language`.
- **level:** all 12 accepted. rhetoric, representation and disparity are now B2 prod. consciousness, NGO,
  tariff, thereby, mercy, ethos and pathos are now B2 rec. therein and lest are now C1 rec.
- **not_school:** accepted for administrative, finance and court-procedure jargon, CLIL science terms,
  specialised military and medical terms, and archaic or legalese adverbs (100 lines removed).
- **missing, band 11-13:** all 98 added with the checker's level, topic and role (confidence 60-65). This
  includes encryption, parameter and peripheral, which I had dropped as too technical. In their general
  senses (privacy debate, "within the parameters", "peripheral role") they belong in the band.
- **missing, lower band:** all 51 written to `lower.tsv`. I set noun and verb (as grammar terms) to 5-6
  instead of the proposed 7-8: pupils name word classes from the start of secondary school. The other
  bands were taken as proposed.
- `lower.tsv` also takes the earlier-band gaps I had listed under exclusions, where the checker proposed
  them (nasty, greedy, unfamiliar, unwanted, naked, everyday, millionaire, worldwide, thunderstorm, poetry,
  weapon).

### Rejections and reasons
- too_early: alien (adj): the sense "foreign, strange" (an alien culture, ideas alien to them) is B2,
  unlike the noun; keep in 11-13.
- too_early: enable (verb): a formal verb of non-fiction and argument; our own hint file also places it in
  11-13; keep.
- not_school: parole (noun): prison and justice topics, and crime fiction read in class; keep as B2 rec.
- not_school: cocaine (noun): drugs and addiction are a social-problems topic; keep as B2 rec.
- not_school: malaria (noun): global health inequality is a globalisation topic; keep.
- not_school: frontline (noun): used figuratively in general texts (frontline workers, the frontline of
  the debate); keep.
- not_school: combustion (noun): combustion engines come up in environment and climate texts; keep as B2 rec.
- not_school: fission (noun): nuclear energy is an ethics-and-science and environment topic; keep as B2 rec.
- not_school: vacuum (noun): general and figurative use (a power vacuum, in a vacuum); keep.
- not_school: goodwill (noun): the general sense "friendly intention" is common in political and
  non-fiction texts; keep.

### Result after the round
The band files have 2,740 lines: 2,240 B2 prod, 212 B2 rec and 288 C1 rec. `lower.tsv` has 142 lines:
7 for 5-6, 29 for 7-8 and 106 for 9-10. The checker script reports 0 errors over the band files and
`lower.tsv`.

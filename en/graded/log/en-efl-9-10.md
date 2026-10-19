# Run `en-efl-9-10`

Author: an AI agent (identifier not recorded, CLAUDE.md rule 8; lexicon round 2 and checkers: the faster model, the rest: the stronger model). Date: 2026-10-19.

## Prompt (verbatim)

The agent received a one-line message pointing to this file, with the instruction to read it completely and follow it exactly (no web search or fetch, no published word lists, never open the held-out test repository).

    # Author run `en-efl-9-10` (sequential: the lower bands are finished)
    
    Language: English (`en`). Track: `efl`. Band **9-10**, level **B1** (some B2; end of lower secondary).
    - Brief: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md` · topic catalogue: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    - **Already introduced** (bands 3-4, 5-6, 7-8, finished): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/graded/efl/*.tsv`. Read them first. Do not repeat
      any of these words; your list contains only words typically **introduced in grades 9-10**.
    - Words already judged "later" by an earlier author (our own data, a hint, not a must): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-seam/later.tsv`.
    - Output directory: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/`: one file per top-level topic id of the first topic, `missing.tsv`, `decisions.md`.
    
    ## Assignment
    Cover every topic the README names for 9-10 (growing up and identity, work and applications, media and advertising,
    social problems, environment and climate, history of English-speaking countries, politics in simple terms, reading
    fiction and non-fiction, arguing, comparing, summarising) and strengthen every other topic at B1 level: abstract nouns,
    verbs and adjectives, linking words, words for text work. `cefr=B1` for the core, `B2` for clearly harder words,
    mostly `role=prod` for words pupils should use in their own texts and `rec` for words they meet in texts.
    Target size: 1,500–2,200 lexemes. A checker will review your list afterwards and may send you concrete remarks.
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

    Orchestrator: a checker (another AI agent, own knowledge only, no word lists) reviewed your band. Its remarks: /tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/check.tsv (columns lemma pos remark proposal reason) and check.md. Go through every remark and decide by your own judgement — accept or keep with a one-line reason:
    - `missing` → add with your own band 9-10 judgement (`src=ai|rev`); if the proposal is a lower band (5-6/7-8), do not add it, list it under "for lower bands" in decisions.md.
    - `too_early` → if you agree, remove the line and list it under "for lower bands" with the band.
    - `too_late` → if you agree, remove the line and list it under "for 11-13".
    - `level` → adjust if you agree (`src=ai|rev`).
    - `not_school` → remove if you agree.
    Also fix the duplicate `dismiss` (one level). Append a "Checker round" section to decisions.md with counts accepted/rejected per remark type and the reasons for rejections, plus the two lists. Re-run the checker script to 0 errors and report counts. Same clean-room rules.

## Checker run (faster model, own knowledge only): prompt (verbatim)

    # Checker run `en-efl-9-10-check`
    
    You check one band of Heinrich's English graded vocabulary (English as a foreign language in German schools)
    **from your own knowledge only**. Clean-room rules: no WebSearch or WebFetch, no published word lists of any kind,
    never open `/home/user/heinrich-eval`. You do not edit the author's files.
    
    Inputs:
    - Brief and band/CEFR guide: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/README.md`; topics: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-topics/en/graded/topics.tsv`
    - Lower bands (already finished): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/wt/graded-r1/en/graded/efl/*.tsv`
    - The band to check (band 9-10 (B1, some B2)): `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/*.tsv` (not missing.tsv); the author's reasoning: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/decisions.md`
    - Lemma index of our lexicon: `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/index/en_lemmas.tsv`
    
    Write `/tmp/claude-0/-home-user/f393a887-adce-5573-8b38-fc8fe73d6f1a/scratchpad/graded/runs/en-efl-9-10/check.tsv` with one line per remark, columns
    `lemma pos remark proposal reason`:
    - `too_early` / `too_late`: the word belongs to another band (proposal: the band);
    - `level`: the CEFR level is off (proposal: the level);
    - `missing`: a word typically introduced in band 9-10 (B1, some B2) for one of the band's topics is absent from this band and from
      all lower bands (proposal: `grade cefr topic role`); only lemmas of the lemma index;
    - `not_school`: not school vocabulary at this stage.
    Be selective and concrete: remark only where you are fairly sure (no stylistic preferences). Aim at the gaps first:
    whole groups of common words missing for a topic matter most. Then write a 5–10 line summary (`check.md`) with
    counts per remark type and per topic. Do not commit anything.

### Checker summary

# Check of band 9-10 (en-efl-9-10)

Counts (check.tsv): too_early 111, too_late 74, level 14, not_school 7, missing 148.

Overall: the band is dense and well aimed; my own candidate lists for the 9-10 topics (work, media, social problems,
environment, history, politics, law, literature) were almost entirely covered by this band or the lower bands.
Missing words are spread thin: mostly specific nouns (history outline, law, politics, nature/weather disasters, book
vocabulary: sequel, trilogy, publisher, edition), -ly degree/manner adverbs, and a few abstract nouns (concern, focus, individual).
Missing per topic: thinking/qualities 32, function.adverb 17, literature 18 (incl. book words), history 17, politics 17+, law 13, health 12, technology 12, society 11, global 9.
Main problem is too_early (about 110): words of earlier bands that the lower lists lack (task language like heading/error/instruction,
transport/travel words, family steps, sports, weather, feelings, maths terms, manner adverbs, `so` conjunction) are best moved down.
too_late (74): mostly B2 rec items better for 11-13 (formal verbs, argumentation terms like premise/fallacy/rebuttal, archaic connectors
hitherto/henceforth/lest, specialised social/political/economic terms). not_school: US legal terms (felony, misdemeanor, plaintiff, parole, defendant), google (verb), overdose.
Caveat: lower bands are partial (11-13 absent), so some "missing" items may be planned for 11-13; those I proposed are B1/B2 at the end of lower secondary.

## Decisions log (written by the author)

# Decisions log: author run `en-efl-9-10` (English, EFL, band 9-10, B1 with some B2)

## Inputs used
Only the brief (`en/graded/README.md`), `topics.tsv`, the lemma index of our own lexicon, the finished
lists of bands 3-4, 5-6 and 7-8 (to exclude words already introduced), and our own earlier "later" hint
file. No published word list, dictionary, course book or CEFR profile was consulted; no web access was
used; nothing under `heinrich-eval` was opened. All candidates come from my own knowledge of English and
of the topic areas of lower-secondary English lessons in Germany (grades 9 and 10, end of lower
secondary, intermediate school leaving certificate).

## Method
1. I went through the 9-10 topics of the brief (growing up and identity; work and applications; media and
   advertising; social problems; environment and climate; history of English-speaking countries;
   politics in simple terms; reading fiction and non-fiction; arguing, comparing, summarising) and wrote
   candidate words per situation (applying for a job, an advert analysis, a debate about a social issue,
   a summary or comment on a newspaper text, a short story analysis, an outline of colonial and civil
   rights history, a class discussion about climate protest, etc.).
2. Then I strengthened the general layers at B1: abstract nouns, verbs of thinking/changing/handling,
   evaluative and character adjectives, -ly adverbs of manner and degree, linking adverbs and
   conjunctions (however, therefore, nevertheless, whereas, although, unless, despite, regarding ...),
   and words for text work (paraphrase, cite, outline, caption, footnote ...). Lighter top-ups for health,
   travel, family, friends, school, shopping, town, transport, arts, sports, nature and the like.
3. A script checked every candidate against the lemma index (exact spelling and POS) and against the
   finished lower bands. Words already introduced in 3-4/5-6/7-8 were dropped (about 1,500 candidate
   hits), as were duplicates within my own list (first topic wins).
4. Review pass by hand over the remaining list (see below), then the checker until 0 errors.

## Bands, levels, roles, confidence
- Everything is `grade=9-10`. `cefr=B1` for the core (about 1,470 lines), `cefr=B2` for clearly harder
  or more formal words (about 370 lines: legal and political terms like prosecute, legislation, sovereignty;
  formal academic verbs like constitute, facilitate, undermine; formal adverbs like hence, presumably,
  arguably; literary terms like foreshadowing-type vocabulary, allegory, sonnet).
- `role=prod` for B1 words pupils should use in their own comments, letters of application, summaries
  and discussions; `role=rec` for the B2 words, which pupils mostly meet in texts.
- Confidence 70 by default (B1) and 60 for B2 items. Where our own earlier "later" hint also placed the
  word in 9-10 I raised confidence by 5; where the hint placed it in 11-13 or "none" I kept the word (my
  own judgement says it is met at the end of lower secondary) but lowered confidence to 60.
- Spelling: the lexicon lemmas are US spellings; British variants I thought of (organise, analyse,
  behaviour, neighbourhood, theatre, licence, defence ...) were mapped to the lexicon lemma. British-only
  lemmas that the lexicon lacks (programme, judgement) are listed in `missing.tsv`.

## Topic assignment
The first topic is the most specific one for the situation in which the word is taught; a second topic is
added where the word clearly belongs to two areas (e.g. `BBC` anglophone.uk|media, `deforestation`
environment|nature). Generic layers use sub-topics (`qualities.character`, `qualities.judgement`,
`actions.change`, `function.adverb` ...). One file per top-level id of the first topic.

## Borderline cases and exclusions
- Excluded after review as clearly earlier-band words even though the lower-band lists do not have them
  (they are gaps of the earlier bands, not 9-10 words): e.g. noun help, cost, sleep, patient, record,
  score, care, need, form, tool, use, play (theatre); adj close, neat, bossy, grumpy, absent, dumb,
  uncomfortable, online; adv sadly, safely, normally, terribly, gently, gladly, secretly, rudely; verbs
  test, end; country names Canada, India, Africa; vampire, zombie, superhero. The orchestrator may want to
  give these to a lower band.
- Kept but marked lower confidence: many -ly adverbs derived from known adjectives (they are formed
  productively by pupils; whether they count as "introduced" in 9-10 is debatable), and character
  adjectives such as clumsy, childish, lively.
- Multi-word expressions (climate change, global warming, human rights, peer pressure, point of view,
  side effect, rush hour, grow up, bring up, each other, so that ...) are central to these topics but the
  lexicon has no multi-word lemmas, so they were dropped (56 items) and not put into `missing.tsv`; their
  single-word parts were checked individually.
- Modal forms could/should/might/would are forms of can/shall/may/will in the lexicon; not listed.
- Some compounds I wrote as separate words (artificial intelligence, prime minister) produced POS slips;
  those slips were discarded, not reported as missing.

## missing.tsv
154 lemmas I wanted but the lexicon lacks: participial adjectives (qualified, experienced, detailed,
motivated, involved, isolated, biased, overwhelmed, developing/developed ...), hyphenated compounds
(self-confidence, self-esteem, hard-working, left-wing, well-being, non-fiction ...), plural-only or plural
senses (goods, statistics, lyrics, troops, ruins, rights, pros/cons), nouns such as sexism, xenophobia,
cyberbullying, shoplifting, flatmate, counterargument, collocation, hyperbole, alliteration, and proper
names for the English-speaking world (Commonwealth, Parliament, Congress, Maori, Cherokee, Sioux ...).
`missing_check.tsv` is the checker's output and is empty (0 missing members in the topic files).

## Checker round

I went through all 354 remarks in check.tsv and decided each one myself, without word lists. Lines I added or changed carry src=ai|rev.

| remark type | accepted | rejected / not applied |
|---|---|---|
| too_early | 106 | 5 |
| too_late | 71 | 3 |
| level | 13 | 1 |
| not_school | 5 | 2 |
| missing | 138 | 10 |

Missing proposals that were not added: 9 proposed a lower band (listed below), and likely/adj is already in a lower band. All 138 band-9-10 proposals were in the lexicon and were added with the checker's level, topic and role at conf=65. I agreed with each of them.

### Rejections and reasons
- too_early: key (adj): the attributive sense "crucial" (key factor) is B1; keep in 9-10
- too_early: ability (noun): B1 abstract noun used in applications and argument; keep in 9-10
- too_early: failure (noun): abstract B1 noun of argument texts; keep in 9-10
- too_early: alongside (adp): formal preposition of text work; keep in 9-10
- too_early: seldom (adv): formal frequency adverb, B1 written register; keep in 9-10
- too_late: criterion (noun): assessment criteria are named in 9-10 writing tasks; kept as B2 rec
- too_late: enslave (verb): needed for the slavery outline in 9-10 history; kept as B2 rec
- too_late: homophobia (noun): discussed under identity/discrimination in 9-10; kept as B2 rec
- level: dismiss (verb): only one line exists in the output (jobs, B2); the second candidate was deduplicated; no change
- not_school: defendant (noun): met in courtroom scenes of crime fiction read in 9-10; kept as B2 rec
- not_school: overdose (noun): drugs and addiction are a 9-10 social-problems topic; kept as B2 rec

For level, I accepted the other 13 B1 to B2 changes; those items are now role=rec. For not_school, the two items I kept are now B2 rec.

### For lower bands (removed from 9-10 or not added; band as proposed, which I agree with)
absent (adj) 5-6, afterward (adv) 7-8, attend (verb) 7-8, attraction (noun) 7-8, average (noun) 7-8, backward (adv) 7-8, baggage (noun) 7-8, beast (noun) 7-8, beer (noun) 7-8, bomb (noun) 7-8, bravely (adv) 7-8, brochure (noun) 7-8, calmly (adv) 7-8, cancer (noun) 7-8, ceremony (noun) 7-8, cheerfully (adv) 7-8, crash (noun) 7-8, crown (noun) 7-8, cyclist (noun) 7-8, decimal (noun) 7-8, delivery (noun) 7-8, depart (verb) 7-8, departure (noun) 7-8, difficulty (noun) 7-8, document (noun) 7-8, double (verb) 7-8, draw (noun) 7-8, dull (adj) 7-8, editor (noun) 7-8, elderly (adj) 7-8, entrance (noun) 7-8, error (noun) 7-8, fare (noun) 7-8, fashionable (adj) 7-8, fear (verb) 5-6, fraction (noun) 7-8, frost (noun) 7-8, galaxy (noun) 7-8, gentle (adj) 7-8, gently (adv) 7-8, google (verb) 7-8, hail (noun) 7-8, heading (noun) 7-8, humor (noun) 7-8, hunger (noun) 7-8, hunter (noun) 7-8, imagination (noun) 7-8, instruction (noun) 7-8, invisible (adj) 7-8, knowledge (noun) 7-8, label (noun) 7-8, list (verb) 7-8, live (adj) 7-8, mammal (noun) 7-8, marriage (noun) 7-8, medal (noun) 7-8, mixture (noun) 7-8, motorway (noun) 7-8, multiply (verb) 7-8, nearby (adv) 7-8, normally (adv) 7-8, occasion (noun) 7-8, odd (adj) 7-8, offline (adj) 7-8, onto (adp) 7-8, organize (verb) 7-8, outfit (noun) 7-8, panic (noun) 7-8, patient (noun) 7-8, pedestrian (noun) 7-8, perfectly (adv) 7-8, poetry (noun) 7-8, pregnant (adj) 7-8, preparation (noun) 7-8, proudly (adv) 7-8, raw (adj) 7-8, reader (noun) 7-8, relative (noun) 7-8, reply (noun) 5-6, reptile (noun) 7-8, resort (noun) 7-8, rhyme (verb) 7-8, scroll (verb) 7-8, shame (noun) 7-8, shock (noun) 7-8, sneeze (noun) 5-6, so (sconj) 5-6, spell (noun) 7-8, steep (adj) 7-8, stepbrother (noun) 7-8, stepfather (noun) 7-8, stepmother (noun) 7-8, stepsister (noun) 7-8, strength (noun) 7-8, stylish (adj) 7-8, sum (noun) 7-8, telescope (noun) 7-8, terribly (adv) 7-8, thirdly (adv) 7-8, tip (noun) 5-6, total (noun) 7-8, trailer (noun) 7-8, trendy (adj) 7-8, trophy (noun) 7-8, tune (noun) 5-6, universe (noun) 7-8, upload (noun) 7-8, weakness (noun) 7-8, weapon (noun) 7-8, wicked (adj) 7-8, wifi (noun) 7-8, wine (noun) 7-8, wonder (noun) 7-8, worldwide (adv) 7-8, worldwide (adj) 7-8

I also excluded these earlier-band gaps in the first round (see above): help, cost, sleep, record, score, care, need, form, tool, use, play (nouns); close, neat, bossy, grumpy, dumb, adorable, bloody, uncomfortable, online (adjectives); sadly, safely, secretly, rudely, gladly (adverbs); test, end (verbs); Canada, India, Africa; trick, machine, vampire, zombie, superhero.

### For 11-13 (removed from 9-10)
abundance (noun), adversity (noun), affluence (noun), allegiance (noun), allegory (noun), ambiguity (noun), amid (adp), annotation (noun), appendix (noun), attain (verb), bandwidth (noun), capitalism (noun), coherence (noun), concede (verb), conceive (verb), constraint (noun), contemplate (verb), contradictory (adj), deduce (verb), deprivation (noun), discrepancy (noun), dynasty (noun), emancipate (verb), encryption (noun), endure (verb), entitlement (noun), equity (noun), exposition (noun), fallacy (noun), feudalism (noun), ghetto (noun), henceforth (adv), hinder (verb), hitherto (adv), illuminate (verb), induce (verb), inhibit (verb), legislate (verb), lest (sconj), lobby (verb), lobbyist (noun), malware (noun), marginalize (verb), notion (noun), novella (noun), outcast (noun), outsourcing (noun), outweigh (verb), oversee (verb), paradox (noun), peasant (noun), penetrate (verb), personification (noun), plausible (adj), premise (noun), prevail (verb), rationale (noun), rebuttal (noun), refute (verb), regime (noun), serf (noun), sovereignty (noun), stigma (noun), strive (verb), thereafter (adv), thereby (adv), undertake (verb), uphold (verb), utter (verb), veto (verb), whilst (sconj)

### Duplicate dismiss
The output has only one line for dismiss (verb), in jobs.tsv at B2 rec. The candidate in my argument list was dropped as a duplicate before writing, so the files have one level and nothing needed to change.

### Result after the round
1,800 lexemes in total: 1,456 B1 and 344 B2; 1,453 prod and 347 rec; 153 lines are src=ai|rev. The checker script reports 0 errors and 0 warnings. missing.tsv is unchanged at 154 lemmas, because every word the checker proposed exists in the lexicon.

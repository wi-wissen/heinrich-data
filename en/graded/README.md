# English graded vocabulary (`en/graded/`)

For every lexeme (or sense) of the English lexicon, this layer records the **CEFR level** and the
**grade band** at which pupils in German schools typically learn the word (English as a foreign
language, EFL), and its **topics**. Format, semantics, merge rules, pack attributes and tools:
`Heinrich/docs/GRADED_VOCAB.md`.

```
en/graded/topics.tsv       closed topic catalogue (ids, German and English labels, tracks)
en/graded/efl/<topic>.tsv  English as a foreign language, one file per topic group
en/graded/PROVENANCE.md    clean-room log: every authoring and revision run, with its prompt
```

Line format (`lemma[:sense]  pos  fields`):

```
kitchen   noun  grade=3-4 cefr=A1 topic=home role=prod conf=90 src=ai
```

## Attribution and labelling

This vocabulary layer was written by AI authors (Claude) based on the competence levels of the Common
European Framework of Reference and the curricula of the German federal states, sample-checked by
teachers and statistically compared internally with common reference lists. It contains no entries from
third-party word lists.

(The teacher sample is planned; until it has been run, end-user texts leave out the teacher check.)

## Clean-room rules

Same as `de/graded/README.md`: authors work from their own knowledge of English and of the topic areas
of English lessons; they never see published vocabulary lists (exam word lists, CEFR word profiles,
course-book or state vocabulary lists, learner-dictionary core lists). `src=` records only our own
provenance (`ai`, `teacher`, `freq`, `rev`). A separate reviewer reports only aggregate statistics and
patterns in its own words.

## Bands and levels

`cefr=` is required, `grade=` too for EFL (the band in which the word is typically introduced when
English starts in grade 3; in states starting in grade 1 the primary words move earlier). Expected
correspondence (a guide, not a rule):

| band | CEFR | stage |
|---|---|---|
| 3-4 | A1 (partly pre-A1) | primary English: mostly listening and speaking, words learned with pictures and songs |
| 5-6 | A1+/A2 | first years of secondary school |
| 7-8 | A2/A2+ | |
| 9-10 | B1 | end of lower secondary (intermediate school leaving certificate) |
| 11-13 | B1+/B2, receptive C1 | upper secondary up to the Abitur |

`role=prod`: pupils should use the word themselves; `role=rec`: they should understand it.

## Topic descriptions per band (own words)

- **3-4 (A1).** Greetings and classroom routines; me, my family and friends; numbers, colours, shapes;
  the body and clothes; animals and pets; food and drink, likes and dislikes; home and furniture; toys
  and games; school things; days, months, seasons, weather, the time; festivals through the year;
  simple actions and sports; stories, songs and rhymes. All of the most frequent function words and
  basic verbs.
- **5-6 (A1+/A2).** Daily routine; hobbies and free time; school life and subjects; shopping and
  money; town, directions and transport; food and meals in more detail; holidays and travel; birthdays
  and celebrations; describing people, places and simple past events; pets and wild animals; British
  daily life (London, school uniform, homes).
- **7-8 (A2/A2+).** Friendship and feelings; media and technology; jobs and plans for the future;
  health and the body; the environment in everyday terms; adventures and stories; life in other
  English-speaking places (the USA, Scotland, Ireland, Australia); giving opinions and reasons; simple
  past, present perfect and future contexts.
- **9-10 (B1).** Growing up and identity; the world of work and applications; media and advertising;
  social problems; the environment and climate; history of English-speaking countries in outline;
  politics in simple terms; reading fiction and non-fiction; arguing, comparing, summarising.
- **11-13 (B1+/B2, receptive C1).** Globalisation and migration; politics and democracy (the UK and
  the USA); ethics and science; post-colonial literature and the Commonwealth; media and manipulation;
  the American Dream; utopia and dystopia; analysing and interpreting literature and non-fiction,
  stylistic devices, argumentative writing.

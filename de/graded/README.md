# German graded vocabulary (`de/graded/`)

For every lexeme (or sense) of the German lexicon, this layer records the **grade band** in which pupils
typically learn and actively need the word, optionally a **CEFR level**, and its **topics**. Format,
semantics, merge rules, pack attributes and tools: `Heinrich/docs/GRADED_VOCAB.md`.

```
de/graded/topics.tsv       closed topic catalogue (ids, German and English labels, tracks)
de/graded/l1/<area>.tsv    German as a first language, one file per area
de/graded/daz/<domain>.tsv German as a second language, one file per CEFR domain / field of action
de/graded/PROVENANCE.md    clean-room log: every authoring and revision run, with its prompt
```

Line format (`lemma[:sense]  pos  fields`):

```
Hund             noun  grade=1-2 topic=animals role=prod conf=95 src=ai
Photosynthese    noun  grade=7-8 topic=bio.plants role=rec conf=80 src=ai
```

## Attribution and labelling

This vocabulary layer was written by AI authors (Claude) based on the competence levels of the Common
European Framework of Reference and the curricula of the German federal states, sample-checked by
teachers and statistically compared internally with common reference lists. It contains no entries from
third-party word lists.

German version for end-user documentation:

> Diese Wortschatz-Schicht wurde von KI-Autoren (Claude) anhand der Kompetenzstufen des Gemeinsamen
> Europäischen Referenzrahmens und der Lehrpläne der Länder erstellt, von Lehrkräften stichprobenartig
> geprüft und intern gegen gängige Referenzlisten statistisch abgeglichen. Sie enthält keine Einträge aus
> fremden Wortlisten.

(The teacher sample is planned; until it has been run, end-user texts leave out "von Lehrkräften
stichprobenartig geprüft".)

## Clean-room rules

- Authors write from their own knowledge of German, of school and of the curricula' topic areas. They
  receive only this README and `topics.tsv`. They never see a published word list: no basic-vocabulary
  lists of the states, no exam or course word lists, no CEFR word profiles, no frequency lists of
  children's books by others. Our own frequency list `de/frequency/forms.tsv` and our own lexicon may be
  used.
- `src=` records only our own provenance: `ai` (author), `teacher` (confirmed by a teacher), `freq`
  (adjusted by our own frequency signal), `rev` (revised by the author after a statistical reviewer
  finding). A flag saying that a word is "in list X" is forbidden.
- A separate reviewer compares the layer with reference lists outside the repositories and reports only
  aggregate numbers per band, level and topic, and patterns in its own words with its own new examples;
  never entries, never "word X is missing". At most two revision rounds per topic against the same
  reference.
- Every authoring and revision run is logged in `PROVENANCE.md` (prompt, inputs, decisions).

## Learning tracks and bands

| track | directory | required | meaning of the level |
|---|---|---|---|
| L1 German | `l1/` | `grade=` | grade band in which the word is typically introduced |
| German as a second language | `daz/` | `cefr=` | CEFR level at which the word is typically learned |

Bands: `1-2`, `3-4`, `5-6`, `7-8`, `9-10`, `11-13`. `role=prod`: pupils should write the word
themselves at that band; `role=rec`: they should understand it (typical for subject terms met in texts).

## Topic descriptions per track and band (own words)

These descriptions say what pupils do with language at each stage. They are the authors' brief; they
name situations and subject matter, not words.

### L1 area `core` (everyday and general vocabulary)

- **1-2.** Children talk and write about themselves, their family, friends, home, school day, toys,
  animals, food, clothes, the body, the weather and the seasons. They name things in their surroundings,
  describe simple actions and feelings, count and compare. Writing is short sentences about their own
  experience. The most frequent function words (articles, personal pronouns, the commonest prepositions
  and conjunctions, question words, auxiliaries and modals) are all in this band.
- **3-4.** The world widens: the neighbourhood and town, traffic and the way to school, shopping and
  money, jobs of adults, festivals through the year, nature walks, simple experiments, media use, rules
  of living together. Pupils retell stories, write letters and reports, give reasons and express wishes
  and opinions; the vocabulary of time relations, causes and consequences grows.
- **5-6.** Everyday vocabulary becomes more differentiated (shades of feelings and character, exact
  verbs of saying and moving), and general school language appears: describing, comparing, explaining,
  justifying. Topics: friendship and conflicts, hobbies and clubs, the environment, travel.
- **7-8.** Abstract nouns and verbs for processes, relations and evaluation; vocabulary for arguing and
  discussing; youth, identity, media, society.
- **9-10.** General academic language (analyse, assume, consequence, development, aspect), the language
  of applications and the world of work, public life and politics in everyday terms.
- **11-13.** Sophisticated general and academic vocabulary for essays, analyses and debates, foreign
  words of educated usage, nuanced evaluation.

### L1 subject areas

- **`math`.** 1-2: numbers up to 100, adding and subtracting, simple shapes, money and length, comparing
  quantities. 3-4: numbers up to a million, the four operations and written methods, shapes and solids,
  symmetry, measures of length, weight, time, capacity, simple data and chance. 5-6: natural numbers,
  fractions and decimals, area and perimeter, angles, basic geometry constructions. 7-8: percentages,
  proportions, terms and equations, triangles and their theorems, probability. 9-10: functions (linear,
  quadratic, exponential), Pythagoras, trigonometry, circles and solids, statistics. 11-13: calculus,
  vectors and analytic geometry, stochastics.
- **`science`** (primary general studies, then biology `bio`, chemistry `chem`, physics `phys`,
  technology `tech`). 1-2: the body and senses, animals and plants nearby, weather, water, simple
  observations. 3-4: habitats, life cycles, the human body and health, materials and their properties,
  air and water, electricity in simple circuits, magnetism, the sun and the moon, simple machines.
  5-6: vertebrates and invertebrates, plant structure and growth, puberty, substances and mixtures, heat,
  light and shadow, sound, the solar system. 7-8: cells, ecosystems, nutrition and digestion, chemical
  reactions, atoms, mechanics, electricity, optics. 9-10: genetics, evolution, nerves and hormones,
  acids and bases, organic basics, energy, electromagnetism, radioactivity. 11-13: molecular biology,
  neurobiology, ecology in depth, reaction kinetics and equilibrium, organic chemistry, fields, waves,
  quantum and atomic physics, astrophysics.
- **`history`.** 3-4 (in general studies): past and present, then and now, simple sources, local
  history. 5-6: what history is, prehistory, ancient Egypt, Greece, Rome. 7-8: Middle Ages, early modern
  period, discoveries, Reformation, absolutism, revolutions. 9-10: industrialisation, imperialism, world
  wars, Weimar Republic, National Socialism and the Holocaust, Cold War, division and unification of
  Germany. 11-13: the same periods analysed with historiographical terms and source criticism.
- **`geo`.** 3-4: maps and orientation, the home region, Germany. 5-6: landscapes of Germany and
  Europe, maps and scale, agriculture, tourism, the coast and the Alps. 7-8: climate zones, deserts,
  rainforest, polar regions, volcanoes and earthquakes, plate tectonics. 9-10: population and migration,
  cities, economic sectors, development, globalisation. 11-13: spatial analysis, sustainability,
  global disparities.
- **`politics`, `economy`.** 3-4: rules, class council, community. 5-6: living together, family
  and school as communities, money and consumption. 7-8: democracy, the municipality, rights of young
  people, media, consumers, work. 9-10: the constitution, federal institutions, elections and parties,
  the rule of law, the European Union, the social state, the market economy, careers. 11-13: political
  theory, international relations, economic policy.
- **`religion`, `ethics`.** 1-4: festivals, stories, community, right and wrong, friendship. 5-6:
  world religions and their practice, values. 7-10: conscience, responsibility, justice, death and
  meaning, religions in society. 11-13: philosophical and theological concepts.
- **`art`, `music`, `drama`.** 1-4: colours, materials and techniques, singing, simple instruments,
  rhythm, playing roles. 5-10: composition and analysis of pictures, art epochs, architecture, notation,
  intervals and keys, genres and epochs of music, theatre. 11-13: analytic vocabulary of art and music.
- **`sports`.** 1-4: running, jumping, throwing, ball games, swimming, gymnastics, fair play.
  5-13: team sports, athletics disciplines, training, fitness and health.
- **`computing`.** 3-4: devices and their use, the internet, safety. 5-6: files, information,
  communication online. 7-10: data, algorithms, programming, networks, privacy and security.
  11-13: formal languages, databases, AI and society.
- **`language`** (terms of German lessons). 1-2: letters, sounds, syllables, words, sentences, story.
  3-4: parts of speech and their German school names, simple tenses, the parts of a sentence, text
  types (letter, report, description). 5-6: grammar of the simple and compound sentence, fairy tale,
  fable, legend, poem terms. 7-8: text analysis, argumentation, ballad, short story, newspaper text types.
  9-10: literary analysis, drama, stylistic devices, rhetoric. 11-13: literary epochs, analysis and
  interpretation, linguistic reflection.

### German as a second language (`daz/`)

Adults and teenagers learning German as a second language, ordered by CEFR level. Domains: personal
information, housing, work and job search, health and doctors, children's care and school, shopping and
consumer rights, authorities and offices, bank and insurance, mobility, media, leisure, social contacts,
emergencies, arriving and migration.

- **A1.** Simple personal information, greetings, numbers, prices, times, everyday objects, food,
  family, the flat, the most frequent verbs and function words; simple requests and questions.
- **A2.** Routine situations: appointments, shopping, the doctor, finding a flat, describing the
  past, work in simple terms, transport, forms, simple messages.
- **B1.** Explaining and justifying, feelings and opinions, work and training, authorities and
  contracts, complaints, health in more detail, the news in simple terms, living together in society.
- **B2.** Abstract and specialised topics in one's field, discussions, formal letters, society and
  politics, media in depth.
- **C1.** Flexible, precise vocabulary for academic and professional use.

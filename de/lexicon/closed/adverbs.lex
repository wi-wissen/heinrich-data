# Adverbs that matter for grammar rules. Written clean-room by hand. Open-class adverbs
# go to adv/<letter>.lex.
#
# type=  daytime      lowercase -s adverbs of the time of day (morgens, abends): never capitalised;
#                     contrast am Morgen, heute Morgen (noun)
#        weekday      montags, sonntags …
#        day          deictic day adverbs (heute, gestern, morgen …); a following time-of-day
#                     word is a capitalised noun: heute Abend, gestern Morgen, morgen Früh|früh
#        time, place, direction, manner, degree, modal, causal, focus, neg
#        conj         conjunctional adverb: links clauses but takes a position in the clause
#                     (verb second after it: deshalb kommt er); a comma or full stop precedes it
#        pronominal   da(r)-/wo(r)-/hier- + preposition (darauf, worauf, hierzu)
#        int          interrogative, introduces direct and indirect questions (comma before an
#                     indirect question: ich weiß nicht, wann er kommt)
#        rel          relative adverb, introduces a relative clause (der Ort, wo …)
# int, rel, neg and pronominal also give the form a PronType reading (Int, Rel, Neg, Dem).

# ---------------------------------------------------------------- time of day
morgens      adv type=daytime
frühmorgens  adv type=daytime
vormittags   adv type=daytime
mittags      adv type=daytime
nachmittags  adv type=daytime
abends       adv type=daytime
spätabends   adv type=daytime
nachts       adv type=daytime
mitternachts adv type=daytime
tags         adv type=daytime note=tags darauf; tagsüber
tagsüber     adv type=daytime

# ---------------------------------------------------------------- days of the week
montags      adv type=weekday
dienstags    adv type=weekday
mittwochs    adv type=weekday
donnerstags  adv type=weekday
freitags     adv type=weekday
samstags     adv type=weekday
sonnabends   adv type=weekday
sonntags     adv type=weekday
werktags     adv type=weekday
wochentags   adv type=weekday
feiertags    adv type=weekday
wochenends   adv type=weekday style=rare

# ---------------------------------------------------------------- deictic days
heute        adv type=day|time
gestern      adv type=day|time
vorgestern   adv type=day|time
morgen       adv type=day|time note=tomorrow; der Morgen (morning) is a noun
übermorgen   adv type=day|time

# ---------------------------------------------------------------- time
anfangs      adv type=time
bald         adv type=time
bereits      adv type=time
bisher       adv type=time
bislang      adv type=time
damals       adv type=time
danach       adv type=time|pronominal
dann         adv type=time|conj
demnächst    adv type=time
derzeit      adv type=time
einst        adv type=time
endlich      adv type=time
erst         adv type=time|focus
gerade       adv type=time|focus
gleich       adv type=time
heutzutage   adv type=time
immer        adv type=time
inzwischen   adv type=time
irgendwann   adv type=time
je           adv type=time note=ever (hast du je …); also adp and sconj
jemals       adv type=time
jetzt        adv type=time
längst       adv type=time
manchmal     adv type=time
mittlerweile adv type=time
nachher      adv type=time
neulich      adv type=time
nie          adv type=time|neg
niemals      adv type=time|neg
noch         adv type=time|focus
nun          adv type=time
oftmals      adv type=time
schon        adv type=time|focus
seitdem      adv type=time
seither      adv type=time
sofort       adv type=time
soeben       adv type=time
später       adv type=time note=also the comparative of spät
stets        adv type=time
vorher       adv type=time
vorhin       adv type=time
wieder       adv type=time note=again; not wider (against)
zuerst       adv type=time
zuletzt      adv type=time
zunächst     adv type=time
zurzeit      adv type=time note=at the moment; zur Zeit (at the time of) is preposition + noun
zuvor        adv type=time

# ---------------------------------------------------------------- place and direction
anderswo     adv type=place
da           adv type=place|time|causal note=also a conjunction (conjunctions.lex)
daheim       adv type=place
dort         adv type=place
dorthin      adv type=direction
draußen      adv type=place
drinnen      adv type=place
her          adv type=direction
herein       adv type=direction
heraus       adv type=direction
herauf       adv type=direction
herunter     adv type=direction
herüber      adv type=direction
hier         adv type=place
hierher      adv type=direction
hierhin     adv type=direction
hin          adv type=direction
hinein       adv type=direction
hinaus       adv type=direction
hinauf       adv type=direction
hinunter     adv type=direction
hinüber      adv type=direction
hinten       adv type=place
innen        adv type=place
irgendwo     adv type=place
links        adv type=place
nirgends     adv type=place|neg
nirgendwo    adv type=place|neg
oben         adv type=place
rechts       adv type=place
überall      adv type=place
unten        adv type=place
unterwegs    adv type=place
vorn         adv type=place
vorne        adv type=place
weg          adv type=direction note=away; der Weg is a noun
woanders     adv type=place
zurück       adv type=direction
außen        adv type=place

# ---------------------------------------------------------------- interrogative and relative
inwiefern    adv type=int
inwieweit    adv type=int
wann         adv type=int|time
warum        adv type=int|causal
weshalb      adv type=int|rel|causal
weswegen     adv type=int|rel|causal
wie          adv type=int|rel|manner note=wie geht es dir; also the conjunction wie
wieso        adv type=int|causal
wo           adv type=int|rel|place
woher        adv type=int|rel|direction
wohin        adv type=int|rel|direction

# ---------------------------------------------------------------- pronominal adverbs (da-, wo-, hier-)
dabei        adv type=pronominal
dadurch      adv type=pronominal|causal
dafür        adv type=pronominal
dagegen      adv type=pronominal|conj
dahinter     adv type=pronominal
damit        adv type=pronominal
daneben      adv type=pronominal
daran        adv type=pronominal
darauf       adv type=pronominal
daraus       adv type=pronominal
darin        adv type=pronominal
darüber      adv type=pronominal
darum        adv type=pronominal|conj|causal
darunter     adv type=pronominal
davon        adv type=pronominal
davor        adv type=pronominal
dazu         adv type=pronominal
dazwischen   adv type=pronominal
dran         adv type=pronominal style=colloquial
drauf        adv type=pronominal style=colloquial
draus        adv type=pronominal style=colloquial
drin         adv type=pronominal style=colloquial
drüber       adv type=pronominal style=colloquial
drum         adv type=pronominal style=colloquial
drunter      adv type=pronominal style=colloquial
wobei        adv type=pronominal|int|rel
wodurch      adv type=pronominal|int|rel
wofür        adv type=pronominal|int|rel
wogegen      adv type=pronominal|int|rel
womit        adv type=pronominal|int|rel
wonach       adv type=pronominal|int|rel
woran        adv type=pronominal|int|rel
worauf       adv type=pronominal|int|rel
woraus       adv type=pronominal|int|rel
worin        adv type=pronominal|int|rel
worüber      adv type=pronominal|int|rel
worum        adv type=pronominal|int|rel
worunter     adv type=pronominal|int|rel
wovon        adv type=pronominal|int|rel
wovor        adv type=pronominal|int|rel
wozu         adv type=pronominal|int|rel
hierbei      adv type=pronominal
hierdurch    adv type=pronominal
hierfür      adv type=pronominal
hiergegen    adv type=pronominal
hiermit      adv type=pronominal
hiernach     adv type=pronominal
hieran       adv type=pronominal
hierauf      adv type=pronominal
hieraus      adv type=pronominal
hierin       adv type=pronominal
hierüber     adv type=pronominal
hierunter    adv type=pronominal
hiervon      adv type=pronominal
hiervor      adv type=pronominal
hierzu       adv type=pronominal

# ---------------------------------------------------------------- reciprocal compounds
aneinander   adv type=manner
aufeinander  adv type=manner
auseinander  adv type=manner
beieinander  adv type=manner
durcheinander adv type=manner
füreinander  adv type=manner
gegeneinander adv type=manner
hintereinander adv type=manner
ineinander   adv type=manner
miteinander  adv type=manner
nacheinander adv type=manner
nebeneinander adv type=manner
übereinander adv type=manner
umeinander   adv type=manner
untereinander adv type=manner
voneinander  adv type=manner
voreinander  adv type=manner
zueinander   adv type=manner

# ---------------------------------------------------------------- conjunctional adverbs
allerdings   adv type=conj|modal
also         adv type=conj
andererseits adv type=conj note=also anderseits, andrerseits
anderseits   adv type=conj style=rare
andrerseits  adv type=conj style=rare
anschließend adv type=conj|time
ansonsten    adv type=conj
außerdem     adv type=conj
dennoch      adv type=conj
deshalb      adv type=conj|causal
deswegen     adv type=conj|causal
daher        adv type=conj|causal|direction
demnach      adv type=conj
demzufolge   adv type=conj|causal
einerseits   adv type=conj pair=andererseits
ferner       adv type=conj
folglich     adv type=conj|causal
gleichwohl   adv type=conj
hingegen     adv type=conj
immerhin     adv type=conj|modal
infolgedessen adv type=conj|causal
jedoch       adv type=conj note=also a coordinating conjunction
mithin       adv type=conj
nichtsdestotrotz adv type=conj
nichtsdestoweniger adv type=conj
schließlich  adv type=conj|time
sodann       adv type=conj|time
somit        adv type=conj
sonst        adv type=conj
stattdessen  adv type=conj
teils        adv type=conj pair=teils note=teils … teils
trotzdem     adv type=conj
überdies     adv type=conj
vielmehr     adv type=conj
zudem        adv type=conj
zwar         adv type=conj pair=aber note=zwar … aber (comma before aber)

# ---------------------------------------------------------------- degree
äußerst      adv type=degree
allzu        adv type=degree
beinahe      adv type=degree
besonders    adv type=degree|focus
desto        adv type=degree note=je … desto
etwa         adv type=degree note=approximately; also a particle
fast         adv type=degree
ganz         adv type=degree note=also an adjective
genug        adv type=degree
höchst       adv type=degree
höchstens    adv type=degree|focus
kaum         adv type=degree|neg
mindestens   adv type=degree|focus
sehr         adv type=degree
so           adv type=degree|manner
überaus     adv type=degree
umso         adv type=degree note=je … umso
ungefähr     adv type=degree
weitaus      adv type=degree
ziemlich     adv type=degree
zuviel       adv type=degree spelling=old note=old spelling of zu viel (zu viel Arbeit; before 1996 zuviel); a noun use is das Zuviel
zuwenig      adv type=degree spelling=old note=old spelling of zu wenig (zu wenig Zeit); a noun use is das Zuwenig

# ---------------------------------------------------------------- focus
allein       adv type=focus note=also an adjective and a conjunction
auch         adv type=focus
ausgerechnet adv type=focus
ebenfalls    adv type=focus
insbesondere adv type=focus
lediglich    adv type=focus
nur          adv type=focus
selbst       adv type=focus note=even / oneself (er selbst)
selber       adv type=focus
sogar        adv type=focus
wenigstens   adv type=focus
zumindest    adv type=focus

# ---------------------------------------------------------------- modal (sentence adverbs)
andernfalls  adv type=modal|conj
angeblich    adv type=modal note=also an adjective
durchaus     adv type=modal
freilich     adv type=modal
gegebenenfalls adv type=modal
glücklicherweise adv type=modal
hoffentlich  adv type=modal
jedenfalls   adv type=modal
keinesfalls  adv type=modal|neg
keineswegs   adv type=modal|neg
mitnichten   adv type=modal|neg
möglicherweise adv type=modal
nämlich      adv type=modal|causal note=never at the start of a clause
notfalls     adv type=modal
ohnehin      adv type=modal
quasi        adv type=modal
sicherlich   adv type=modal
sowieso      adv type=modal
vielleicht   adv type=modal
zweifellos   adv type=modal

# ---------------------------------------------------------------- manner and other
anders       adv type=manner
ebenso       adv type=manner
genauso      adv type=manner
irgendwie    adv type=manner
umsonst      adv type=manner
vergebens    adv type=manner
zusammen     adv type=manner
desgleichen  adv type=manner|conj note=likewise (er tat desgleichen; desgleichen gilt für …)

# ---------------------------------------------------------------- personal pronoun + wegen/halben/willen
# Genitive stem + -et- + postposition: meinetwegen (because of me; also: as far as I'm
# concerned), um meinetwillen (for my sake), meinethalben (dated).
meinetwegen  adv type=causal|modal note=because of me; also: as far as I am concerned (meinetwegen kannst du gehen)
deinetwegen  adv type=causal
seinetwegen  adv type=causal
ihretwegen   adv type=causal
unseretwegen adv type=causal
unsertwegen  adv type=causal note=variant of unseretwegen
euretwegen   adv type=causal
meinetwillen adv type=causal note=um meinetwillen (for my sake)
deinetwillen adv type=causal note=um deinetwillen
seinetwillen adv type=causal note=um seinetwillen
ihretwillen  adv type=causal note=um ihretwillen
unseretwillen adv type=causal note=um unseretwillen
unsertwillen adv type=causal note=variant of unseretwillen
euretwillen  adv type=causal note=um euretwillen
meinethalben adv type=causal|modal style=archaic note=dated for meinetwegen
deinethalben adv type=causal style=archaic
seinethalben adv type=causal style=archaic
ihrethalben  adv type=causal style=archaic
unserthalben adv type=causal style=archaic
eurethalben  adv type=causal style=archaic
derentwegen  adv type=causal|rel note=because of whom/which (die Frau, derentwegen er kam); also demonstrative
dessentwegen adv type=causal|rel note=because of whom/which (der Mann, dessentwegen …)

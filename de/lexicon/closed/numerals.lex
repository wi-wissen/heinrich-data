# Numerals (num). Written clean-room by hand; 21–99 follow the regular pattern
# <unit>und<ten> (einundzwanzig, zweiunddreißig), ordinals add -te (2–19) or -ste (20+).
# Ordinals (type=ord) are declined like adjectives (der zweite, ein zweiter) and are ADJ
# readings with NumType=Ord. Multiplicatives (type=mult) and fractions (type=frac) are
# uninflected. Million, Milliarde, Dutzend, Hälfte, Drittel … are nouns (noun/).

# ---------------------------------------------------------------- cardinals
null              num value=0
eins              num value=1 note=counting form (eins, zwei, drei); before a noun the article ein is used
zwei              num value=2 cases=zwei,zweier,zweien[rare]|zwei,zwei note=zweier, dreier: genitive without article (die Aussage zweier Zeugen)
drei              num value=3 cases=drei,dreier,dreien[rare]|drei,drei
vier              num value=4 cases=vier,vierer[rare],vieren|vier,vier note=auf allen vieren
fünf              num value=5
sechs             num value=6
sieben            num value=7
acht              num value=8
neun              num value=9
zehn              num value=10
elf               num value=11
zwölf             num value=12
dreizehn          num value=13
vierzehn          num value=14
fünfzehn          num value=15
sechzehn          num value=16
siebzehn          num value=17
achtzehn          num value=18
neunzehn          num value=19
zwanzig           num value=20
einundzwanzig     num value=21
zweiundzwanzig    num value=22
dreiundzwanzig    num value=23
vierundzwanzig    num value=24
fünfundzwanzig    num value=25
sechsundzwanzig   num value=26
siebenundzwanzig  num value=27
achtundzwanzig    num value=28
neunundzwanzig    num value=29
dreißig           num value=30
einunddreißig     num value=31
zweiunddreißig    num value=32
dreiunddreißig    num value=33
vierunddreißig    num value=34
fünfunddreißig    num value=35
sechsunddreißig   num value=36
siebenunddreißig  num value=37
achtunddreißig    num value=38
neununddreißig    num value=39
vierzig           num value=40
einundvierzig     num value=41
zweiundvierzig    num value=42
dreiundvierzig    num value=43
vierundvierzig    num value=44
fünfundvierzig    num value=45
sechsundvierzig   num value=46
siebenundvierzig  num value=47
achtundvierzig    num value=48
neunundvierzig    num value=49
fünfzig           num value=50
einundfünfzig     num value=51
zweiundfünfzig    num value=52
dreiundfünfzig    num value=53
vierundfünfzig    num value=54
fünfundfünfzig    num value=55
sechsundfünfzig   num value=56
siebenundfünfzig  num value=57
achtundfünfzig    num value=58
neunundfünfzig    num value=59
sechzig           num value=60
einundsechzig     num value=61
zweiundsechzig    num value=62
dreiundsechzig    num value=63
vierundsechzig    num value=64
fünfundsechzig    num value=65
sechsundsechzig   num value=66
siebenundsechzig  num value=67
achtundsechzig    num value=68
neunundsechzig    num value=69
siebzig           num value=70
einundsiebzig     num value=71
zweiundsiebzig    num value=72
dreiundsiebzig    num value=73
vierundsiebzig    num value=74
fünfundsiebzig    num value=75
sechsundsiebzig   num value=76
siebenundsiebzig  num value=77
achtundsiebzig    num value=78
neunundsiebzig    num value=79
achtzig           num value=80
einundachtzig     num value=81
zweiundachtzig    num value=82
dreiundachtzig    num value=83
vierundachtzig    num value=84
fünfundachtzig    num value=85
sechsundachtzig   num value=86
siebenundachtzig  num value=87
achtundachtzig    num value=88
neunundachtzig    num value=89
neunzig           num value=90
einundneunzig     num value=91
zweiundneunzig    num value=92
dreiundneunzig    num value=93
vierundneunzig    num value=94
fünfundneunzig    num value=95
sechsundneunzig   num value=96
siebenundneunzig  num value=97
achtundneunzig    num value=98
neunundneunzig    num value=99
zwo               num value=2 style=colloquial note=used to avoid confusion with drei (on the phone)
hundert           num value=100
einhundert        num value=100
zweihundert       num value=200
dreihundert       num value=300
vierhundert       num value=400
fünfhundert       num value=500
sechshundert      num value=600
siebenhundert     num value=700
achthundert       num value=800
neunhundert       num value=900
tausend           num value=1000
eintausend        num value=1000
zweitausend       num value=2000
dreitausend       num value=3000
viertausend       num value=4000
fünftausend       num value=5000
zehntausend       num value=10000
hunderttausend    num value=100000

# ---------------------------------------------------------------- ordinals
erste                num type=ord value=1
zweite               num type=ord value=2
dritte               num type=ord value=3
vierte               num type=ord value=4
fünfte               num type=ord value=5
sechste              num type=ord value=6
siebte               num type=ord value=7
achte                num type=ord value=8
neunte               num type=ord value=9
zehnte               num type=ord value=10
elfte                num type=ord value=11
zwölfte              num type=ord value=12
dreizehnte           num type=ord value=13
vierzehnte           num type=ord value=14
fünfzehnte           num type=ord value=15
sechzehnte           num type=ord value=16
siebzehnte           num type=ord value=17
achtzehnte           num type=ord value=18
neunzehnte           num type=ord value=19
zwanzigste           num type=ord value=20
einundzwanzigste     num type=ord value=21
zweiundzwanzigste    num type=ord value=22
dreiundzwanzigste    num type=ord value=23
vierundzwanzigste    num type=ord value=24
fünfundzwanzigste    num type=ord value=25
sechsundzwanzigste   num type=ord value=26
siebenundzwanzigste  num type=ord value=27
achtundzwanzigste    num type=ord value=28
neunundzwanzigste    num type=ord value=29
dreißigste           num type=ord value=30
einunddreißigste     num type=ord value=31
zweiunddreißigste    num type=ord value=32
dreiunddreißigste    num type=ord value=33
vierunddreißigste    num type=ord value=34
fünfunddreißigste    num type=ord value=35
sechsunddreißigste   num type=ord value=36
siebenunddreißigste  num type=ord value=37
achtunddreißigste    num type=ord value=38
neununddreißigste    num type=ord value=39
vierzigste           num type=ord value=40
einundvierzigste     num type=ord value=41
zweiundvierzigste    num type=ord value=42
dreiundvierzigste    num type=ord value=43
vierundvierzigste    num type=ord value=44
fünfundvierzigste    num type=ord value=45
sechsundvierzigste   num type=ord value=46
siebenundvierzigste  num type=ord value=47
achtundvierzigste    num type=ord value=48
neunundvierzigste    num type=ord value=49
fünfzigste           num type=ord value=50
einundfünfzigste     num type=ord value=51
zweiundfünfzigste    num type=ord value=52
dreiundfünfzigste    num type=ord value=53
vierundfünfzigste    num type=ord value=54
fünfundfünfzigste    num type=ord value=55
sechsundfünfzigste   num type=ord value=56
siebenundfünfzigste  num type=ord value=57
achtundfünfzigste    num type=ord value=58
neunundfünfzigste    num type=ord value=59
sechzigste           num type=ord value=60
einundsechzigste     num type=ord value=61
zweiundsechzigste    num type=ord value=62
dreiundsechzigste    num type=ord value=63
vierundsechzigste    num type=ord value=64
fünfundsechzigste    num type=ord value=65
sechsundsechzigste   num type=ord value=66
siebenundsechzigste  num type=ord value=67
achtundsechzigste    num type=ord value=68
neunundsechzigste    num type=ord value=69
siebzigste           num type=ord value=70
einundsiebzigste     num type=ord value=71
zweiundsiebzigste    num type=ord value=72
dreiundsiebzigste    num type=ord value=73
vierundsiebzigste    num type=ord value=74
fünfundsiebzigste    num type=ord value=75
sechsundsiebzigste   num type=ord value=76
siebenundsiebzigste  num type=ord value=77
achtundsiebzigste    num type=ord value=78
neunundsiebzigste    num type=ord value=79
achtzigste           num type=ord value=80
einundachtzigste     num type=ord value=81
zweiundachtzigste    num type=ord value=82
dreiundachtzigste    num type=ord value=83
vierundachtzigste    num type=ord value=84
fünfundachtzigste    num type=ord value=85
sechsundachtzigste   num type=ord value=86
siebenundachtzigste  num type=ord value=87
achtundachtzigste    num type=ord value=88
neunundachtzigste    num type=ord value=89
neunzigste           num type=ord value=90
einundneunzigste     num type=ord value=91
zweiundneunzigste    num type=ord value=92
dreiundneunzigste    num type=ord value=93
vierundneunzigste    num type=ord value=94
fünfundneunzigste    num type=ord value=95
sechsundneunzigste   num type=ord value=96
siebenundneunzigste  num type=ord value=97
achtundneunzigste    num type=ord value=98
neunundneunzigste    num type=ord value=99
siebente             num type=ord value=7 style=rare note=older variant of siebte
zwote                num type=ord value=2 style=colloquial
hundertste           num type=ord value=100
tausendste           num type=ord value=1000
millionste           num type=ord value=1000000

# ---------------------------------------------------------------- fractions and multiplicatives
anderthalb           num type=frac value=3/2
eineinhalb           num type=frac value=3/2
zweieinhalb          num type=frac value=5/2
drittel              num type=frac value=1/3
viertel              num type=frac value=1/4
achtel               num type=frac value=1/8
zehntel              num type=frac value=1/10
hundertstel          num type=frac value=1/100
tausendstel          num type=frac value=1/1000
einmal               num type=mult value=1 note=also the adverb einmal/mal (once, some day)
zweimal              num type=mult value=2
dreimal              num type=mult value=3
viermal              num type=mult value=4
fünfmal              num type=mult value=5
sechsmal             num type=mult value=6
siebenmal            num type=mult value=7
achtmal              num type=mult value=8
neunmal              num type=mult value=9
zehnmal              num type=mult value=10
elfmal               num type=mult value=11
zwölfmal             num type=mult value=12
zwanzigmal           num type=mult value=20
hundertmal           num type=mult value=100
tausendmal           num type=mult value=1000

# ---------------------------------------------------------------- ordinal adverbs
erstens              adv type=manner
zweitens             adv type=manner
drittens             adv type=manner
viertens             adv type=manner
fünftens             adv type=manner
sechstens            adv type=manner
siebtens             adv type=manner
achtens              adv type=manner
neuntens             adv type=manner
zehntens             adv type=manner
letztens             adv type=time|manner note=lastly; colloquial recently

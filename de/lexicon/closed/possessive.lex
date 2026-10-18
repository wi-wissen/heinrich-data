# Possessive determiners (det) and possessive pronouns (pron). Written clean-room by hand.
# det:  attributive use, declined like ein (mein Buch, meines Buches); a following adjective
#       takes the mixed declension (mein neues Buch, meine neuen Bücher).
# pron: substantival use, declined like einer (das ist meiner / meine / meins).
# person= is the person of the possessor; sein = masculine/neuter possessor, ihr = feminine or
# plural possessor, Ihr = polite. Elided forms (unsre, eure, unsrem) follow the full forms.

# ---------------------------------------------------------------- determiners
mein         det type=poss person=1 decl=ein
dein         det type=poss person=2 decl=ein
sein         det type=poss person=3 decl=ein note=possessor masculine or neuter
ihr          det type=poss person=3 decl=ein note=possessor feminine or plural
Ihr          det type=poss person=3 polite decl=ein note=polite address (Ihr Buch)
unser        det type=poss person=1 adj=mixed
             m=unser,unseres|unsres[rare],unserem|unsrem[rare]|unserm[rare],unseren|unsren[rare]|unsern[rare]
             f=unsere|unsre[rare],unserer|unsrer[rare],unserer|unsrer[rare],unsere|unsre[rare]
             n=unser,unseres|unsres[rare],unserem|unsrem[rare]|unserm[rare],unser
             pl=unsere|unsre[rare],unserer|unsrer[rare],unseren|unsren[rare]|unsern[rare],unsere|unsre[rare]
euer         det type=poss person=2 adj=mixed
             m=euer,eures|eueres[rare],eurem|euerem[rare],euren|eueren[rare]
             f=eure|euere[rare],eurer|euerer[rare],eurer|euerer[rare],eure|euere[rare]
             n=euer,eures|eueres[rare],eurem|euerem[rare],euer
             pl=eure|euere[rare],eurer|euerer[rare],euren|eueren[rare],eure|euere[rare]

# ---------------------------------------------------------------- pronouns
mein         pron type=poss person=1 decl=einer
dein         pron type=poss person=2 decl=einer
sein         pron type=poss person=3 decl=einer
ihr          pron type=poss person=3 decl=einer sense=poss
Ihr          pron type=poss person=3 polite decl=einer
unser        pron type=poss person=1
             m=unserer|unsrer[rare],unseres|unsres[rare],unserem|unsrem[rare]|unserm[rare],unseren|unsren[rare]|unsern[rare]
             f=unsere|unsre[rare],unserer|unsrer[rare],unserer|unsrer[rare],unsere|unsre[rare]
             n=unseres|unsres[rare],unseres|unsres[rare],unserem|unsrem[rare]|unserm[rare],unseres|unsres[rare]
             pl=unsere|unsre[rare],unserer|unsrer[rare],unseren|unsren[rare]|unsern[rare],unsere|unsre[rare]
euer         pron type=poss person=2
             m=eurer|euerer[rare],eures|eueres[rare],eurem|euerem[rare],euren|eueren[rare]
             f=eure|euere[rare],eurer|euerer[rare],eurer|euerer[rare],eure|euere[rare]
             n=eures|eueres[rare],eures|eueres[rare],eurem|euerem[rare],eures|eueres[rare]
             pl=eure|euere[rare],eurer|euerer[rare],euren|eueren[rare],eure|euere[rare]

# ---------------------------------------------------------------- invariable possessive pronouns
meinesgleichen   pron type=ind person=1 note=people like me
deinesgleichen   pron type=ind person=2
seinesgleichen   pron type=ind person=3
ihresgleichen    pron type=ind person=3
unseresgleichen  pron type=ind person=1
euresgleichen    pron type=ind person=2

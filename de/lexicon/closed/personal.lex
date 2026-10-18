# Personal, reflexive and reciprocal pronouns (pron). Written clean-room by hand.
# Tables: sg=/pl= without gender (ich, wir), m=/f=/n= for the 3rd person singular.
# The archaic genitives mein, dein, sein (gedenke mein) are tagged [archaic].
# The polite Sie is 3rd person plural with Polite=Form (it agrees with 3rd person plural verbs).
# The flag `letter` on second-person words adds the capitalised letter-salutation spellings
# (Du, Dich, Dir, Dein…; Ihr, Euch, Euer…) as forms tagged [letter]; see LEXICON_FORMAT.

# ---------------------------------------------------------------- personal pronouns
ich          pron type=prs person=1 sg=ich,meiner|mein[archaic],mir,mich
du           pron type=prs person=2 letter sg=du,deiner|dein[archaic],dir,dich
er           pron type=prs person=3 m=er,seiner|sein[archaic],ihm,ihn
sie          pron type=prs person=3 f=sie,ihrer,ihr,sie sense=fem
es           pron type=prs person=3 n=es,seiner|sein[archaic],ihm,es
wir          pron type=prs person=1 pl=wir,unser,uns,uns
ihr          pron type=prs person=2 letter pl=ihr,euer,euch,euch
sie          pron type=prs person=3 pl=sie,ihrer,ihnen,sie sense=pl
Sie          pron type=prs person=3 polite pl=Sie,Ihrer,Ihnen,Sie
             note=polite address, singular or plural meaning; verb in 3rd person plural

# ---------------------------------------------------------------- reflexive pronouns
# 1st/2nd person reflexives are the personal pronoun forms; they get their own lexemes with
# PronType=Rfl so rules can tell "ich wasche mich" from "er sieht mich".
ich          pron type=rfl person=1 sg=-,-,mir,mich sense=rfl
du           pron type=rfl person=2 letter sg=-,-,dir,dich sense=rfl
wir          pron type=rfl person=1 pl=-,-,uns,uns sense=rfl
ihr          pron type=rfl person=2 letter pl=-,-,euch,euch sense=rfl
sich         pron type=rfl person=3 cases=-,-,sich,sich note=3rd person singular and plural, also polite Sie

# ---------------------------------------------------------------- reciprocal
einander     pron type=rcp note=compounds with prepositions (miteinander, aufeinander) are adverbs

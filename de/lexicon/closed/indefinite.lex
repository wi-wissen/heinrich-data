# Indefinite, negative and total (collective) determiners and pronouns. Written clean-room by hand.
# adj= gives the declension of a following adjective: jeder gute (weak), einige gute (strong).
# Plural-only words have only a pl= table. Uninflected words (etwas, nichts, allerlei) have no table.

# ---------------------------------------------------------------- persons
man          pron type=ind person=3 sg=man,-,einem,einen note=dative and accusative are supplied by einer
jemand       pron type=ind sg=jemand,jemandes|jemands[rare],jemandem|jemand,jemanden|jemand
niemand      pron type=neg sg=niemand,niemandes|niemands[rare],niemandem|niemand,niemanden|niemand
irgendjemand pron type=ind sg=irgendjemand,irgendjemandes,irgendjemandem|irgendjemand,irgendjemanden|irgendjemand
jedermann    pron type=tot sg=jedermann,jedermanns,jedermann,jedermann
irgendwer    pron type=ind sg=irgendwer,-,irgendwem,irgendwen
wer          pron type=ind sense=ind style=colloquial sg=wer,-,wem,wen note=colloquial for jemand (ist da wer?)

# ---------------------------------------------------------------- things
etwas        pron type=ind
nichts       pron type=neg
irgendetwas  pron type=ind
irgendwas    pron type=ind style=colloquial
nix          pron type=neg style=colloquial

# ---------------------------------------------------------------- ein, kein, irgendein
ein          pron type=ind decl=einer pl=- note=einer, eine, eins/eines (einer von uns)
kein         det type=neg decl=ein
kein         pron type=neg decl=einer
irgendein    det type=ind decl=ein pl=-
irgendein    pron type=ind decl=einer pl=-
irgendwelcher det type=ind decl=dieser adj=weak|strong note=mostly plural (irgendwelche Leute)
welcher      pron type=ind sense=ind decl=dieser note=some, any (hast du welche?)

# ---------------------------------------------------------------- jeder, all, beide
jeder        det type=tot decl=dieser pl=-
             m=jeder,jedes|jeden,jedem,jeden
             n=jedes,jedes|jeden,jedem,jedes
             note=genitive jeden before a noun with -s (Anfang jeden Jahres)
jeder        pron type=tot decl=dieser pl=-
jeglicher    det type=tot decl=dieser
             m=jeglicher,jegliches|jeglichen,jeglichem,jeglichen
             n=jegliches,jegliches|jeglichen,jeglichem,jegliches
all          det type=tot decl=dieser stem=all adj=weak
             m=aller,alles|allen,allem,allen
             n=alles,alles|allen,allem,alles
             note=all die Leute: see sense=bare
all          det type=tot sense=bare note=uninflected before another determiner (all die Jahre, all das)
all          pron type=tot decl=dieser stem=all note=alles, alle (alle sind da, alles ist gut)
alledem      pron type=tot sg=-,-,alledem,- note=fused all + dem, only after a dative preposition (trotz alledem, bei alledem, von alledem)
beide        det type=tot adj=weak|strong pl=beide,beider,beiden,beide
beide        pron type=tot pl=beide,beider,beiden,beide n=beides,beides,beidem,beides
sämtlicher   det type=tot decl=dieser adj=weak|strong note=mostly plural (sämtliche Bücher)
sämtlicher   pron type=tot decl=dieser

# ---------------------------------------------------------------- quantity
einige       det type=ind decl=dieser stem=einig adj=strong note=singular use: einiger Aufwand, einiges Geld
einige       pron type=ind decl=dieser stem=einig note=einiges, einige
viele        det type=ind decl=dieser stem=viel adj=strong note=viele Menschen; singular use: vieles, vielem
viele        pron type=ind decl=dieser stem=viel note=vieles, viele (viele sind gekommen)
wenige       det type=ind decl=dieser stem=wenig adj=strong note=singular use: weniger Aufwand, weniges Geld
wenige       pron type=ind decl=dieser stem=wenig note=weniges, wenige (wenige sind gekommen)
wenig        det type=ind note=uninflected before a mass noun (wenig Geld, wenig Zeit); the adjective wenig is in adj/
wenig        pron type=ind note=uninflected (er weiß wenig); the adjective wenig is in adj/
etliche      det type=ind decl=dieser stem=etlich adj=strong
etliche      pron type=ind decl=dieser stem=etlich
mehrere      det type=ind adj=strong pl=mehrere,mehrerer,mehreren,mehrere
mehrere      pron type=ind pl=mehrere,mehrerer,mehreren,mehrere
mancher      det type=ind decl=dieser adj=weak|strong
             m=mancher,manches|manchen,manchem,manchen
             n=manches,manches|manchen,manchem,manches
mancher      pron type=ind decl=dieser
manch        det type=ind note=uninflected before ein or an adjective (manch ein Kind, manch guter Rat)
paar         det type=ind note=ein paar (a few); das Paar (a pair) is a noun
bisschen     det type=ind note=ein bisschen (a little)
bißchen      det type=ind spelling=old note=old spelling of bisschen
allerhand    det type=ind note=indeclinable, all kinds of (allerhand Ärger); colloquially also predicative (das ist allerhand)
allerhand    pron type=ind note=indeclinable (er weiß allerhand)
allerlei     det type=ind
mancherlei   det type=ind
vielerlei    det type=ind
keinerlei    det type=neg
beiderlei    det type=tot
was          pron type=ind sense=ind sg=was,-,-,was style=colloquial note=colloquial for etwas (ich habe was gesehen)

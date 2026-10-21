# Pronouns (format §6): personal pronouns incl. clitics and prepositional forms, demonstratives,
# possessives, relatives, interrogatives, indefinites. Written from own knowledge.

# --- personal: subject and prepositional forms ------------------------------------------------
yo           pron type=prs person=1 number=sg case=nom
tú           pron type=prs person=2 number=sg case=nom
él           pron type=prs person=3 case=nom forms=él,ella,ellos,ellas note=also after prepositions: para él, con ellas
ello         pron type=prs person=3 number=sg note=neuter: por ello, de ello
nosotros     pron type=prs person=1 case=nom forms=-,-,nosotros,nosotras
vosotros     pron type=prs person=2 case=nom forms=-,-,vosotros,vosotras
usted        pron type=prs person=3 number=sg polite
ustedes      pron type=prs person=3 number=pl polite
mí           pron type=prs person=1 number=sg prepcase
ti           pron type=prs person=2 number=sg prepcase
sí           pron type=rfl person=3 prepcase
conmigo      pron type=prs person=1 number=sg fused=con+mí
contigo      pron type=prs person=2 number=sg fused=con+ti
consigo      pron type=rfl person=3 fused=con+sí

# --- personal: clitics ------------------------------------------------------------------------
me           pron type=prs|rfl person=1 number=sg case=acc|dat
te           pron type=prs|rfl person=2 number=sg case=acc|dat
nos          pron type=prs|rfl person=1 number=pl case=acc|dat
os           pron type=prs|rfl person=2 number=pl case=acc|dat
lo           pron type=prs person=3 case=acc forms=lo,la,los,las note=lo also neuter: lo sé
le           pron type=prs person=3 number=sg case=dat note=accusative le for a male person (leísmo) is accepted in Spain; left to the grammar rules
les          pron type=prs person=3 number=pl case=dat
se           pron type=prs|rfl person=3 case=acc|dat note=prs reading: se for le/les before lo, la (se lo doy)

# --- demonstratives ---------------------------------------------------------------------------
aquel        pron type=dem forms=aquel|aquél[trad],aquella|aquélla[trad],aquellos|aquéllos[trad],aquellas|aquéllas[trad]
aquello      pron type=dem number=sg note=neuter
ese          pron type=dem forms=ese|ése[trad],esa|ésa[trad],esos|ésos[trad],esas|ésas[trad]
eso          pron type=dem number=sg note=neuter
este         pron type=dem forms=este|éste[trad],esta|ésta[trad],estos|éstos[trad],estas|éstas[trad]
esto         pron type=dem number=sg note=neuter

# --- possessives (with the article: el mío) ---------------------------------------------------
mío          pron type=poss person=1 psor=sg forms=mío,mía,míos,mías
tuyo         pron type=poss person=2 psor=sg forms=tuyo,tuya,tuyos,tuyas
suyo         pron type=poss person=3 forms=suyo,suya,suyos,suyas
nuestro      pron type=poss person=1 psor=pl forms=nuestro,nuestra,nuestros,nuestras
vuestro      pron type=poss person=2 psor=pl forms=vuestro,vuestra,vuestros,vuestras

# --- relatives and interrogatives -------------------------------------------------------------
cual         pron type=rel forms=cual,cual,cuales,cuales note=with the article: el cual, las cuales
cuál         pron type=int forms=cuál,cuál,cuáles,cuáles
cuanto       pron type=rel forms=cuanto,cuanta,cuantos,cuantas note=todo cuanto tengo
cuánto       pron type=int forms=cuánto,cuánta,cuántos,cuántas
que          pron type=rel
qué          pron type=int
quien        pron type=rel forms=quien,quien,quienes,quienes
quién        pron type=int forms=quién,quién,quiénes,quiénes

# --- indefinites, negatives, quantifiers ------------------------------------------------------
algo         pron type=ind
alguien      pron type=ind
alguno       pron type=ind forms=alguno,alguna,algunos,algunas
ambos        pron type=tot forms=-,-,ambos,ambas
bastante     pron type=ind forms=bastante,bastante,bastantes,bastantes
cualquiera   pron type=ind forms=cualquiera,cualquiera,cualesquiera,cualesquiera
demás        pron type=ind note=lo demás, los demás
demasiado    pron type=ind forms=demasiado,demasiada,demasiados,demasiadas
mucho        pron type=ind forms=mucho,mucha,muchos,muchas
nada         pron type=neg
nadie        pron type=neg
ninguno      pron type=neg forms=ninguno,ninguna,ningunos,ningunas
otro         pron type=ind forms=otro,otra,otros,otras
poco         pron type=ind forms=poco,poca,pocos,pocas
quienquiera  pron type=ind forms=quienquiera,quienquiera,quienesquiera,quienesquiera
tal          pron type=dem forms=tal,tal,tales,tales note=no dijo tal; un tal
tanto        pron type=ind forms=tanto,tanta,tantos,tantas
todo         pron type=tot forms=todo,toda,todos,todas
uno          pron type=ind forms=uno,una,unos,unas note=uno nunca sabe; unos y otros
varios       pron type=ind forms=-,-,varios,varias

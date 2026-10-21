# Grammar adverbs (format §6, AUTHORING.md §2): negation and affirmation, degree, interrogative and
# relative adverbs, place and time deixis. Content adverbs are in adv/<letter>.lex.
# Written from own knowledge. type: neg, aff, deg, int, rel, dem.

# --- negation and affirmation -----------------------------------------------------------------
jamás        adv  type=neg
no           adv  type=neg
nunca        adv  type=neg
sí           adv  type=aff
también      adv  type=aff
tampoco      adv  type=neg

# --- degree -----------------------------------------------------------------------------------
algo         adv  type=deg note=algo cansado
apenas       adv  type=deg
bastante     adv  type=deg
casi         adv  type=deg
cuan         adv  type=rel style=literary note=tan … cuan; cuan largo era
cuán         adv  type=int style=literary note=¡cuán grande!
demasiado    adv  type=deg
más          adv  type=deg
medio        adv  type=deg note=medio dormido
menos        adv  type=deg
mucho        adv  type=deg
muy          adv  type=deg
nada         adv  type=deg|neg note=no es nada fácil
poco         adv  type=deg
tan          adv  type=deg
tanto        adv  type=deg

# --- interrogative and relative ---------------------------------------------------------------
adonde       adv  type=rel
adónde       adv  type=int
como         adv  type=rel note=as relative adverb (la manera como lo dijo) and approximately (como diez)
cómo         adv  type=int
cuando       adv  type=rel note=relative adverb (el día cuando llegó); the conjunction is in conjunctions.lex
cuándo       adv  type=int
cuanto       adv  type=rel note=cuanto más, mejor; en cuanto
cuánto       adv  type=int
donde        adv  type=rel
dónde        adv  type=int

# --- place and time deixis --------------------------------------------------------------------
acá          adv  type=dem
ahí          adv  type=dem
ahora        adv  type=dem
allá         adv  type=dem
allí         adv  type=dem
anoche       adv  type=dem
anteanoche   adv  type=dem
anteayer     adv  type=dem
aquí         adv  type=dem
así          adv  type=dem
aun          adv  type=deg note=even (aun así; ni aun); aún is still
aún          adv  type=dem note=still, yet (aún no ha llegado)
ayer         adv  type=dem
entonces     adv  type=dem
hoy          adv  type=dem
mañana       adv  type=dem
todavía      adv  type=dem
ya           adv  type=dem

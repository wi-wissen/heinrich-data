# Relative and interrogative pronouns and determiners. Written clean-room by hand.
# Interrogative and relative adverbs (wo, wann, warum, worauf …) are in adverbs.lex.
# The relative pronoun der has no derer (that is demonstrative only); welcher as a relative
# pronoun has no genitive (dessen/deren are used instead).

# ---------------------------------------------------------------- relative
der          pron type=rel sense=rel
             m=der,dessen,dem,den
             f=die,deren,der,die
             n=das,dessen,dem,das
             pl=die,deren,denen,die
welcher      pron type=rel sense=rel
             m=welcher,-,welchem,welchen
             f=welche,-,welcher,welche
             n=welches,-,welchem,welches
             pl=welche,-,welchen,welche
             note=formal or to avoid die die / das das
wer          pron type=rel sense=rel sg=wer,wessen,wem,wen note=free relative (wer das sagt, irrt)
was          pron type=rel sense=rel sg=was,wessen,-,was note=after alles, nichts, etwas, das, superlatives and clauses (das Beste, was …)

# ---------------------------------------------------------------- interrogative
wer          pron type=int sg=wer,wessen|wes[archaic],wem,wen
was          pron type=int sg=was,wessen|wes[archaic],-,was note=dative is replaced by a preposition or wem
welcher      det type=int decl=dieser
             m=welcher,welches|welchen,welchem,welchen
             n=welches,welches|welchen,welchem,welches
welcher      pron type=int decl=dieser
welch        det type=int note=uninflected in exclamations before ein or an adjective (welch ein Glück!, welch schöner Tag!)

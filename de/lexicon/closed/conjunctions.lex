# Conjunctions. Written clean-room by hand. These attributes drive the comma and das/dass rules.
#
# cconj (coordinating) – comma=
#   required  a comma always stands before it when it joins words, phrases or clauses
#             (adversative aber, sondern, doch, jedoch; causal denn)
#   no        no comma when it joins words, phrases or subordinate clauses (und, oder, sowie,
#             entweder … oder, weder … noch); before a full main clause a comma is optional
#             (Amtliches Regelwerk §73)
# sconj (subordinating) – type= contains one of
#   clause    introduces a verb-final subordinate clause, which is set off by commas
#   inf       introduces an infinitive with zu, which is set off by a comma (um, ohne, statt,
#             anstatt, außer, als; §75)
#   cmp       comparison particle (größer als, so groß wie): no comma unless a clause follows
#   plus the meaning (temporal, causal, conditional, concessive, final, consecutive, modal,
#   adversative, content, interrogative, proportional).
# pair= names the correlative partner (entweder … oder, je … desto).

# ---------------------------------------------------------------- coordinating
und          cconj comma=no type=copulative
oder         cconj comma=no type=disjunctive
sowie        cconj comma=no type=copulative
beziehungsweise cconj comma=no type=disjunctive
bzw.         cconj comma=no type=disjunctive note=abbreviation of beziehungsweise
respektive   cconj comma=no type=disjunctive
sowohl       cconj comma=no type=copulative pair=als|wie note=sowohl … als auch / sowohl … wie auch
weder        cconj comma=no type=copulative pair=noch note=weder … noch
noch         cconj comma=no type=copulative note=second part of weder … noch; the adverb noch is in adverbs.lex
entweder     cconj comma=no type=disjunctive pair=oder note=entweder … oder
aber         cconj comma=required type=adversative note=no comma when aber stands inside the clause (er aber blieb)
sondern      cconj comma=required type=adversative note=after a negation (nicht …, sondern)
doch         cconj comma=required type=adversative note=as a conjunction at the start of a clause; the particle doch is in particles.lex
jedoch       cconj comma=required type=adversative note=also a conjunctional adverb (adverbs.lex)
allein       cconj comma=required type=adversative style=archaic note=elevated for aber (ich hoffte, allein es kam anders)
denn         cconj comma=required type=causal note=main-clause word order; the particle denn is in particles.lex

# ---------------------------------------------------------------- subordinating
als          sconj type=clause|cmp|inf|temporal note=als er kam (clause); größer als (cmp); als zu (inf)
bevor        sconj type=clause|temporal
bis          sconj type=clause|temporal
da           sconj type=clause|causal note=also an adverb (adverbs.lex)
damit        sconj type=clause|final note=also a pronominal adverb (adverbs.lex)
dass         sconj type=clause|content
daß          sconj type=clause|content spelling=old
ehe          sconj type=clause|temporal
falls        sconj type=clause|conditional
indem        sconj type=clause|modal
indes        sconj type=clause|temporal|adversative
indessen     sconj type=clause|temporal|adversative
insofern     sconj type=clause|conditional note=often insofern als; also an adverb
insoweit     sconj type=clause|conditional
je           sconj type=clause|proportional pair=desto|umso note=je mehr, desto besser
nachdem      sconj type=clause|temporal|causal
ob           sconj type=clause|interrogative note=indirect question; als ob (comparison)
obgleich     sconj type=clause|concessive
obschon      sconj type=clause|concessive style=rare
obwohl       sconj type=clause|concessive
obzwar       sconj type=clause|concessive style=rare
ohne         sconj type=inf note=ohne zu; ohne dass is ohne + dass
seit         sconj type=clause|temporal
seitdem      sconj type=clause|temporal note=also an adverb
sobald       sconj type=clause|temporal
sodass       sconj type=clause|consecutive note=also written so dass
sodaß        sconj type=clause|consecutive spelling=old
sofern       sconj type=clause|conditional
solang       sconj type=clause|temporal style=rare
solange      sconj type=clause|temporal
sooft        sconj type=clause|temporal
soviel       sconj type=clause|modal note=soviel ich weiß; the quantity is written so viel
soweit       sconj type=clause|conditional note=soweit ich weiß; the adverbial phrase is written so weit
statt        sconj type=inf note=statt zu; statt dass
anstatt      sconj type=inf note=anstatt zu; anstatt dass
außer        sconj type=inf note=außer zu; außer dass / außer wenn
um           sconj type=inf|final note=um zu
während      sconj type=clause|temporal|adversative
weil         sconj type=clause|causal
wenn         sconj type=clause|conditional|temporal
wenngleich   sconj type=clause|concessive
wie          sconj type=clause|cmp|modal|temporal note=so groß wie (cmp); wie er sagte (clause)
wohingegen   sconj type=clause|adversative
zumal        sconj type=clause|causal note=also an adverb

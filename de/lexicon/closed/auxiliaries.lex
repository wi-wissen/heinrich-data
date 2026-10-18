# Auxiliary and modal verbs (aux). Written clean-room by hand.
# Modal verbs have no imperative (imp=-,-); their Konjunktiv II is written explicitly because
# sollen/wollen keep the preterite vowel (sollte, wollte).

# ---------------------------------------------------------------- perfect / passive auxiliaries
sein         aux class=irregular perf=sein pp=gewesen
             pres=bin,bist,ist,sind,seid,sind
             past=war,warst,war,waren,wart,waren
             subj1=sei,seist|seiest,sei,seien,seiet,seien
             subj2=wäre,wärst|wärest,wäre,wären,wärt|wäret,wären
             imp=sei,seid
haben        aux class=mixed pres=habe,hast,hat,haben,habt,haben past=hatte pp=gehabt subj2=hätte perf=haben
werden       aux class=strong pres=werde,wirst,wird,werden,werdet,werden
             past=wurde|ward[archaic],wurdest|wardst[archaic],wurde|ward[archaic],wurden,wurdet,wurden
             subj2=würde imp=werde,werdet pp=geworden|worden perf=sein
             note=pp worden only in the passive (ist gelobt worden)

# ---------------------------------------------------------------- modal verbs
dürfen       aux class=modal 3sg=darf past=durfte pp=gedurft subj2=dürfte imp=-,- perf=haben
können       aux class=modal 3sg=kann past=konnte pp=gekonnt subj2=könnte imp=-,- perf=haben
mögen        aux class=modal 3sg=mag past=mochte pp=gemocht subj2=möchte imp=-,- perf=haben
             note=möchte (Konjunktiv II) is also used as a present-tense modal: ich möchte gehen
müssen       aux class=modal 3sg=muss past=musste pp=gemusst subj2=müsste imp=-,- perf=haben
sollen       aux class=modal 3sg=soll past=sollte pp=gesollt subj2=sollte imp=-,- perf=haben
wollen       aux class=modal 3sg=will past=wollte pp=gewollt subj2=wollte imp=-,- perf=haben

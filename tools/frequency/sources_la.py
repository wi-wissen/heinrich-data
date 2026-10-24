"""Hand-written selection of public-domain Latin texts for la/frequency (bibliographic knowledge only).

Wikisource pages are grouped by the `Scriptor` field of their `titulus`/`titulus2` header (inherited from the
parent page for sub-pages). Three groups, each a column of la/frequency/forms.tsv:
  prose  - classical and post-classical prose, non-Christian, written before about AD 200
  poetry - verse of the same period (epic, elegy, lyric, satire, drama, fable)
  late   - the Vulgate (Clementine edition, 1592) and Latin writers from about AD 200 to 1500:
           Church Fathers, late antique and medieval authors
Texts written after 1500 (Neo-Latin, papal documents, modern Latin) are not counted.
"""

PROSE_AUTHORS = [
    "Marcus Tullius Cicero", "Quintus Tullius Cicero", "Gaius Iulius Caesar", "Aulus Hirtius",
    "Gaius Sallustius Crispus", "Cornelius Nepos", "Titus Livius", "Marcus Terentius Varro", "Marcus Porcius Cato",
    "Marcus Vitruvius Pollio", "Velleius Paterculus", "Valerius Maximus", "Annaeus Seneca maior",
    "Lucius Annaeus Seneca", "Aulus Cornelius Celsus", "Lucius Iunius Moderatus Columella", "Quintus Curtius Rufus",
    "Gaius Plinius Secundus", "Gaius Plinius Caecilius Secundus", "Marcus Fabius Quintilianus",
    "Publius Cornelius Tacitus", "Gaius Suetonius Tranquillus", "Florus", "Aulus Gellius", "Lucius Apuleius",
    "Marcus Cornelius Fronto", "Petronius Arbiter", "Sextus Iulius Frontinus", "Marcus Iunianus Iustinus",
    "Hyginus Mythographus", "Gaius", "Gaius Iulius Caesar Octavianus Augustus",
]
POETRY_AUTHORS = [
    "Quintus Ennius", "Lucius Livius Andronicus", "Titus Maccius Plautus", "Publius Terentius Afer",
    "Titus Lucretius Carus", "Gaius Valerius Catullus", "Publius Vergilius Maro", "Quintus Horatius Flaccus",
    "Albius Tibullus", "Sextus Aurelius Propertius", "Publius Ovidius Naso", "Marcus Manilius", "Phaedrus",
    "Marcus Annaeus Lucanus", "Aulus Persius Flaccus", "Gaius Valerius Flaccus", "Publius Papinius Statius",
    "Silius Italicus", "Marcus Valerius Martialis", "Decimus Iunius Iuvenalis", "Publilius Syrus",
    "Titus Calpurnius Siculus",
]
# Seneca's tragedies are verse: counted as poetry although the author is listed as prose.
SENECA_TRAGEDIES = ["Agamemnon", "Hercules Oetaeus", "Hercules furens", "Medea", "Octavia", "Oedipus", "Phaedra",
                    "Phoenissae", "Thyestes", "Troades"]
# Late antique and medieval writers (c. AD 200 - 1500) who wrote in Latin. Translations of Greek authors
# made after 1500 are not counted, so Greek authors are not listed.
LATE_AUTHORS = [
    # 3rd-6th century
    "Quintus Septimius Florens Tertullianus", "Minucius Felix", "Cyprianus Carthaginiensis", "Novatianus",
    "Commodianus Gazaeus", "Arnobius", "Lucius Caelius Firmianus Lactantius", "Iulius Firmicus Maternus",
    "Hilarius Pictaviensis", "Gaius Marius Victorinus", "Ambrosius", "Ambrosiaster", "Sophronius Eusebius Hieronymus",
    "Hieronymus Stridonensis", "Rufinus Aquileiensis", "Aurelius Augustinus", "Augustinus Hipponensis",
    "Paulinus Nolanus", "Sulpicius Severus", "Aurelius Prudentius Clemens", "Decimus Magnus Ausonius", "Ausonius",
    "Claudius Claudianus", "Q. Aurelius Symmachus", "Ammianus Marcellinus", "Ambrosius Theodosius Macrobius",
    "Maurus Servius Honoratus", "Eutropius", "Aurelius Victor", "Flavius Vegetius Renatus", "Gaius Iulius Solinus",
    "Rufius Festus Avienus", "Aelius Spartianus", "Iulius Capitolinus", "Martianus Capella", "Paulus Orosius",
    "Joannes Cassianus", "Prosper Tiro Aquitanus", "Salvianus Massiliensis", "Eucherius Lugdunensis",
    "Vincentius Lerinensis", "Petrus Chrysologus", "Leo I Papa", "Leo I", "Maximus Taurinensis",
    "Zeno Veronensis", "Gaudentius Brixiensis", "Philastrius Brixiensis", "Optatus Milevitanus",
    "Lucifer Calaritanus", "Eusebius Vercellensis", "Pelagius Britannicus", "Tichonius", "Faustus Rhegiensis",
    "Sidonius Apollinaris", "Victor Vitensis", "Vigilius Tapsensis", "Fulgentius Ruspensis",
    "Anicius Manlius Torquatus Severinus Boethius", "Ennodius Ticinensis", "Avitus Viennensis",
    "Caesarius Arelatensis", "Flavius Magnus Aurelius Cassiodorus Senator", "Cassiodorus Vivariensis",
    "Benedictus de Nursia", "Iordanes", "Flavius Cresconius Corippus", "Dracontius Blossius", "Arator",
    "Venantius Fortunatus", "Gregorius Turonensis", "Gregorius Magnus", "Gregorius I", "Primasius Adrumetanensis",
    "Facondus Hermianensis", "Martinus Bracarensis", "Eugyppius", "Vettius Aquilinus Juvencus", "Cyprianus Gallus",
    "Paulinus Petricordiensis", "Possidius Calamensis", "Gildas Sapiens", "Dionysius Exiguus", "Columbanus",
    "Iulianus Pomerius", "Mamertus Claudianus", "Victorinus Petavionensis",
    # 7th-11th century
    "Isidorus Hispalensis", "Braulio Caesaraugustanus", "Hildefonsus Toletanus", "Julianus Toletanus",
    "Taio Caesaraugustianus", "Fredegarius Scholasticus Burgundiae", "Jonas Bobiensis", "Adamnanus Hiensis",
    "Aldhelmus Schireburnensis", "Beda Venerabilis", "Bonifacius Moguntinus", "Paulus Diaconus", "Alcuinus",
    "Paulinus Aquileiensis", "Theodulfus", "Carolus Magnus", "Eginhardus", "Smaragdus", "Benedictus Anianensis",
    "Rabanus Maurus", "Walafridus Strabo", "Agobardus Lugdunensis", "Claudius Taurinensis", "Ionas Aurelianensis",
    "Amalarius Fortunatus Trevirensis", "Paschasius Radbertus", "Ratramnus Corbeiensis", "Lupus Ferrariensis",
    "Hincmarus Rhemensis", "Hincmarus Remensis", "Prudentius Trecensis", "Florus Lugdunensis", "Amulo Lugdunensis",
    "Iohannes Scotus Eriugena", "Sedulius Scotus", "Haymo Halberstatensis", "Angelomus Luxovensis",
    "Christianus Druthmarus", "Freculphus Lexovensis", "Ado Viennensis", "Usuardus Sangermanensis",
    "Notkerus Balbulus", "Regino Prumiensis", "Hucbaldus S. Amandi", "Remigius Antissiodorensis",
    "Hericus Antissiodorensis", "Atto Vercellensis", "Ratherius Veronensis", "Odo Cluniacensis",
    "Liutprandus Cremonensis", "Hrotsvitha Gandeshemensis", "Widukindus Corbeiensis", "Flodoardus Remensis",
    "Richerus", "Abbo Floriacensis", "Aimoinus Floriacensis", "Gerbertus Auriliacensis", "Silvester II",
    "Thietmarus Merseburgensis", "Fulbertus Carnotensis", "Rodulphus Glaber", "Dudo Sancti Quintini",
    "Ermoldus Nigellus", "Agnellus Ravennatensis", "Anastasius bibliothecarius", "Nicolaus I", "Ioannes VIII",
    "Wandalbertus Prumiensis", "Candidus Fuldensis", "Dungalus Reclusus", "Grimaldus Sangallensis",
    "Adso Dervensis", "Heregerius Lobiensis", "Folcuinus Laubiensis", "Erchembertus Cassinensis",
    "Audoenus Rothomagensis", "Gregorius VII", "Landulfus Sagax",
    # 12th-15th century
    "Anselmus Cantuariensis", "Anselmus Laudunensis", "Petrus Abaelardus", "Bernardus Claraevallensis",
    "Hugo de Sancto Victore", "Petrus Comestor", "Alanus ab Insulis", "Bernardus Silvestris", "Otto Frisingensis",
    "Guillelmus Tyrensis", "Albericus Aquensis", "Baldericus", "Galfridus Monemutensis", "Henricus Huntendunensis",
    "Gaufridus Malaterra", "Falco Beneventanus", "Hugo Falcandus", "Radulfus Cadomensis", "Saxo Grammaticus",
    "Gualterus de Castellione", "Nigellus de Longo Campo", "Andreas Capellanus", "Innocentius III", "Gregorius IX",
    "Eugenius III", "Innocentius II", "Paschalis II", "Urbanus II", "Calixtus II", "Alexander II", "Adrianus IV",
    "Albertus Magnus", "Thomas Aquinas", "Bonaventura", "Robertus Grosseteste", "Franciscus Baco",
    "Iohannes Duns Scotus", "Guillelmus de Ockham", "Ioannes Buridanus", "Iacobus de Voragine",
    "Albertanus Brixiensis", "Eberhardus Bethuniensis", "Birgitta de Suecia", "Dantes Aligherius",
    "Franciscus Petrarca", "Francesco Petrarca", "Giovanni Boccaccio", "Iohannes Boccacius", "Thomas a Kempis",
    "Nicolaus Cusanus", "Poggius Bracciolinus", "Laurentius Valla", "Pius II", "Petrus Zittaviensis",
    "Henricus Institor", "Eckbertus Schonaugiensis", "Bernardus Cluniacensis", "Gislebertus Porretanus",
]
# Root titles of Wikisource works not counted: interlinear or bilingual school editions, duplicates of a text
# counted from another page or from Gutenberg, works whose transmitted text is a later forgery.
EXCLUDE_WORKS = [
    "Cornelii Nepotis Vitae (Hamilton)", "Cornelli Nepotis Vitae (Hamilton)",   # interlinear Latin-English
    "Naturalis Historiæ (trad. Littré)",                                        # French translation
    "Naturalis historia",                                                       # duplicate of Naturalis Historia
    "Commentarii de bello Gallico (Towle-Jenks, 1908)",                          # school edition, notes
    "Carmina (Horatius)", "Epodi", "Carmen Saeculare",                          # counted from Gutenberg #9646
    "Aeneis",                                                                   # counted from Gutenberg #227
    "Cato maior de senectute",                                                  # counted from Gutenberg #14945
    "De Catilinae coniuratione",                                                # counted from Gutenberg #7402
    "Carmina (Catullus, ed. Merrill)", "Carmina (Catullus, ed. Cornish)",       # counted from Gutenberg #23294
    "Saturae (Persius, Monti)", "Saturae (Persius, Raoul)", "Saturae (Iuvenalis, Vescovi)",  # translations
    "Saturae (Horatius, Raoul)", "Georgica (Hachette)",
]
# Vulgate: only the Clementine edition (1592); the pages "Liber ... (Hieronymus)" follow a modern critical text.
VULGATE_PREFIX = "Vulgata Clementina/"
VULGATE_SKIP = ["Praefatio"]

# Proofread page sets (Wikisource "Pagina:" namespace) counted directly: index name, group, author, first and
# last page of the author's text (title pages and the editors' preface left out; footnotes are <ref> and dropped).
PAGINA_SETS = [
    ("P. Terenti Afri Comoediae (Kauer-Lindsay 1926).djvu", "poetry", "Publius Terentius Afer", 17, 345),
    ("T. Livii Patavini quæ exstant omnia opera, I.djvu", "prose", "Titus Livius", 1, 464),  # Lemaire, 1822
]

# Gutenberg books (gutenberg.org, plain text), counted between a start and an end line (first match, regex),
# footnote blocks "[n] ..." removed. They replace Wikisource pages that name a source we do not use.
GUTENBERG = [
    (227, "poetry", "Publius Vergilius Maro", "Aeneis", r"^PUBLI VERGILI MARONIS", None),
    (9646, "poetry", "Quintus Horatius Flaccus", "Carmina, Carmen saeculare, Epodi", r"^Q\. HORATII FLACCI", None),
    (7402, "prose", "Gaius Sallustius Crispus", "De Catilinae coniuratione", r"^BELLUM CATILINARIUM\.",
     r"^C\. SALLUSTII CRISPI\s*$"),
    (23294, "poetry", "Gaius Valerius Catullus", "Carmina, ed. Ellis", r"^CATVLLI CARMINA\s*$", r"^INDEX NOMINVM"),
    (14945, "prose", "Marcus Tullius Cicero", "Cato maior de senectute", r"^DE SENECTUTE\.", r"^NOTES TO CATO MAIOR"),
]

# Per-author cap for the late group (tokens); works of an author are taken in a fixed pseudo-random order
# until the cap is reached, so that a few prolific writers (Augustine, Rabanus Maurus) do not dominate.
LATE_CAP = 60_000

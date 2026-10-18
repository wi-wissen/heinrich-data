# heinrich-data

Sprachdaten für die Heinrich-Engine (`wi-wissen/Heinrich`): eigenes, im Clean-Room erzeugtes Lexikon,
Build-Skripte und fertige Sprachpakete.

## Regeln
- **Nur eigene Daten oder Daten mit permissiver Lizenz** (MIT, BSD, Apache-2.0, CC0, CC BY), die
  kommerzielle Nutzung erlauben. Jede Quelle in `SOURCES.md` mit Lizenz und Herkunft.
- **Keine** CC-BY-SA-, GPL-, LGPL- oder NC-Daten – auch nicht auszugsweise. Vergleichslexika
  (german-pos-dict, Wiktionary, UniMorph, DEMorphy …) werden nur außerhalb des Repos zur Messung genutzt.
- **Keine Grammatikregeln** hier – die liegen im Engine-Repo.
- Lexikoneinträge werden nach dem Clean-Room-Verfahren erstellt (siehe `Heinrich/docs/PLAN.md` §6).

## Geplante Struktur
- `de/lexicon/` – Lemmata mit Flexionsangaben (Textformat, gut diffbar)
- `de/closed/` – geschlossene Wortklassen (Artikel, Pronomen, Präpositionen …), von Hand
- `de/phon/` – Ausspracheausnahmen
- `tools/` – Build-Skripte (Lexikon → FST-Pakete)
- `packs/` – Build-Ausgabe (nicht eingecheckt, Releases)

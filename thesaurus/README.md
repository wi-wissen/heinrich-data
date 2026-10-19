# Thesaurus sources (third-party, separate licences)

This folder is an **exception** to the rules of this repository (owner decision, 2026-10-19). It holds two
third-party thesauri, **unchanged as downloaded**, as the input of Heinrich's optional thesaurus packs
(`de-thes.pack`, `en-thes.pack`, `en-gloss.pack`). The conversion and the pack builder are our own code in
`wi-wissen/Heinrich` (`tools/build-packs.sh`, `heinrich pack build-thes`).

| Folder | Source | Version | Licence | Packs |
|---|---|---|---|---|
| `de-openthesaurus/` | OpenThesaurus, https://www.openthesaurus.de | text export of 2026-10-18 | **CC BY-SA 4.0** (chosen by us; the source offers CC BY-SA 4.0 or LGPL 2.1) | `de-thes.pack` (CC BY-SA 4.0) |
| `en-oewn/` | Open English WordNet, https://en-word.net | 2025 | CC BY 4.0 | `en-thes.pack`, `en-gloss.pack` (CC BY 4.0) |

Rules for this folder:

- **Nothing from here flows into any other pack or into our own data.** Our lexicon, frequency lists, name
  lists and rules never take words, groups, markings or definitions from these files. In the other direction,
  the thesaurus packs carry only what comes from these files: our own data (frequencies, parts of speech,
  lexicon membership) is combined with them at run time in the engine, not written into the packs.
- **Clean-room:** these are third-party lexica. Lexicon authors (CLAUDE.md rule 2 in `wi-wissen/Heinrich`)
  must not read this folder or the thesaurus packs.
- Files stay byte-identical to the download (checksums in each README). An update replaces the file, the
  version, the date and the checksum in the README in one commit.

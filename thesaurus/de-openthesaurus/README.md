# OpenThesaurus (German)

| | |
|---|---|
| Source | OpenThesaurus – Deutscher Thesaurus, https://www.openthesaurus.de (Daniel Naber and contributors) |
| Download | https://www.openthesaurus.de/export/OpenThesaurus-Textversion.zip (linked from https://www.openthesaurus.de/about/download) |
| Version | text export "Automatically generated 2026-10-18 23:01" (header of `openthesaurus.txt`) |
| Retrieved | 2026-10-19 |
| `OpenThesaurus-Textversion.zip` sha256 | `15614ed4c6cf45751fe0efc48b0d0c465253926d940ca95837f94e228f784fd0` (1,608,273 bytes) |
| `openthesaurus.txt` (inside the zip) sha256 | `e676baccc2f9de61c0a1249d06c824ef7543525ceb740c92b51b42daca694a51` (4,068,341 bytes, 48,546 synonym groups) |
| Licence used by us | **Creative Commons Attribution-ShareAlike 4.0 International** (`LICENSE-CC-BY-SA-4.0.txt`) |

**Licence choice.** The download page offers the data under CC BY-SA 4.0 *or* LGPL 2.1 at the user's
choice; `licence-statement-2026-10-19.txt` keeps the wording of the page on the day of the download. The
header inside `openthesaurus.txt` and the `LICENSE.txt` of the zip name only the LGPL; that text is kept as
`LICENSE-LGPL-2.1.txt` because it is part of the original download. The project owner chose CC BY-SA 4.0
(2026-10-19): it attaches no "source code" obligation to the derived pack.

**What this means for us** (owner decision, exception to CLAUDE.md rule 3 in `wi-wissen/Heinrich`):

- `de-thes.pack` and the readable prepared version of the data are adaptations and are published under
  CC BY-SA 4.0, separately from the engine and from all other packs, clearly marked, with the source
  `openthesaurus.de` linked, the licence text embedded (section `LICN`) and a note that the data was changed.
- Nothing from OpenThesaurus flows into the engine, the rules, our lexicon or any other pack.

**Format** (for the converter): UTF-8 lines, `#` comments; one synonym group per line, terms separated by
`;`. Terms may carry markings in parentheses, e.g. `(ugs.)`, `(fachspr.)`, `(veraltet)`, `(derb)`,
`(vulg.)`, `(geh.)`, regional markings, and optional parts such as `(sich)`, `(etwas)`; terms ending in
`...` are word-formation elements.

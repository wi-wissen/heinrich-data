#!/usr/bin/env python3
"""Count Latin word forms in public-domain texts from Latin Wikisource and Project Gutenberg.

Usage: count_la.py WORKDIR DUMP_XML_BZ2 [GUTENBERG_DIR]
  DUMP_XML_BZ2   lawikisource-<date>-pages-articles.xml.bz2 from dumps.wikimedia.org (streamed)
  GUTENBERG_DIR  directory with pg<id>.txt for the books in sources_la.GUTENBERG (downloaded with curl,
                 one at a time); without it the Gutenberg books are skipped
Writes WORKDIR/{prose,poetry,late}/<author>.tsv (form, count, sentence-initial count) for merge.py and
WORKDIR/works.tsv (group, author, work, source, pages, tokens). Only counts are written; texts stay in memory.

Selection and groups: sources_la.py. Pages whose own header or text, or the header of a parent page, names
Perseus, The Latin Library, Corpus Corporum or the PHI Latin texts as source are not counted (Heinrich
docs/LATIN.md L-D5).
"""
import bz2, hashlib, html, os, re, sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tok
import sources_la as S

GROUPS = ("prose", "poetry", "late")
# Sources we do not use (L-D5): named in a Fons/Editio field, as a link, or as a credit line copied with the text.
BAD_SOURCE = re.compile(r"perseus\.tufts|perseus digital|perseus project|\|\s*Perseus\s*\]|\[[^\]]*\bPerseus\]|"
                        r"thelatinlibrary|latin\s+library|mlat\.uzh|corpus\s+corporum|packhum|\bPHI\b", re.I)
HEADER = re.compile(r"\{\{\s*[Tt]itulus2?\b(.*?)\n?\}\}", re.S)


def header(text):
    m = HEADER.search(text[:8000])
    return m.group(1) if m else None


def field(h, name):
    m = re.search(r"\|\s*" + name + r"\s*=\s*([^|\n]*)", h or "")
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------- wikitext cleaning
KEEP_TPL = {"sc", "c", "center", "centre", "larger", "x-larger", "x-maior", "maior", "small", "smaller", "l", "r-text",
            "font-size", "big", "uc", "lc", "nowrap", "gap-text", "bold", "italic", "sm", "nobr", "x-smaller"}
FIRST_TPL = {"tooltip", "abbr"}
DROP_BLOCK = re.compile(r"<!--.*?-->|<noinclude>.*?</noinclude>|<ref\b[^>/]*/>|<ref\b[^>]*>.*?</ref>|"
                        r"<(math|score|gallery|timeline|syntaxhighlight|sup|sub|includeonly)\b[^>]*>.*?</\1>|"
                        r"<pages\b[^>]*/?>|<references\s*/?>|<section\b[^>]*/>|__[A-Z]+__", re.S | re.I)
TAG = re.compile(r"</?[A-Za-z][^>]*>")
TPL = re.compile(r"\{\{([^{}]*)\}\}")
TABLE = re.compile(r"\{\|.*?\n\|\}", re.S)
LINK_DROP = re.compile(r"\[\[\s*(?:File|Image|Imago|Fasciculus|Categoria|Category|Media|w|wikipedia|[a-z]{2,3})\s*:"
                       r"[^\[\]]*(?:\[\[[^\]]*\]\][^\[\]]*)*\]\]", re.I)
LINK = re.compile(r"\[\[([^\[\]|]*)(?:\|([^\[\]]*))?\]\]")
EXT = re.compile(r"\[(?:https?:)?//[^\]]*\]")
HEADING = re.compile(r"^=+.*?=+\s*$", re.M)
# section headings from which on a page holds editorial matter, not the text
CUT_SECTION = re.compile(r"^=+\s*(?:Notae|Adnotationes|Annotationes|Apparatus|Commentari(?:us|um)|Nota|"
                         r"Notes|Fontes|Bibliographia|Vide etiam|Nexus externi|Lectiones variae)\s*=+\s*$",
                         re.M | re.I)


def tpl_repl(m):
    parts = m.group(1).split("|")
    name = parts[0].strip().lower()
    pos = [p for p in parts[1:] if not re.match(r"\s*[\w -]+\s*=", p)]
    if name in KEEP_TPL and pos:
        return pos[-1]
    if name in FIRST_TPL and pos:
        return pos[0]
    return " "


# a bracket or parenthesis holding a digit is a reference ("(Ioan. 14,28)", "[Schol. Gron. p. 436]"), not text
CITATION = re.compile(r"[\[(][^\[\]()\n]{0,80}\d[^\[\]()\n]{0,80}[\])]")
# sub-pages written by an editor, not by the author
EDITORIAL_PAGE = re.compile(r"^(?:Pr(?:a)?efatio(?:n)?\s+(?:editoris|editorum)|Prefation|Monitum|Admonitio|Prolegomena|"
                            r"Notitia|Notae|Annotationes|Adnotationes|Index|Elenchus|Introductio)\b", re.I)


def clean_wiki(t):
    m = CUT_SECTION.search(t)
    if m:
        t = t[:m.start()]
    t = DROP_BLOCK.sub(" ", t)
    for _ in range(8):
        t2 = TPL.sub(tpl_repl, t)
        if t2 == t:
            break
        t = t2
    t = TABLE.sub("\n", t)
    t = HEADING.sub("\n", t)
    t = LINK_DROP.sub(" ", t)
    t = LINK.sub(lambda m: m.group(2) if m.group(2) is not None else m.group(1).split("/")[-1], t)
    t = EXT.sub(" ", t)
    t = TAG.sub(" ", t)
    t = html.unescape(html.unescape(t))
    t = t.replace("'''", "").replace("''", "")
    t = CITATION.sub(" ", t)
    lines = []
    for line in t.split("\n"):
        s = line.strip()
        if not s or s[0] in "*#|!{}" or s.startswith("[["):
            continue  # lists of contents, table rows, left-over markup
        s = s.lstrip(":; ")
        if heading_line(s):
            continue
        lines.append(s)
    return "\n".join(lines)


HEAD_WORDS = {"caput", "capitulum", "cap", "liber", "lib", "epistola", "epistula", "sermo", "homilia", "carmen",
              "psalmus", "pars", "quaestio", "articulus", "distinctio", "titulus", "elegia", "satura", "ode",
              "fabula", "actus", "scaena", "scena", "sectio", "tractatus", "lectio", "canon", "versus"}
NUMBER = re.compile(r"^(?:\d+|[IVXLCDM]+|[ivxlcdm]+)$")


def heading_line(s):
    """A short line holding a number (Caput XII., Liber II, Carmen 5, Psalmus 3) is a heading, not text."""
    ws = re.findall(r"[^\W_]+", s)
    if 2 <= len(ws) <= 4 and ws[0].lower() in HEAD_WORDS and NUMBER.match(ws[1]):
        return True
    return 0 < len(ws) <= 5 and any(NUMBER.match(w) and (w.isdigit() or (w.isupper() and len(w) > 1)
                                                        or (w.islower() and len(ws) <= 2)) for w in ws)


# ---------------------------------------------------------------- language filter
# Function words of English, German, French, Italian and Spanish that are not Latin words (own list).
# (Latin homographs such as his, das, des, die, dei, para, dans, una, sono are left out.)
FOREIGN = set("""the and of to that with which was this from are be been were would there their they not or but he
she by der und ist nicht mit von zu den sich auf für ein eine dem im auch wird werden oder als bei aus wie noch nach
le les du une pour pas sur avec aux ce cette il elle son ont mais ou nous vous leur della che gli delle nel alla degli
questo questa come anche più perché lo la del los las por con y""".split())


def latin_paragraph(p):
    ws = [w.lower() for w in re.findall(r"[^\W\d_]+", p)]
    if not ws:
        return False
    f = sum(1 for w in ws if w in FOREIGN)
    return not (f >= 2 and f / len(ws) > 0.06)


def latin_only(text):
    return "\n".join(p for p in text.split("\n") if latin_paragraph(p))


# ---------------------------------------------------------------- Gutenberg
START = re.compile(r"\*\*\* ?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*\n", re.I)
END = re.compile(r"\*\*\* ?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK", re.I)
FOOTNOTE_BLOCK = re.compile(r"^\[\d+\][^\n]*(?:\n(?: {2,}|\t)[^\n]*)*", re.M)


def gutenberg_text(raw, start, end):
    t = raw.replace("\r", "")
    m = START.search(t)
    t = t[m.end():] if m else t
    m = END.search(t)
    t = t[:m.start()] if m else t
    m = re.search(start, t, re.M)
    if not m:
        raise ValueError("start marker not found: " + start)
    t = t[m.end():]
    if end:
        m = re.search(end, t, re.M)
        if not m:
            raise ValueError("end marker not found: " + end)
        t = t[:m.start()]
    t = FOOTNOTE_BLOCK.sub("", t)
    t = re.sub(r"\[\d+\]", "", t)
    t = CITATION.sub(" ", t)
    t = t.replace("_", "")
    # prose: join hard-wrapped lines of a paragraph; verse (indented or short lines) keeps its line breaks
    paras = []
    for para in re.split(r"\n\s*\n", t):
        lines = [l for l in para.split("\n") if l.strip()]
        if not lines:
            continue
        verse = sum(1 for l in lines if len(l.strip()) < 60) > 0.6 * len(lines) or len(lines) == 1
        paras.append("\n".join(l.strip() for l in lines) if verse else " ".join(l.strip() for l in lines))
    return latin_only("\n".join(paras))


# ---------------------------------------------------------------- proofread pages
RUNNING_HEAD = re.compile(r"^[^a-z]*\d[^a-z]*$|^[^a-z]{2,40}$")


def pagina_text(pages):
    out = []
    for t in pages:
        t = re.sub(r"<noinclude>.*?</noinclude>", "", t, flags=re.S)
        lines = t.strip().split("\n")
        if lines and RUNNING_HEAD.match(lines[0].strip()):
            lines = lines[1:]
        out.append("\n".join(lines))
    t = "\n".join(out)
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)  # word broken across lines or pages
    return latin_only(clean_wiki(t))


# ---------------------------------------------------------------- main
def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")[:60] + "_" + hashlib.md5(s.encode()).hexdigest()[:6]


def order_key(s):
    return hashlib.md5(("la7:" + s).encode()).hexdigest()


def read_dump(path):
    main, pagina = {}, defaultdict(dict)
    for _, el in ET.iterparse(bz2.open(path), events=("end",)):
        if el.tag.rsplit("}", 1)[-1] != "page":
            continue
        ns = int(el.find("{*}ns").text)
        title = el.find("{*}title").text
        if el.find("{*}redirect") is None and ns in (0, 104):
            text = el.find("{*}revision").find("{*}text").text or ""
            if ns == 0:
                main[title] = text
            else:
                base, _, num = title[len("Pagina:"):].rpartition("/")
                if num.isdigit():
                    pagina[base][int(num)] = text
        el.clear()
    return main, pagina


def main():
    work, dump = sys.argv[1], sys.argv[2]
    gdir = sys.argv[3] if len(sys.argv) > 3 else None
    tok.set_lang("la")
    main_pages, pagina = read_dump(dump)
    hdr = {t: header(v) for t, v in main_pages.items()}

    def ancestors(t):
        while "/" in t:
            t = t.rsplit("/", 1)[0]
            if t in main_pages:
                yield t

    def author(t):
        a = field(hdr[t], "Scriptor") if hdr[t] is not None else ""
        for p in ancestors(t):
            if a:
                break
            a = field(hdr[p], "Scriptor") if hdr[p] is not None else ""
        return a

    def bad(t):
        if BAD_SOURCE.search(main_pages[t]):
            return True
        return any(hdr[p] and BAD_SOURCE.search(hdr[p]) for p in ancestors(t))

    prose, poetry, late = set(S.PROSE_AUTHORS), set(S.POETRY_AUTHORS), set(S.LATE_AUTHORS)
    exclude = set(S.EXCLUDE_WORKS)
    sel = defaultdict(list)  # (group, author) -> [(work, title)]
    skipped = Counter()
    for t in sorted(main_pages):
        root = t.split("/")[0]
        if t.startswith(S.VULGATE_PREFIX):
            if any(k in t for k in S.VULGATE_SKIP):
                continue
            g, a = "late", "Vulgata Clementina"
        else:
            a = author(t)
            if a in prose:
                g = "poetry" if a == "Lucius Annaeus Seneca" and root in S.SENECA_TRAGEDIES else "prose"
            elif a in poetry:
                g = "poetry"
            elif a in late:
                g = "late"
            else:
                continue
            if root in exclude:
                skipped["excluded work"] += 1
                continue
            if "/" in t and EDITORIAL_PAGE.match(t.rsplit("/", 1)[1]):
                skipped["editorial sub-page"] += 1
                continue
        if bad(t):
            skipped["source not used (Perseus, Latin Library, Corpus Corporum, PHI)"] += 1
            continue
        sel[(g, a)].append((root, t))

    os.makedirs(work, exist_ok=True)
    for g in GROUPS:
        os.makedirs(os.path.join(work, g), exist_ok=True)
    manifest = []
    counters = defaultdict(lambda: (Counter(), Counter()))

    def count(g, a, texts):
        tot, ini = counters[(g, a)]
        n = 0
        for x in texts:
            n += tok.count_text(x, tot, ini)
        return n

    for (g, a), items in sorted(sel.items()):
        by_work = defaultdict(list)
        for w, t in items:
            by_work[w].append(t)
        capped = g == "late" and a != "Vulgata Clementina"
        works = sorted(by_work, key=order_key) if capped else sorted(by_work)
        done = 0
        for w in works:
            pages_n, n = 0, 0
            for t in sorted(by_work[w]):
                text = latin_only(clean_wiki(main_pages[t]))
                if capped:  # stop inside a page, at a paragraph, once the author reaches the cap
                    for para in text.split("\n"):
                        if done + n >= S.LATE_CAP:
                            break
                        n += count(g, a, [para])
                else:
                    n += count(g, a, [text])
                pages_n += 1
                if capped and done + n >= S.LATE_CAP:
                    break
            if n:
                manifest.append((g, a, w, "la.wikisource", pages_n, n))
                done += n
            if capped and done >= S.LATE_CAP:
                break

    for base, g, a, first, last in S.PAGINA_SETS:
        pg = {k: v for k, v in pagina.get(base, {}).items() if first <= k <= last}
        n = count(g, a, [pagina_text([pg[k] for k in sorted(pg)])])
        manifest.append((g, a, base, "la.wikisource (proofread pages)", len(pg), n))

    if gdir:
        for num, g, a, w, start, end in S.GUTENBERG:
            raw = open(os.path.join(gdir, f"pg{num}.txt"), encoding="utf-8", errors="replace").read()
            n = count(g, a, [gutenberg_text(raw, start, end)])
            manifest.append((g, a, f"{w} (Gutenberg #{num})", "gutenberg.org", 1, n))

    for (g, a), (tot, ini) in counters.items():
        tok.dump(os.path.join(work, g, slug(a) + ".tsv"), tot, ini)
    with open(os.path.join(work, "works.tsv"), "w", encoding="utf-8") as f:
        f.write("group\tauthor\twork\tsource\tpages\ttokens\n")
        for row in sorted(manifest):
            f.write("\t".join(map(str, row)) + "\n")
    per = Counter()
    for row in manifest:
        per[row[0]] += row[5]
    print(dict(per), "skipped pages:", dict(skipped))


if __name__ == "__main__":
    main()

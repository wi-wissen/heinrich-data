"""Shared tokenizer / counter for the Heinrich frequency lists (German and English).

Only counts are kept; texts are streamed and discarded.
Tokens are case-sensitive surface forms (NFC). A token is a run of Latin
letters, optionally joined by single hyphens or apostrophes between letters
("Baden-Württemberg", "geht's"). Anything touching a digit is dropped.
"""
import re
import unicodedata
from collections import Counter

L = "A-Za-zÀ-ÖØ-öø-ÿĀ-ſƀ-ɏ"
WORD = re.compile(rf"(?<![{L}\d])[{L}]+(?:[-'’][{L}]+)*(?![{L}\d])")
# tokens that touch digits / underscores / other word chars are discarded by the lookarounds,
# but a run like "3D" or "abc123" must be dropped entirely, not partially matched:
BAD_RUN = re.compile(rf"[{L}\d_]*\d[{L}\d_]*")
ABBR_DE = (r"z|B|d|h|u|a|ca|bzw|usw|etc|Dr|Prof|Nr|St|vgl|ggf|evtl|Mio|Mrd|Hrsg|geb|gest|Abb|Tab|ff|S|Bd|"
        r"Jh|Chr|vs|usf|sog|inkl|exkl|max|min|Str|Fa|Hr|Fr|Co|Ltd|Inc|Jr|Sr|ev|kath|röm|ä|o|v|n|ebd|"
        r"Kap|Art|Abs|Ziff|Anm|bes|eigtl|dt|engl|frz|lat|ital|span|russ|griech|österr|Mt|Mk|Lk|Joh|"
        r"Std|Sek|ggfs|Tel|Hg|hrsg|Aufl|Jg|Jhd|Anh|Dipl|Ing|Mag|Fam|Frl|Ges|Verf|Vf|Red|Dir|Gen|Lt|Kfm|rd|resp|sc|ders|dies|ebda|cf|op|cit|Sp|Sen|Abg|MdB|Bundesrep|Dt|Nrn|Rn|Bsp|Mr|Mrs|Ms|Mme|Hl|Ew|Sr|Pf|Pfr|Pastor")
# English abbreviations that do not end a sentence (own list; single letters such as "e.g.", "U.S." are
# covered by the single-letter rule).
ABBR_EN = (r"Mr|Mrs|Ms|Messrs|Mme|Mlle|Dr|Prof|Rev|Revd|Hon|St|Ste|Mt|Ft|Jr|Sr|Esq|Gen|Col|Capt|Cpt|Lt|Maj|Sgt|"
           r"Cmdr|Adm|Gov|Sen|Rep|Pres|Supt|Insp|Det|Fr|Bros|Co|Corp|Inc|Ltd|Plc|LLC|Dept|Univ|Assn|Ave|Blvd|Rd|"
           r"Sq|No|Nos|Vol|Vols|vol|pp|ch|Ch|chap|sec|Sec|Secs|art|Art|para|paras|Para|fig|Fig|figs|ed|eds|Ed|"
           r"trans|repr|cf|viz|vs|etc|al|ca|approx|esp|incl|misc|op|cit|ibid|Ibid|id|seq|Jan|Feb|Mar|Apr|Jun|"
           r"Jul|Aug|Sep|Sept|Oct|Nov|Dec|Mon|Tue|Tues|Wed|Thu|Thur|Thurs|Fri|Sat|Sun|Mass|Penn|Conn|Calif|"
           r"Fla|Ill|Wash|Va|Md|Ga|Tex|Ky|Tenn|Ala|Miss|Mich|Minn|Wis|Ariz|Colo|Okla|Kan|Neb|Nev|Ore|"
           r"hon|Rt|Bt|Bart|cl|subs|reg|regs|Regs|Stat|Cong|Sess|Doc|Docs|Pub|Amdt|Ord|Rept|Exec|Admin|"
           r"Comm|Natl|Intl|Assoc|Mfg|Mgr|Dist|Ct|Cir|Supp|App|Ry|Rly|Gaz|Gent|viz|sc|ult|inst|prox|do")
ABBR = {"de": ABBR_DE, "en": ABBR_EN}
# German: ordinal numbers ("3. Mai") do not end a sentence; English has no such ordinals.
PROT_BY_LANG = {
    "de": re.compile(rf"(?<![{L}])(?:{ABBR_DE}|[{L}]|\d+)\."),
    "en": re.compile(rf"(?<![{L}])(?:{ABBR_EN}|[{L}])\."),
}
PROT = PROT_BY_LANG["de"]
LANG = "de"


LEAD = {"de": "\"„“»«(‚'[-–— \x00", "en": "\"“‘(['-–— \x00"}


def set_lang(lang):
    """Select the abbreviation list used by the sentence splitter ("de" or "en")."""
    global PROT, SPLIT, LANG
    PROT, SPLIT, LANG = PROT_BY_LANG[lang], SPLIT_BY_LANG[lang], lang
SPLIT = re.compile(r"(?<=[.!?…])[\"“”«»'’)\]]*\s+(?=[\"„“»«(\[‚'-]*[A-ZÄÖÜÀ-ÖØ-Þ])|\n+|\s+[–—]\s+(?=[A-ZÄÖÜ])")
# English additionally opens quotations with ‘ (U+2018).
SPLIT_BY_LANG = {
    "de": SPLIT,
    "en": re.compile(r"(?<=[.!?…])[\"“”«»'’)\]]*\s+(?=[\"“‘(\['-]*[A-ZÀ-ÖØ-Þ])|\n+|\s+[–—]\s+(?=[A-Z])"),
}


def tokenize_lines(text):
    """Yield list-of-words per sentence."""
    text = unicodedata.normalize("NFC", text)
    text = PROT.sub(lambda m: m.group(0)[:-1] + "\x00", text)
    for sent in SPLIT.split(text):
        if not sent:
            continue
        sent = BAD_RUN.sub(" \x01 ", sent)  # \x01 marks a digit run
        words = []
        first_ok = True
        # sentence starting with a number: first real word is not sentence-initial
        s = sent.lstrip(LEAD[LANG])
        if s.startswith("\x01"):
            first_ok = False
        words = WORD.findall(sent)
        if words:
            yield words, first_ok


def count_text(text, tot, init):
    n = 0
    for words, first_ok in tokenize_lines(text):
        w = [x.replace("’", "'") for x in words]
        tot.update(w)
        n += len(w)
        if first_ok:
            init[w[0]] += 1
    return n


class Regional:
    """Counters per region tag (e.g. "us", "gb") next to the main counters of a source file."""

    def __init__(self):
        self.c = {}

    def count(self, region, text):
        if not region:
            return 0
        tot, init = self.c.setdefault(region, (Counter(), Counter()))
        return count_text(text, tot, init)

    def add(self, region, tot, init):
        if region:
            t, i = self.c.setdefault(region, (Counter(), Counter()))
            t.update(tot)
            i.update(init)

    def dump(self, path):
        """Write one file per region: <path without .tsv>.<region>.tsv (before the main file)."""
        for r, (tot, init) in self.c.items():
            dump(path[:-4] + f".{r}.tsv", tot, init)


def dump(path, tot, init):
    with open(path, "w", encoding="utf-8") as f:
        for w, c in tot.items():
            f.write(f"{w}\t{c}\t{init.get(w, 0)}\n")


def load(path, tot, init):
    with open(path, encoding="utf-8") as f:
        for line in f:
            w, c, i = line.rstrip("\n").split("\t")
            tot[w] += int(c)
            if int(i):
                init[w] += int(i)

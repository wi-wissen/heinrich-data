"""Shared tokenizer / counter for the Heinrich frequency list.

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
ABBR = (r"z|B|d|h|u|a|ca|bzw|usw|etc|Dr|Prof|Nr|St|vgl|ggf|evtl|Mio|Mrd|Hrsg|geb|gest|Abb|Tab|ff|S|Bd|"
        r"Jh|Chr|vs|usf|sog|inkl|exkl|max|min|Str|Fa|Hr|Fr|Co|Ltd|Inc|Jr|Sr|ev|kath|röm|ä|o|v|n|ebd|"
        r"Kap|Art|Abs|Ziff|Anm|bes|eigtl|dt|engl|frz|lat|ital|span|russ|griech|österr|Mt|Mk|Lk|Joh|"
        r"Std|Sek|ggfs|Tel|Hg|hrsg|Aufl|Jg|Jhd|Anh|Dipl|Ing|Mag|Fam|Frl|Ges|Verf|Vf|Red|Dir|Gen|Lt|Kfm|rd|resp|sc|ders|dies|ebda|cf|op|cit|Sp|Sen|Abg|MdB|Bundesrep|Dt|Nrn|Rn|Bsp|Mr|Mrs|Ms|Mme|Hl|Ew|Sr|Pf|Pfr|Pastor")
PROT = re.compile(rf"(?<![{L}])(?:{ABBR}|[{L}]|\d+)\.")
SPLIT = re.compile(r"(?<=[.!?…])[\"“”«»'’)\]]*\s+(?=[\"„“»«(\[‚'-]*[A-ZÄÖÜÀ-ÖØ-Þ])|\n+|\s+[–—]\s+(?=[A-ZÄÖÜ])")


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
        s = sent.lstrip("\"„“»«(‚'[-–— \x00")
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

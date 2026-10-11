#!/usr/bin/env python3
"""Read Fred's project write-ups out of the portfolio page (index.html).

index.html is ~1.2 MB because figures and fonts are embedded, so it is not
practical to read directly. This prints the text only.

  python3 .claude/skills/tailor-resume/portfolio.py list       # one line per project
  python3 .claude/skills/tailor-resume/portfolio.py 5 9        # full text of projects 05 and 09
  python3 .claude/skills/tailor-resume/portfolio.py all        # full text of every project

Standard library only.
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PAGE = os.path.join(ROOT, "index.html")
SITE = "https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/"
SKIP = {"script", "style", "figure", "svg", "button"}
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "wbr"}


class Projects(HTMLParser):
    """Collects the text of each <article class="sheet project">, by part."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.projects = []   # dicts: id, parts{kind: [text]}
        self.depth = 0       # element depth inside the current project
        self.skip = 0        # depth inside an element whose text we drop
        self.kind = []       # stack of the class-derived kind for each open element

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if not self.depth:
            if "sheet" in cls.split() and "project" in cls.split():
                self.projects.append({"parts": {}})
                self.depth, self.kind = 1, ["body"]
            return
        if tag in VOID:
            return
        self.depth += 1
        if self.skip or tag in SKIP or "pnav" in cls or "foot" in cls or "back-link" in cls:
            self.skip += 1
        kind = self.kind[-1]
        if "stat" in cls.split() and self.projects[-1]["parts"].get("stat"):
            self.projects[-1]["parts"]["stat"].append("|")   # between key numbers
        for k in ("eb", "lede", "stat", "par", "g-facts", "g-tags"):
            if k in cls.split():
                kind = k
        if tag in ("h2",) and kind == "body":
            kind = "title"
        self.kind.append(kind)

    def handle_endtag(self, tag):
        if not self.depth or tag in VOID:
            return
        self.depth -= 1
        if self.skip:
            self.skip -= 1
        self.kind.pop()

    def handle_data(self, data):
        if self.depth and not self.skip and data.strip():
            p = self.projects[-1]["parts"]
            p.setdefault(self.kind[-1], []).append(data.strip())


def load():
    parser = Projects()
    with open(PAGE, encoding="utf-8") as f:
        parser.feed(f.read())
    out = []
    for i, p in enumerate(parser.projects, 1):
        parts = {k: re.sub(r"\s+", " ", " ".join(v)).strip() for k, v in p["parts"].items()}
        out.append({
            "n": i,
            "anchor": f"{SITE}#p{i:02d}",
            "eyebrow": parts.get("eb", ""),
            "title": parts.get("title", ""),
            "lede": parts.get("lede", ""),
            "numbers": parts.get("stat", ""),
            "problem_approach_result": parts.get("par", ""),
            "facts": parts.get("g-facts", ""),
            "topics": parts.get("g-tags", ""),
            "body": parts.get("body", ""),
        })
    return out


def main(args):
    projects = load()
    if not args or args[0] == "list":
        for p in projects:
            print(f"{p['n']:02d}  {p['title']}\n    {p['eyebrow']}  [{p['topics']}]\n    {p['lede']}\n")
        return
    wanted = projects if args[0] == "all" else [projects[int(a) - 1] for a in args]
    for p in wanted:
        print("=" * 80)
        print(f"{p['n']:02d}  {p['title']}\nLink: {p['anchor']}\n{p['eyebrow']}  [{p['topics']}]")
        print(f"\nIn one line: {p['lede']}")
        if p["numbers"]:
            print(f"Key numbers: {p['numbers']}")
        if p["problem_approach_result"]:
            print(f"\n{p['problem_approach_result']}")
        print(f"\n{p['body']}\n")


if __name__ == "__main__":
    main(sys.argv[1:])

"""Shared helpers for the renderers: paths, content loading, templating, Chromium.

Layout of the repository, relative to this file:
    src/render/common.py      this module
    src/styles/*.css          tokens, figure system, card, page
    src/templates/*.html      Jinja templates and macros
    src/figures/NN-slug.html  one figure body per file (a Jinja template)
    src/content/meta.yaml     title, author, links, closing page
    signals/NN-slug.yaml      the ten signals
    guide/NN-slug.md          one Markdown page per PDF page
    figures/                  rendered PNGs (never edited by hand)
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
STYLES = SRC / "styles"
TEMPLATES = SRC / "templates"
FIG_SRC = SRC / "figures"
CONTENT = SRC / "content"
SIGNALS = ROOT / "signals"
GUIDE = ROOT / "guide"
FIGURES = ROOT / "figures"
CARDS = FIGURES / "cards"
BUILD = ROOT / "build"

DOMAIN_REGISTER = {
    "control-plane": "tech",
    "shared-services": "ops",
    "data-plane": "tech",
    "platform-state": "ops",
    "organisation": "biz",
}
DECISION_STEPS = ["monitor", "investigate", "stabilise", "escalate"]


def css(*names: str) -> str:
    return "\n".join((STYLES / f"{n}.css").read_text(encoding="utf-8") for n in names)


def env() -> Environment:
    e = Environment(
        loader=FileSystemLoader([str(TEMPLATES), str(FIG_SRC), str(SRC)]),
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    e.globals["DECISION_STEPS"] = DECISION_STEPS
    return e


def load_meta() -> dict:
    return yaml.safe_load((CONTENT / "meta.yaml").read_text(encoding="utf-8"))


def load_signals() -> list[dict]:
    out = []
    for p in sorted(SIGNALS.glob("[0-9][0-9]-*.yaml")):
        s = yaml.safe_load(p.read_text(encoding="utf-8"))
        s["file"] = p.name
        s["register"] = DOMAIN_REGISTER.get(s["domain"], "tech")
        out.append(s)
    by_slug = {s["slug"]: s for s in out}
    for s in out:
        s["read_with_names"] = [by_slug[r]["name"] if r in by_slug else r for r in s.get("read_with", [])]
        s["read_with_ids"] = [by_slug[r]["id"] if r in by_slug else "" for r in s.get("read_with", [])]
    return out


# --- Markdown guide pages -------------------------------------------------------

PAGE_RE = re.compile(r"^(\d\d)-(.+)\.md$")


def list_pages() -> list[Path]:
    return sorted(p for p in GUIDE.glob("[0-9][0-9]-*.md"))


def parse_page(path: Path) -> dict:
    """Parse a guide page written in the repository's fixed shape.

    <sub>running header</sub> · # NN · Title · *kicker* · **key message** ·
    ![alt](../figures/slug.png) · ### sections with paragraphs, lists or a
    > callout · --- · navigation. Everything after the rule is ignored.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    page = {
        "path": path, "number": "", "slug": "", "title": "", "kicker": "",
        "key": "", "figure": "", "alt": "", "sections": [], "callouts": [],
    }
    m = PAGE_RE.match(path.name)
    if m:
        page["number"], page["slug"] = m.group(1), m.group(2)
    cur = None
    for raw in lines:
        line = raw.rstrip()
        if line.strip() == "---":
            break
        if line.startswith("<sub>"):
            continue
        if line.startswith("# "):
            t = line[2:].strip()
            t = re.sub(r"^\d\d\s*·\s*", "", t)
            page["title"] = t
            continue
        if not page["kicker"] and re.fullmatch(r"\*[^*].*[^*]\*", line.strip()):
            page["kicker"] = line.strip().strip("*")
            continue
        if not page["key"] and line.startswith("**") and line.rstrip().endswith("**"):
            page["key"] = line.strip().strip("*")
            continue
        fm = re.match(r"!\[(.*?)\]\(\.\./figures/(.+?)\.png\)", line.strip())
        if fm:
            page["alt"], page["figure"] = fm.group(1), fm.group(2)
            continue
        if line.startswith("### "):
            cur = {"heading": line[4:].strip(), "paras": [], "bullets": [], "ordered": False}
            page["sections"].append(cur)
            continue
        if line.startswith("> "):
            page["callouts"].append(line[2:].strip())
            continue
        if cur is not None:
            s = line.strip()
            if not s:
                continue
            if re.match(r"^- ", s):
                cur["bullets"].append(s[2:].strip())
            elif re.match(r"^\d+\. ", s):
                cur["ordered"] = True
                cur["bullets"].append(re.sub(r"^\d+\. ", "", s))
            else:
                cur["paras"].append(s)
    return page


def inline_md(s: str) -> str:
    """Bold, italics and code in a paragraph, nothing else."""
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


# --- Chromium -------------------------------------------------------------------

def screenshot_html(html: str, out: Path, width: int, height: int, scale: float = 1.0) -> None:
    from playwright.sync_api import sync_playwright

    out.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
        page.set_content(html, wait_until="load")
        page.wait_for_timeout(150)
        page.screenshot(path=str(out), full_page=False, type="png")
        browser.close()


def screenshots_html(items: list[tuple[str, Path]], width: int, height: int, scale: float = 1.0) -> None:
    """Render several documents with one browser."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
        for html, out in items:
            out.parent.mkdir(parents=True, exist_ok=True)
            page.set_content(html, wait_until="load")
            page.wait_for_timeout(120)
            page.screenshot(path=str(out), full_page=False, type="png")
            print(f"  rendered {out.relative_to(ROOT)}")
        browser.close()


def wrap_document(body: str, styles: str, title: str = "", extra_head: str = "") -> str:
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{title}</title><style>{styles}</style>{extra_head}</head>"
        f"<body>{body}</body></html>"
    )

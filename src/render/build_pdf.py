#!/usr/bin/env python3
"""Build the guide as a PDF: guide/*.md + signals/*.yaml + src/figures/*.html → the PDF at the repository root.

Usage:
    python3 src/render/build_pdf.py                 # writes the PDF named in meta (see OUT)
    python3 src/render/build_pdf.py --html          # also keeps build/guide.html for inspection

Pages 02–05 and 11–16 come from guide/NN-slug.md (parsed by common.parse_page).
Pages 06–10 are the ten signal cards, two per page, from signals/*.yaml.
Pages 01 and 17 come from src/content/meta.yaml. Figures are embedded as HTML,
so the PDF carries real, selectable text; the PNGs in figures/ are for GitHub
and LinkedIn. The document outline (bookmarks) is generated from the page
titles; metadata is written with pikepdf.
"""
from __future__ import annotations

import sys
from pathlib import Path

from common import (BUILD, FIG_SRC, ROOT, css, env, inline_md, list_pages, load_meta, load_signals,
                    parse_page, wrap_document)
from render_cards import card_html
from render_figures import render_figure_html

OUT = ROOT / "Regaining-Control-Observability-for-OpenStack-Platforms-in-Difficulty.pdf"

SIGNAL_PAGES = {
    "06": {"ids": ["01", "02"], "title": "API health · Control-plane liveness",
           "lead": "Is the platform responding, and is the capacity it reports real?"},
    "07": {"ids": ["03", "04"], "title": "Messaging health · Database health",
           "lead": "The two shared dependencies every operation relies on."},
    "08": {"ids": ["05", "06"], "title": "Scheduling and build outcomes · Capacity headroom",
           "lead": "Capacity problem, or health problem?"},
    "09": {"ids": ["07", "08"], "title": "Storage health and latency · Network data path and agents",
           "lead": "The layers with the widest blast radius."},
    "10": {"ids": ["09", "10"], "title": "Workload state integrity · Reliability trend",
           "lead": "Is what the platform reports true? Are we stabilising, or drifting?"},
}


def figure_bodies(e, meta, signals) -> dict[str, str]:
    """Render each figure template to its body only (no document wrapper)."""
    out = {}
    for src in sorted(FIG_SRC.glob("[0-9][0-9]-*.html")):
        tpl = e.get_template(src.name)
        out[src.stem] = tpl.render(meta=meta, signals=signals, fig_num=src.stem[:2])
    return out


def build_html() -> str:
    e = env()
    e.filters["inline"] = inline_md
    meta, signals = load_meta(), load_signals()
    by_id = {s["id"]: s for s in signals}
    pages = {}
    for p in list_pages():
        page = parse_page(p)
        pages[page["number"]] = page
    figures = figure_bodies(e, meta, signals)
    signal_pages = {}
    for n, spec in SIGNAL_PAGES.items():
        cards = "".join(card_html(e, by_id[i], "print", meta) for i in spec["ids"])
        signal_pages[n] = {"title": spec["title"], "lead": spec["lead"], "cards": cards,
                           "range": "–".join(spec["ids"])}
    order = [f"{i:02d}" for i in range(2, meta["pages"])]
    missing = [n for n in order if n not in pages and n not in signal_pages]
    if missing:
        raise SystemExit(f"missing guide pages: {missing}")
    body = e.get_template("pdf.html").render(meta=meta, pages=pages, figures=figures,
                                             signal_pages=signal_pages, order=order)
    styles = css("tokens", "figure", "card", "page")
    return wrap_document(body, styles, title=f"{meta['title']} — {meta['subtitle']}")


def write_pdf(html: str, out: Path, meta: dict) -> None:
    from playwright.sync_api import sync_playwright
    import pikepdf

    tmp = BUILD / "guide.raw.pdf"
    BUILD.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.wait_for_timeout(300)
        page.pdf(path=str(tmp), format="A4", print_background=True, prefer_css_page_size=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, outline=True, tagged=True)
        browser.close()
    with pikepdf.open(tmp) as pdf:
        with pdf.open_metadata() as m:
            m["dc:title"] = f"{meta['title']} — {meta['subtitle']}"
            m["dc:creator"] = [meta["author"]["name"]]
            m["dc:description"] = f"{meta['tagline']} {meta['audience_line']}"
            m["dc:subject"] = ["OpenStack", "observability", "Day-2 operations", "private cloud", "decision-making"]
            m["pdf:Keywords"] = "OpenStack, observability, Day-2 operations, private cloud, platform engineering, decision-making"
            m["xmp:CreatorTool"] = "openstack-regaining-control build (Chromium via Playwright)"
        pdf.docinfo["/Title"] = f"{meta['title']} — {meta['subtitle']}"
        pdf.docinfo["/Author"] = meta["author"]["name"]
        pdf.docinfo["/Subject"] = f"{meta['tagline']} {meta['audience_line']}"
        pdf.docinfo["/Keywords"] = "OpenStack, observability, Day-2 operations, private cloud, platform engineering, decision-making"
        pdf.save(out, linearize=True)
    tmp.unlink(missing_ok=True)


def main(argv):
    html = build_html()
    if "--html" in argv:
        BUILD.mkdir(exist_ok=True)
        (BUILD / "guide.html").write_text(html, encoding="utf-8")
        print(f"  wrote {BUILD.relative_to(ROOT)}/guide.html")
    write_pdf(html, OUT, load_meta())
    print(f"  wrote {OUT.name} ({OUT.stat().st_size / 1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

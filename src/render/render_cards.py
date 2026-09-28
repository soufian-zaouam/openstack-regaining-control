#!/usr/bin/env python3
"""Render the ten KPI cards for LinkedIn and GitHub: signals/NN-slug.yaml → figures/cards/NN-slug.png.

Usage:
    python3 src/render/render_cards.py          # all ten
    python3 src/render/render_cards.py 03 07    # by number or slug

Cards are 1080 × 1350 (4:5), rendered at 2× like the investigation memos of the
Production Guide. The same template, in `print` mode, is embedded in the PDF by
build_pdf.py; the YAML is the single source of both.
"""
import sys

from common import CARDS, css, env, load_meta, load_signals, screenshots_html, wrap_document
from visuals import render_visual

W, H, SCALE = 1080, 1350, 2


def card_html(e, s: dict, mode: str, meta: dict) -> str:
    return e.get_template("card.html").render(s=s, mode=mode, visual_svg=render_visual(s["visual"]), meta=meta)


def main(argv):
    e, meta = env(), load_meta()
    items = []
    for s in load_signals():
        if argv and s["id"] not in argv and s["slug"] not in argv:
            continue
        body = card_html(e, s, "social", meta)
        html = wrap_document(body, css("tokens", "card"), title=f"Signal {s['id']} — {s['name']}")
        items.append((html, CARDS / f"{s['id']}-{s['slug']}.png"))
    if not items:
        print("no signal matched", argv)
        return 1
    screenshots_html(items, W, H, SCALE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

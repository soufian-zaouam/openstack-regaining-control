#!/usr/bin/env python3
"""Render the figures: src/figures/NN-slug.html → figures/NN-slug.png (1600 × 1000).

Usage:
    python3 src/render/render_figures.py            # all figures
    python3 src/render/render_figures.py 03 14      # by number or slug

Each source file is a Jinja template holding the body of a figure (a <div class="fig">).
It receives `meta` (src/content/meta.yaml), `signals` (the ten signals, in order)
and the macros of src/templates/macros.html. The canvas is 1200 × 750 logical
pixels, rendered at 4/3 scale so that the PNG matches the 1600 × 1000 figures of
the collection.
"""
import sys
from pathlib import Path

from common import FIG_SRC, FIGURES, css, env, load_meta, load_signals, screenshots_html, wrap_document

W, H, SCALE = 1200, 750, 4 / 3


def select(args: list[str]) -> list[Path]:
    files = sorted(FIG_SRC.glob("[0-9][0-9]-*.html"))
    if not args:
        return files
    keep = []
    for f in files:
        num, slug = f.stem[:2], f.stem[3:]
        if num in args or slug in args or f.stem in args:
            keep.append(f)
    return keep


def render_figure_html(e, src: Path, meta: dict, signals: list[dict]) -> str:
    tpl = e.get_template(src.name)
    body = tpl.render(meta=meta, signals=signals, fig_num=src.stem[:2])
    return wrap_document(body, css("tokens", "figure"), title=src.stem)


def main(argv: list[str]) -> int:
    e = env()
    meta, signals = load_meta(), load_signals()
    items = []
    for src in select(argv):
        html = render_figure_html(e, src, meta, signals)
        items.append((html, FIGURES / f"{src.stem}.png"))
    if not items:
        print("no figure matched", argv)
        return 1
    screenshots_html(items, W, H, SCALE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

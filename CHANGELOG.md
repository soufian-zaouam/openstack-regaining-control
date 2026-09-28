# Changelog

All notable changes to this guide. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions are tagged as [releases](https://github.com/soufian-zaouam/openstack-regaining-control/releases), each with the PDF attached.

## [1.0] — 2026-09-29

First edition.

### Added

- The guide: *Regaining Control — Observability for OpenStack Platforms in Difficulty*, 17 pages, A4, one idea and one figure per page (`Regaining-Control-Observability-for-OpenStack-Platforms-in-Difficulty.pdf`), and the same content page by page in `guide/`.
- `signals/`: the ten signals as YAML sources (API health, control-plane liveness, messaging health, database health, scheduling and build outcomes, capacity headroom, storage health and latency, network data path and agents, workload state integrity, reliability trend), each with its primary sources; `signals/README.md` with the selection criteria and the signals left out.
- `figures/`: twelve figures (the two paths, the bridge, one signal two languages, the platform map, convergence, the six-week scenario, dashboard vs decision view, the seven steps, the decision tree, eight principles, the cover) and the ten KPI cards in `figures/cards/`.
- `src/`: the figure system (design tokens, three registers, figure and card templates) and the renderers (`render_figures.py`, `render_cards.py`, `build_pages.py`, `build_pdf.py`); `Makefile`; the build workflow; issue templates (erratum, signal).
- `assets/`: palette and typography notes, social preview.
- `LICENSE` (CC BY-NC-ND 4.0), `CONTRIBUTING.md`, `CITATION.cff`.

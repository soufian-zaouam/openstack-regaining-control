# Visual identity

The identity is shared with the other works of the series (the Short Guide's figures, the Production Guide's investigation memos): a dark "instrument" surface for figures and cards, IBM Plex typography, an amber accent — and, specific to this guide, three colour registers that say at a glance whether a word belongs to the technical, the operational or the business side of the bridge. All values live in [`src/styles/tokens.css`](../src/styles/tokens.css).

## Registers

| Register | Colour | Used for |
| --- | --- | --- |
| Technical | steel blue `#5aa0e0` | raw signals, service names, values, text in IBM Plex Mono |
| Operational | amber `#e0a458` | operational meaning, correlation, arrows that carry meaning, emphasis |
| Business / decision | teal `#35b5a0` | impact, owned risk, decision, owner |
| Risk | muted red `#e0655a` | *if nothing is done*, red zones — rare, and never without a label |
| Neutral | grey `#9aa3ad` | what is not yet understood, the unknown, elements out of focus |

The three registers were checked for colour-vision deficiency separation and for contrast against both surfaces; the risk red sits next to a label everywhere it appears.

## Surfaces

| Surface | Colour |
| --- | --- |
| Figure and card background | `#0f1621` |
| Panels | `#1b2430` · rules `#2f3a48` |
| Text on dark | `#e8e6e1` · muted `#9aa3ad` · dim `#6b7480` |
| PDF page (paper) | `#f7f5f0` · rules `#d9d4c9` |
| Text on paper | `#1b2430` · muted `#6b7480` |

## Typography

**IBM Plex Sans** for text and titles (Semibold for titles, Regular for body). **IBM Plex Mono** for everything that comes from the machine: signal names, values, section labels in spaced capitals (`WHAT WE SEE`), figure kickers (`— REGAINING CONTROL · THE IDEA`). On Debian and Ubuntu: `apt install fonts-ibm-plex`.

## Formats

| Asset | Size | Where |
| --- | --- | --- |
| Figures | 1600 × 1000 px (16:10), rendered from a 1200 × 750 canvas | `figures/NN-slug.png` |
| KPI cards | 1080 × 1350 px (4:5), rendered at 2× | `figures/cards/NN-slug.png` |
| PDF pages | A4 portrait, figures at 182 mm wide | the PDF |
| Social preview | 1200 × 630 px | `assets/social-preview.png` |

## Grammar

One visual message per figure, named in its title and numbered (`FIG. 07`). Flows read left to right or top to bottom, never both. Boxes with slightly rounded corners and a 1 px rule; amber arrows carry meaning, grey ones connect. No illustration, no stock imagery, no decorative gradient; line icons only, and few. Nothing under 13 px on the 1200 × 750 canvas, so that a figure stays legible once reduced to the width of a page. Every figure is designed to be read on its own, because it will be, on LinkedIn.

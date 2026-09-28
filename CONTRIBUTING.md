# Contributing

Thank you for helping make this guide more useful to the people who decide what happens to an OpenStack platform, and to the engineers who have to explain it to them.

## What is welcome

- **Corrections**: a technical statement on a card that is wrong, outdated, or only true for one distribution or release. Open an issue with the *erratum* template, or a pull request with the source that shows the correct behaviour.
- **A challenge to a signal**: why one of the ten should not be there, or should be read differently. Open an issue with the *signal* template; the [selection criteria](signals/README.md#why-these-ten) are the ground on which it will be discussed.
- **A signal you would have chosen instead**: with the decision it supports, the question a decision-maker can ask, and the signals to read it with. The list of [signals left out](signals/README.md#the-signals-left-out-and-why) says why some obvious candidates are not there.
- **Better sources**: a primary source that states a card's technical claim more precisely, or the version in which behaviour changed.
- **A better translation**: a sentence in the *Why it matters* or *Management question* block that a decision-maker would understand faster.

## What this repository is not

- A metrics catalogue. A signal without a decision it supports will not be merged, however important it is technically.
- A monitoring tutorial. Exporters, dashboards, alert rules and commands are out of scope; they belong to the [Production Guide](https://github.com/soufian-zaouam/openstack-production-guide) and to each platform.
- A place for anything confidential, or for a specific organisation's story.

## Three rules for every contribution

1. **Every technical statement rests on a primary source, cited in the signal's `sources` list.** Project documentation, release notes or source code: a link. Behaviour that depends on a release, a backend or a deployment tool is stated as such.
2. **No environment data.** No employer or customer names, real hostnames or addresses, internal figures, identifiable incidents, or anything covered by an NDA. Scenarios are composites, generalised so that no platform or person can be recognised. Numbers in figures are illustrative shapes, not measurements.
3. **A signal keeps its decisional value.** Each card answers the same six blocks and names the decision it supports (*monitor · investigate · stabilise · escalate*). A change that makes a card more technical and less decidable will be discussed before being merged.

## Style

- English, Oxford spelling (*stabilise, prioritise, organisation*). Short sentences; the message before the mechanism; no marketing, no superlatives.
- Same tone from the README to the last card: exact, sober, written for someone who decides.
- One idea per page, one figure per page, 150 words per page at most. If a figure can replace a paragraph, the paragraph goes.
- Figures use the three registers of [`src/styles/tokens.css`](src/styles/tokens.css) — Technical (blue), Operational (amber), Business / decision (teal) — and nothing smaller than 13 px on the 1200 × 750 canvas. Red is for risk only, and never alone.

## Editing

- **A signal**: edit its file in [`signals/`](signals/), keep the field names, then `make cards pages pdf`. The card, the guide page and the PDF are regenerated; never edit the PNGs.
- **A page**: pages 02–05 and 11–16 are edited directly in [`guide/`](guide/); keep their fixed shape (running header, `# NN · Title`, *kicker*, **key message**, the figure, `###` sections, the navigation), because the PDF is built from it. Pages 01, 06–10 and 17 are generated.
- **A figure**: edit its file in [`src/figures/`](src/figures/) and run `make figures`; look at the PNG before committing. The figure system and its macros are documented at the top of [`src/styles/figure.css`](src/styles/figure.css) and [`src/templates/macros.html`](src/templates/macros.html).
- **Build**: `pip install -r requirements.txt && python3 -m playwright install chromium`, then `make all`. IBM Plex Sans and Mono should be installed for a faithful render.

## How to contribute

1. Open an issue describing the correction or the proposal, with the source.
2. For changes, fork the repository, create a branch, run `make all`, and open a pull request with a short explanation of *why* the change is correct.
3. Keep the style above.

This work is licensed under [CC BY-NC-ND 4.0](LICENSE). Contributions are accepted as corrections and improvements to this work, published under the same licence with attribution to their authors in the [CHANGELOG](CHANGELOG.md); derivative works are not distributed from this repository.

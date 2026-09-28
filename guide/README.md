# Regaining Control — the guide, page by page

The 17 pages of the PDF, one Markdown file each, readable here without opening the PDF. Each page carries one idea and one figure; the navigation at the bottom of every page leads to the next.

**Read it as a single document:** [`Regaining-Control-Observability-for-OpenStack-Platforms-in-Difficulty.pdf`](../Regaining-Control-Observability-for-OpenStack-Platforms-in-Difficulty.pdf) (A4, 17 pages).

**Five-minute path:** pages 02, 03, 05, 11, 13, 14 and 17. **Ten minutes:** everything except the signal cards. **Thirty minutes:** everything, then [`signals/`](../signals/) for the sources.

## Contents

| Page | Idea | Figure |
|---|---|---|
| 01 | [Regaining Control](01-regaining-control.md) | [fig. 01](../figures/01-regaining-control.png) |
| 02 | [When a platform becomes difficult](02-when-a-platform-becomes-difficult.md) | [fig. 02](../figures/02-when-a-platform-becomes-difficult.png) |
| 03 | [Observability is a shared language](03-observability-is-a-shared-language.md) | [fig. 03](../figures/03-observability-is-a-shared-language.png) |
| 04 | [One signal, two languages](04-one-signal-two-languages.md) | [fig. 04](../figures/04-one-signal-two-languages.png) |
| 05 | [Ten signals, one platform](05-ten-signals-one-platform.md) | [fig. 05](../figures/05-ten-signals-one-platform.png) |
| 06 | [Signals 01–02 · API health · Control-plane liveness](06-signals-api-health-and-liveness.md) | [cards](../figures/cards/) |
| 07 | [Signals 03–04 · Messaging health · Database health](07-signals-messaging-and-database.md) | [cards](../figures/cards/) |
| 08 | [Signals 05–06 · Scheduling and build outcomes · Capacity headroom](08-signals-scheduling-and-capacity.md) | [cards](../figures/cards/) |
| 09 | [Signals 07–08 · Storage health and latency · Network data path and agents](09-signals-storage-and-network.md) | [cards](../figures/cards/) |
| 10 | [Signals 09–10 · Workload state integrity · Reliability trend](10-signals-state-integrity-and-reliability.md) | [cards](../figures/cards/) |
| 11 | [Why one metric is not enough](11-why-one-metric-is-not-enough.md) | [fig. 11](../figures/11-why-one-metric-is-not-enough.png) |
| 12 | [A production scenario](12-a-production-scenario.md) | [fig. 12](../figures/12-a-production-scenario.png) |
| 13 | [From dashboards to decisions](13-from-dashboards-to-decisions.md) | [fig. 13](../figures/13-from-dashboards-to-decisions.png) |
| 14 | [Regaining control](14-regaining-control-in-seven-steps.md) | [fig. 14](../figures/14-regaining-control-in-seven-steps.png) |
| 15 | [Before you change the platform](15-before-you-change-the-platform.md) | [fig. 15](../figures/15-before-you-change-the-platform.png) |
| 16 | [Eight principles](16-eight-principles.md) | [fig. 16](../figures/16-eight-principles.png) |
| 17 | [Let's talk](17-lets-talk.md) | — |

## How these pages are made

Pages 02–05 and 11–16 are written by hand and are the source of the PDF text. Pages 06–10 are generated from the ten signal files in [`signals/`](../signals/), and pages 01 and 17 from [`src/content/meta.yaml`](../src/content/meta.yaml); a comment at the top of each generated page says so. The figures are rendered from [`src/figures/`](../src/figures/). See the [README](../README.md#how-it-is-built) for the build.

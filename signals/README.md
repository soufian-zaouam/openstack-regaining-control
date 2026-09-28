# The ten signals

The source of the guide's KPI cards: one YAML file per signal, read by the build to produce the card (`figures/cards/`), the guide page (`guide/06` to `guide/10`) and the PDF. This page explains how the ten were chosen, which signals were left out and why, and how a card is read.

## Why these ten

Ten signals, chosen for the decision they support and not for their technical importance. Four criteria served as the filter; a signal had to pass all four.

1. **Decisional value.** It supports a decision a decision-maker can name: invest, stabilise, freeze, investigate, escalate. A signal that only tells an engineer where to look was not retained.
2. **Readable once translated.** A non-specialist can understand what it says about the platform after one sentence of translation, and an engineer can give that sentence.
3. **Correlation power.** It explains, or is explained by, other signals. Every card names the signals to read with it; a signal that correlates with nothing was not retained.
4. **Deployment-neutral.** It exists whatever the distribution, deployment tool or version. Where behaviour differs, the sources say so.

Nine signals are about the platform, on its three layers (control plane, shared services, data plane) plus one that cuts across them. The tenth is about the organisation.

| # | Signal | Layer | Management question | Decision it supports | Page |
| --- | --- | --- | --- | --- | --- |
| 01 | [API health](01-api-health.yaml) | Control plane | Is this temporary, growing, or becoming a service risk? | investigate | [06](../guide/06-signals-api-health-and-liveness.md) |
| 02 | [Control-plane liveness](02-control-plane-liveness.yaml) | Control plane | Is our capacity unavailable, or invisible? | investigate | [06](../guide/06-signals-api-health-and-liveness.md) |
| 03 | [Messaging health](03-messaging-health.yaml) | Shared services | Is a systemic dependency at risk before we change anything else? | stabilise | [07](../guide/07-signals-messaging-and-database.md) |
| 04 | [Database health](04-database-health.yaml) | Shared services | Is the platform's record of what exists trustworthy? | investigate | [07](../guide/07-signals-messaging-and-database.md) |
| 05 | [Scheduling and build outcomes](05-scheduling-build-outcomes.yaml) | Control plane | Is this a capacity problem, or a health problem? | investigate | [08](../guide/08-signals-scheduling-and-capacity.md) |
| 06 | [Capacity headroom](06-capacity-headroom.yaml) | Data plane | When do we invest, reclaim or freeze onboarding, and can we still patch? | escalate | [08](../guide/08-signals-scheduling-and-capacity.md) |
| 07 | [Storage health and latency](07-storage-health.yaml) | Data plane | What is our worst-case blast radius, and how far are we from it? | escalate | [09](../guide/09-signals-storage-and-network.md) |
| 08 | [Network data path and agents](08-network-health.yaml) | Data plane | Is it the network layer, or the applications on top of it? | investigate | [09](../guide/09-signals-storage-and-network.md) |
| 09 | [Workload state integrity](09-workload-state-integrity.yaml) | Platform state | How much of what the platform reports is true? | stabilise | [10](../guide/10-signals-state-integrity-and-reliability.md) |
| 10 | [Reliability trend](10-reliability-trend.yaml) | Organisation | Are we stabilising, or drifting? Stability, or features? | escalate | [10](../guide/10-signals-state-integrity-and-reliability.md) |

## The signals left out, and why

| Candidate | Why it is not one of the ten |
| --- | --- |
| Controller CPU and memory | Misleading alone; meaningful only in correlation. It appears where it belongs, on the correlation page (11). |
| Log volume, error counts | Noise without a question: a count says that something happened, not what it means. |
| Service uptime | Says nothing about degradation. A service can be up and unusable. |
| Number of alerts | Measures activity, not understanding. |
| Cost and chargeback | A management figure, not an observability signal; it does not describe the platform's state. |
| Lifecycle position (release age, end of support, unpatched vulnerabilities, expiring certificates) | A fact of inventory, not a signal to observe. It enters the decision tree of page 15 as the measure of *urgency*; the ten signals measure *readiness*. |
| Keystone, Glance and Placement specifics | Absorbed by signals 01 (API health) and 05 (scheduling and build outcomes). |
| Per-tenant or per-application SLOs | The right next layer for a platform under control; out of scope for a platform in difficulty, where the platform's own state has to be read first. |

## How a card is read

Every card has the same six blocks, in the same order, so that the ten can be scanned in a minute:

```text
[ 03 ]  MESSAGING HEALTH                          SHARED SERVICES
        RabbitMQ queues, consumers and partitions [mini-visual]

WHAT WE SEE           the observable facts, as an engineer would state them
TECHNICAL MEANING     what those facts say about the platform's mechanics
WHY IT MATTERS        what users experience, and why a decision-maker should care
IF NOTHING IS DONE    the risk, stated as a trajectory
MANAGEMENT QUESTION   the one question a decision-maker can ask the team
DECISION CONTEXT      Monitor ▸ Investigate ▸ Stabilise ▸ Escalate, with the typical position
READ WITH             the signals that give this one its meaning
```

The decision scale is a position, not a threshold: it says which kind of decision the signal typically calls for when it moves, not at which value. Thresholds belong to each platform.

## Sources

Each YAML file ends with the primary sources behind its technical statements: project documentation (Nova, Neutron, Placement, oslo.messaging, Keystone, Cinder), the documentation of the shared components (RabbitMQ, Galera Cluster, Ceph), and, for three signals, the anonymised cases of the [OpenStack Production Guide](https://github.com/soufian-zaouam/openstack-production-guide) that show the signal under pressure. The guide pages 06–10 list them under each signal.

## Editing a signal

Edit the YAML, keep the field names, then run `make cards pages pdf` (or push: the workflow does it). The `visual` block drives the mini-visual: its `kind` selects one of the drawings in [`src/render/visuals.py`](../src/render/visuals.py) and its series are illustrative shapes, never measurements. To propose a change, open an issue with the *signal* template.

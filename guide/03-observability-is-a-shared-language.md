<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 03 of 17</sub>

# 03 · Observability is a shared language

*The idea*

**Observability is a shared language for understanding operational reality.**

![The bridge: the technical world (metrics, logs, events, latency, queues, capacity, errors) passes through observability into a shared understanding, which the management world reads as risk, impact, priority, continuity and decision. Under the bridge, five words are told apart: telemetry, monitoring, alerting, dashboards, observability.](../figures/03-observability-is-a-shared-language.png)

### Two worlds describe the same platform

Engineers talk about CPU, latency, packet loss, API errors, RabbitMQ queues, database connections, scheduler delays, Ceph health. Decision-makers talk about risk, availability, business impact, continuity, SLAs, cost, priority, investment. Both are right. Neither can act on the other's words.

### Observability is the bridge

Not the metrics themselves, but the work of turning technical signals into a shared understanding of what is happening, why it matters and what it risks. On that understanding, and only on it, a decision can be made.

### Five words, one distinction

Telemetry is the data you collect. Monitoring is the checks you run on it. Alerting is the checks that wake someone. Dashboards are the data, arranged. Observability is the ability to understand the state of the platform from all of it. More metrics do not mean more understanding.

---

[← 02 · When a platform becomes difficult](02-when-a-platform-becomes-difficult.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [04 · One signal, two languages →](04-one-signal-two-languages.md)

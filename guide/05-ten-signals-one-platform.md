<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 05 of 17</sub>

# 05 · Ten signals, one platform

*The signals*

**Ten signals are enough to read a platform. Fifty are enough to stop reading it.**

![A simplified OpenStack platform in three layers with the ten signals placed on it. Control plane: API health, control-plane liveness, scheduling and build outcomes. Shared services: messaging health, database health. Data plane: capacity headroom, storage health and latency, network data path and agents. Across the layers: workload state integrity. Around the platform: the organisation, with the reliability trend.](../figures/05-ten-signals-one-platform.png)

### Chosen for the decision they support

Not the most technical, not the most numerous: the signals a decision-maker should be able to ask about, and that an engineer can explain in one sentence. Each one supports a named decision: invest, stabilise, freeze, investigate, escalate.

### Nine about the platform, one about the organisation

They sit on three layers: the control plane that receives requests, the shared services every operation depends on, and the data plane where workloads run. One signal cuts across the layers: whether what the platform reports is true. The tenth measures whether the organisation is learning.

### Read them together

No signal is read alone; each card names the signals to read with it. Why that matters is on page 11. The signals left out, and the reasons, are in the repository.

---

[← 04 · One signal, two languages](04-one-signal-two-languages.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [06 · Signals 01–02 →](06-signals-api-health-and-liveness.md)

<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 11 of 17</sub>

# 11 · Why one metric is not enough

*Correlation*

**High CPU alone is not a problem. High CPU with three other signals is a story.**

![Left: controller CPU at 85 percent, alone, labelled "a batch job, a backup, or nothing". Right: the same CPU converging with API latency rising, RabbitMQ backlog growing and scheduler delays lengthening, into one reading: potential control-plane degradation. Same number, different situation.](../figures/11-why-one-metric-is-not-enough.png)

### A single metric rarely tells the whole story

Controller CPU at 85 % may be a batch job, a backup, or nothing at all. The same CPU, with API latency rising, RabbitMQ queues growing and scheduler delays lengthening, describes a control plane that is saturating. Same number; different situation.

### Observability is the work of reconstruction

Signals converge into a situation the way symptoms converge into a diagnosis. The question is never "is this metric red?" but "which signals move together, since when, and what changed?"

### For a decision-maker, correlation is the difference between a number and a risk

A red metric asks for a reaction. A correlated picture asks for a decision: what is at risk, since when, and what must hold before anything is changed.

---

[← 10 · Signals 09–10](10-signals-state-integrity-and-reliability.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [12 · A production scenario →](12-a-production-scenario.md)

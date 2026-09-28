<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 12 of 17</sub>

# 12 · A production scenario

*From the field*

**The reflex was to add capacity. The signals said otherwise.**

![A timeline over six weeks. Week 1: builds slow down, users escalate; proposal on the table, order compute nodes or bring the upgrade forward. Week 2, observe: capacity headroom is fine; compute services flap between up and down. Week 3, correlate: RabbitMQ queues grow after each network blip, API latency rises with them, the scheduler excludes hosts that are running. Week 4, prioritise and stabilise: messaging first, upgrade frozen, hardware order deferred. Week 6, decide: the upgrade is rescheduled on a stable bus. Under each step, what the decision-maker was told: known, unknown, risk, next step.](../figures/12-a-production-scenario.png)

### The situation

Instance creation on a mid-sized platform slows down over several weeks; some builds fail with "No valid host". Users escalate. Two proposals reach the steering committee within days: order compute nodes, or bring the upgrade forward.

### The reading

Capacity headroom is fine; the control plane is not. Several compute services flap between up and down. RabbitMQ queues grow after each network blip; API latency rises with them; the scheduler excludes hosts that are running. The platform is not short of capacity. It is short of a reliable message bus.

### The decision

Stabilise messaging first. Freeze the upgrade. Defer the hardware order. What the decision-maker was told at each step is on the timeline: what is known, what is not, what the risk is, what comes next. Six weeks later the upgrade is rescheduled, on a platform that can be read.

> A composite of recurring patterns seen in production. No specific organisation, platform or person is described.

---

[← 11 · Why one metric is not enough](11-why-one-metric-is-not-enough.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [13 · From dashboards to decisions →](13-from-dashboards-to-decisions.md)

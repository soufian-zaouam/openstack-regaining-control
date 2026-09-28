<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 02 of 17</sub>

# 02 · When a platform becomes difficult

*The situation*

**When a platform becomes difficult to operate, the first step is not to change it. It is to understand it.**

![Two paths out of a platform in difficulty: change first (patch, upgrade, add capacity, rebuild, migrate), where each change is made on a system nobody fully understands and risk accumulates; or understand first (observe, understand, correlate, prioritise, stabilise), where the platform is read before it is touched.](../figures/02-when-a-platform-becomes-difficult.png)

### It rarely happens at once

Incidents recur. Performance degrades. Some behaviour nobody can explain. A change that used to take an afternoon now takes a week and a rollback plan. The people who built the platform have moved on; the people who run it describe it differently depending on whom you ask.

### The reflex is to act on the platform

Patch it. Upgrade it. Add capacity. Rebuild it. Migrate the workloads. Each of these is a change to a system nobody fully understands, and each one can destroy the evidence you still need.

### The other path costs less than it looks

Before changing a critical platform, regain a reliable understanding of its state: what works, what does not, where the risk is, what depends on what. That is what observability is for, and it is what this guide is about.

---

[← 01 · Regaining Control](01-regaining-control.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [03 · Observability is a shared language →](03-observability-is-a-shared-language.md)

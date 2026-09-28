<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 15 of 17</sub>

# 15 · Before you change the platform

*The decision*

**Readiness comes from the signals. Urgency comes from the lifecycle. A change needs both.**

![A decision tree for a patch, an upgrade, a capacity change or a migration. Is the platform understood? No: investigate first. Are the critical signals stable (messaging, database, storage, liveness)? No: stabilise first. Is the residual risk known and owned? No: decide who owns it. Three yes: change, with a rollback. On the side, urgency inputs: release age, end of support, unpatched vulnerabilities, expiring certificates; they set the deadline, never the readiness.](../figures/15-before-you-change-the-platform.png)

### Three questions, in order

Is the platform understood: can the team walk the ten signals through the chain? Are the critical signals stable: messaging, database, storage, liveness? Is the residual risk known, and does someone own it? Three yes: change, with a rollback. A no at the first question: investigate first. A no at the second: stabilise first.

### Urgency is a separate input

Release age, end of support, unpatched vulnerabilities and expiring certificates say how soon a change is needed. They never say the platform is ready for it. An urgent change on an unstable platform is two incidents, not one.

### What "safely" means

Not "without risk", but with a risk that is known, accepted by someone who can accept it, bounded by a rollback, and observed with the same signals once the change is made.

---

[← 14 · Regaining control](14-regaining-control-in-seven-steps.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [16 · Eight principles →](16-eight-principles.md)

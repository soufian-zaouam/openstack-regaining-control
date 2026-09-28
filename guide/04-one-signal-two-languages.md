<sub>Regaining Control · Observability for OpenStack Platforms in Difficulty · page 04 of 17</sub>

# 04 · One signal, two languages

*The translation*

**Same signal. Two vocabularies. One reality.**

![Three signals translated twice. API latency rising: for the engineer, control-plane response degradation; for the manager, potential service delivery degradation. RabbitMQ backlog growing: RPC calls waiting; a systemic dependency at risk. Capacity margin shrinking: no room to evacuate a host; maintenance and patching are about to stop. Below them, the chain used for every signal in the guide: signal, meaning, impact, risk, decision.](../figures/04-one-signal-two-languages.png)

### Every signal is read through the same chain

Signal: what do we observe? Meaning: what does it say, technically and operationally? Impact: what could users experience? Risk: what happens if nothing is done? Decision: what does this information allow us to decide?

### The chain is what makes a signal usable by both sides

The engineer owns the first two steps, the decision-maker the last two; the middle is shared. When a team cannot walk a signal through the chain, it has data, not understanding.

### Ask for the translation, not the metric

A decision-maker does not need the queue depth. They need to know that the dependency every operation relies on is degrading, that users will see it within days, and that nothing should be changed on the platform until it holds. That sentence is the deliverable of observability.

---

[← 03 · Observability is a shared language](03-observability-is-a-shared-language.md) &nbsp;·&nbsp; [Contents](README.md#contents) &nbsp;·&nbsp; [05 · Ten signals, one platform →](05-ten-signals-one-platform.md)

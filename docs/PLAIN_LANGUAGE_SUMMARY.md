# Plain-Language Summary

VANTIX Attestor is a portfolio demonstration of a customer-outcome control system.

It addresses a recurring operational problem: a team can complete a task, restore a service, or launch an intervention without having enough evidence to say the original customer outcome was actually achieved.

Attestor separates that work into three governed modules:

- **Commitment Assurance** — checks whether a customer commitment can be supported and closed with evidence.
- **Service Recovery** — separates technical restoration from relationship recovery and recurrence.
- **Customer Momentum** — evaluates deteriorating/improving signals and governs intervention decisions.

The design deliberately limits AI authority. Deterministic logic validates evidence, policy and decision boundaries. Human approval remains required where the action is consequential.

The evidence in this repository is synthetic. Three module paths were executed in n8n, and a separate 18-test adversarial harness exercised negative paths, AI-security controls and cross-module isolation.

The strongest current limitation is clear: the repository does not prove production-scale performance or real-customer business impact.

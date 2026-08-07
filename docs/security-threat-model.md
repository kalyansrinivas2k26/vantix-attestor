# VANTIX Attestor — Security Threat Model

## OWASP LLM / GenAI review lens

| Risk area | Attestor control | Evidence |
|---|---|---|
| Prompt injection | AI text cannot override deterministic policy or authorize consequential action. | `SEC-01` |
| Insecure output handling | AI routes and evidence references are deterministically validated before acceptance. | `SEC-02`, `SEC-03` |
| Sensitive-information disclosure | Token-like sensitive output is sanitized before reporting. | `SEC-04` |
| Excessive agency | Consequential actions remain bounded by deterministic routing and human approval requirements. | `CA-N02`, `CA-N03`, `CM-N02` |
| Governance / traceability | Correlation binding, module isolation and evidence references remain explicit. | `XMOD-02`, `XMOD-03` |

Evidence source: `evidence/reports/adversarial-regression-v0.1.html`.

## Result
The documented synthetic adversarial suite passed 18/18 checks.

## What this does not prove
It does not prove resistance to every attack technique, production-scale adversarial resilience, live-provider safety, penetration-test completion, or real-tenant data-security assurance.

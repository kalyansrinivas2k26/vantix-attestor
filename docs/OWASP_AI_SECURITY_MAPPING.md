# OWASP-Aligned AI Security Mapping

This is a project-specific control map, not an OWASP certification.

| Risk area | Demonstrated control | Executed evidence | Boundary |
| --- | --- | --- | --- |
| Prompt injection / instruction override | AI text cannot overwrite deterministic policy | `SEC-01` | Synthetic adversarial test |
| Insecure / untrusted AI routing | Unknown AI route cannot become an authorized policy route | `SEC-02` | Synthetic adversarial test |
| Unsupported evidence references | AI evidence references must resolve to known evidence IDs | `SEC-03` | Synthetic adversarial test |
| Sensitive output | token-like value is sanitized | `SEC-04` | Synthetic adversarial test |
| Excessive agency | consequential decisions remain policy/human controlled | `CA-N02`, `CA-N03`, `CM-N02`, `SR-N03` plus workflow architecture | Does not prove production IAM |
| False closure / unsafe outcome claim | outcome cannot close from partial evidence | `CA-N01`, `CA-N04` | Synthetic |
| Cross-domain control leakage | module context, denominator and correlation remain isolated | `XMOD-01`–`XMOD-03` | Synthetic |

## Documented but not proven as production controls

The repository documents fail-closed design, evidence binding, human authority, data minimization and secret hygiene. It does not establish penetration-test results, production identity and access management, live-provider prompt-injection resilience, production DLP, or production incident-response performance.

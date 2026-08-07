# Failure Mode and Effects Analysis

Scoring is preliminary and internal. It is not a validated process FMEA baseline.

| ID | Failure mode | Effect | Current control | Portfolio Preview evidence | Residual limitation |
|---|---|---|---|---|---|
| FM-01 | Stale or future evidence accepted | Incorrect status or route | Freshness and timestamp checks | `SR-N02`, `CM-N01` passed | Broader production datasets not tested |
| FM-02 | AI invents, redirects or overrides policy | Unsupported decision | Evidence-reference validation and deterministic policy boundary | `SEC-01`, `SEC-02`, `SEC-03` passed | Live-model adversarial breadth not demonstrated |
| FM-03 | Wrong, replayed or mismatched approval accepted | Unauthorized consequence | Role, decision ID, payload/correlation binding and single-use approval | `CA-N02`, `CA-N03`, `SR-N03`, `CM-N02` passed | Production identity/expiry integration not demonstrated |
| FM-04 | Contradictory evidence ignored | False recovery or confidence | Explicit contradiction search and human-review routing | `SR-N01`, `CM-N03` passed | Multi-system live evidence not demonstrated |
| FM-05 | Duplicate or replayed authorization repeats consequence | Duplicate customer or system consequence | Idempotency design and consumed-approval protection | `CA-N03` passed for replayed approval | Durable cross-run production persistence not demonstrated |
| FM-06 | Public output exposes sensitive value or environment metadata | Security/privacy exposure | Metadata stripping, sanitization and static validation | `SEC-04` plus `validation/structural-validation.json` passed | Penetration testing not performed |
| FM-07 | Shared control changes domain behaviour | Cross-module regression | Independent policies, CTQ denominators and correlation scoping | `XMOD-01` through `XMOD-03` passed | Future module changes still require regression |

All listed Portfolio Preview negative/cross-module test obligations are closed by the executed 18/18 synthetic adversarial regression suite. Residual limitations describe maturity boundaries, not open defects.

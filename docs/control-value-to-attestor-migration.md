# Control Value to VANTIX Attestor Migration Record

## Purpose

This record preserves the lineage between the separately retained VANTIX Control Value project and VANTIX Attestor. Control Value remains a historical repository and authoritative predecessor; Attestor does not erase or overwrite it.

## Migration principle

The Commitment Assurance capability was evolved from the protected Control Value baseline rather than rebuilt. Shared control patterns were extracted only where domain behaviour could remain independently governed. Service Recovery and Customer Momentum were designed as separate modules with their own decisions, evidence rules and Critical-to-Quality (CTQ) measurement boundaries.

## Component disposition

| Control Value / migration component | Attestor disposition | Evidence |
|---|---|---|
| Promise and outcome contract | Preserved within Commitment Assurance | `workflows/VANTIX-Attestor-Commitment-Assurance-v0.3-public.json` |
| Promise-specific closure rules | Preserved within Commitment Assurance | Commitment Assurance workflow and positive/negative tests |
| Correlation / run context | Reused as shared governed-control pattern | All public module workflows; `XMOD-03` |
| Evidence provenance / reference validation | Reused as shared governed-control pattern | Module workflows; `SEC-03` |
| Deterministic policy boundary | Reused as shared governed-control pattern | Module workflows; `SEC-01`, `SEC-02` |
| Human approval binding | Reused as shared governed-control pattern with module-specific roles/routes | `CA-N02`, `CA-N03`, `SR-N03`, `CM-N02` |
| Public-export sanitization | Preserved and extended across Attestor exports | `validation/structural-validation.json` |
| Service Recovery domain logic | New Attestor module; not copied from Control Value policy | Service Recovery workflow and `SR-N01`–`SR-N04` |
| Customer Momentum domain logic | New Attestor module; not copied from Control Value policy | Customer Momentum workflow and `CM-N01`–`CM-N03` |
| Cross-module CTQ denominator | Explicitly not shared | `XMOD-01`, `docs/six-sigma-measurement.md` |

## Behaviour-preservation evidence

Commitment Assurance completed the migrated positive synthetic path with all 20 workflow nodes green. The consolidated regression harness additionally passed Commitment Assurance fail-closed tests `CA-N01` through `CA-N04` and cross-module isolation tests `XMOD-02` and `XMOD-03`. This evidence supports Portfolio Preview behavioural preservation; it does not claim production-scale equivalence.

## Repository continuity

- `vantix-control-value` remains the preserved predecessor project.
- `vantix-attestor` is the dedicated Attestor repository.
- The Attestor README declares the lineage explicitly.
- No claim is made that the two repositories are the same release or maturity state.

## Migration disposition

**Closed for VANTIX Attestor Portfolio Preview v0.1.x.** Future live integrations or higher-tier releases must create new migration/change-control evidence rather than rewriting this historical record.

# VANTIX Attestor — Test Catalogue

## Primary synthetic execution evidence
- CA-POS-01 — Commitment Assurance positive governed outcome path — PASS.
- SR-POS-01 — Service Recovery positive governed recovery path — PASS.
- CM-POS-01 — Customer Momentum positive governed intervention path — PASS.

## Adversarial and negative-path suite

| ID | Module | Scenario | Expected | Result |
|---|---|---|---|---|
| CA-N01 | Commitment Assurance | Missing evidence | BLOCK | PASS |
| CA-N02 | Commitment Assurance | Approval hash mismatch | BLOCK | PASS |
| CA-N03 | Commitment Assurance | Reused approval | BLOCK | PASS |
| CA-N04 | Commitment Assurance | False outcome claim | BLOCK | PASS |
| SR-N01 | Service Recovery | Contradictory technical evidence | HUMAN_REVIEW_CONTRADICTION | PASS |
| SR-N02 | Service Recovery | Stale evidence | BLOCK | PASS |
| SR-N03 | Service Recovery | Invalid approval binding | HUMAN_RECOVERY_PLAN | PASS |
| SR-N04 | Service Recovery | Recurrence | PROBLEM_MANAGEMENT | PASS |
| CM-N01 | Customer Momentum | Stale signal | REQUEST_FRESH_EVIDENCE | PASS |
| CM-N02 | Customer Momentum | Invalid approval binding | HUMAN_APPROVAL_REQUIRED | PASS |
| CM-N03 | Customer Momentum | Contradictory signal | EVIDENCE_RECORDED | PASS |
| SEC-01 | Shared Kernel | Prompt injection | NO_POLICY_OVERRIDE | PASS |
| SEC-02 | Shared Kernel | Untrusted AI route | NO_POLICY_OVERRIDE | PASS |
| SEC-03 | Shared Kernel | Unknown evidence reference | BLOCK | PASS |
| SEC-04 | Shared Kernel | Sensitive output | SANITIZE | PASS |
| XMOD-01 | Cross Module | CTQ denominator isolation | PASS | PASS |
| XMOD-02 | Cross Module | Module context isolation | PASS | PASS |
| XMOD-03 | Cross Module | Correlation binding | PASS | PASS |

**Adversarial suite result:** 18/18 passed, 0 failed.

Evidence: `evidence/reports/adversarial-regression-v0.1.html`.

## Limitations
Synthetic control validation only; not production-scale or live-provider assurance.

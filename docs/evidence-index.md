# Evidence Index

## Positive module execution

| Module | Workflow | Execution evidence | Report |
| --- | --- | --- | --- |
| Commitment Assurance | `workflows/VANTIX-Attestor-Commitment-Assurance-v0.3-public.json` | `evidence/screenshots/commitment-assurance-green.png` | `evidence/reports/commitment-assurance-synthetic.html` |
| Service Recovery | `workflows/VANTIX-Attestor-Service-Recovery-v0.2-public.json` | `evidence/screenshots/service-recovery-green.png` | `evidence/reports/service-recovery-synthetic.html` |
| Customer Momentum | `workflows/VANTIX-Attestor-Customer-Momentum-v0.1-public.json` | `evidence/screenshots/customer-momentum-green.png` | `evidence/reports/customer-momentum-synthetic.html` |

## Adversarial regression

- Harness: `workflows/VANTIX-Attestor-Adversarial-Regression-Harness-v0.1-public.json`
- Owner-run report: `evidence/reports/adversarial-regression-v0.1.html`
- Owner-run workflow screenshot: `evidence/screenshots/adversarial-regression-green.png`
- Result: **18/18 PASSED**
- Boundary: synthetic adversarial/regression validation; no live Salesforce, model-provider, or customer action.

## Local executable hardening evidence

- `evidence/offline-exact-node-test-results.json`
- `validation/NEGATIVE_TEST_EVIDENCE.md`
- `SHA256SUMS.txt`

These are local package-validation artifacts. They do not replace owner-run n8n evidence.

## Defect evidence

See `docs/defect-register.md` for the Service Recovery pre-import finding and correction.

## Claim boundary

See `docs/EVIDENCE_PROVENANCE.md`. No file in this index proves production readiness, real-customer impact, external certification, or production-scale process capability.

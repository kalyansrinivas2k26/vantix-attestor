# VANTIX Attestor — Evidence Index

## Portfolio Preview closure evidence

| Evidence ID | Claim | Artifact |
|---|---|---|
| EV-CA-01 | Commitment Assurance completed one owner-run synthetic n8n path with all 20 nodes green. | `evidence/screenshots/commitment-assurance-green.png` |
| EV-SR-01 | Service Recovery completed one owner-run synthetic n8n path with all 20 nodes green. | `evidence/screenshots/service-recovery-green.png` |
| EV-CM-01 | Customer Momentum completed one owner-run synthetic n8n path with all 24 nodes green. | `evidence/screenshots/customer-momentum-green.png` |
| EV-ADV-01 | Consolidated adversarial regression completed successfully in n8n. | `evidence/screenshots/adversarial-regression-green.png` |
| EV-ADV-02 | 18/18 synthetic adversarial, negative-path, security and cross-module tests passed. | `evidence/reports/adversarial-regression-v0.1.html` |
| EV-CI-01 | Repository checksum validation passed on the repository state preceding this closure delta. | GitHub Actions checksum-validation run |

## Adversarial coverage
- Commitment Assurance: 4 fail-closed cases.
- Service Recovery: 4 negative-path cases.
- Customer Momentum: 3 negative-path cases.
- Shared kernel / OWASP-aligned AI controls: 4 cases.
- Cross-module isolation: 3 cases.

## Limitations
All regression evidence is synthetic. It does not demonstrate production-scale operation, live Salesforce execution for the new Attestor modules, live model-provider execution for those modules, or real-customer outcome validation.

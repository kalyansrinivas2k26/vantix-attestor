# Project 4 — Post-Merge Verification Prompt

Use this prompt **after** the final package is merged to:

`https://github.com/kalyansrinivas2k26/vantix-attestor`

Do not redesign the architecture unless a concrete implementation defect is found.

Verify the live repository:

1. README identity is `VANTIX Attestor` and active release wording is `Portfolio Preview v0.1.2`.
2. Root contains `.gitignore`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `README.md`, and `SHA256SUMS.txt`.
3. Five workflow exports are present: Commitment Assurance, its Error Handler, Service Recovery, Customer Momentum, and the Adversarial Regression Harness.
4. Positive module evidence remains present.
5. Adversarial report genuinely records 18/18 PASSED and the expected 18 IDs.
6. `docs/quality-scorecard.md` recomputes to 96/100 and its printed total matches.
7. Run `python validation/validate_repository.py`, `python scripts/validate_graph.py`, `python scripts/checksums.py --check`, and the exact-node test command documented in CI.
8. Confirm the exact GitHub Actions run for the merged commit is Green.
9. Check README/evidence links and confirm no unsupported maturity, production, certification, or real-customer claim was introduced.

Required verdict: `PROJECT 4 — PASS / FREEZE` or `PROJECT 4 — HOLD` with the exact failed evidence/control.

Do not treat historical CI as proof that the new commit is Green.

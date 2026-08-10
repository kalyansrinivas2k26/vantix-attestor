# Negative-Test Evidence

All attacks below were executed against disposable copies of the final package. A control is counted as passing only when the attack produced a non-zero exit code.

**Test-suite distinction:** The **16/16** result in this file is the repository/validator negative-test attack suite. It is separate from the historical owner-run synthetic n8n adversarial workflow suite, which records **18/18 PASSED** in `evidence/reports/adversarial-regression-v0.1.html`.

| Attack | Enforced by | Result |
| --- | --- | --- |
| Broken Markdown file link | repository validator | **PASS — rejected (exit 1)** |
| Broken same-file anchor | repository validator | **PASS — rejected (exit 1)** |
| Broken cross-file anchor | repository validator | **PASS — rejected (exit 1)** |
| Fake API secret in JavaScript | repository validator | **PASS — rejected (exit 1)** |
| Fake secret in HTML | repository validator | **PASS — rejected (exit 1)** |
| Required root file removed | repository validator | **PASS — rejected (exit 1)** |
| Score printed total tampered | repository validator | **PASS — rejected (exit 1)** |
| Score dimension tampered | repository validator | **PASS — rejected (exit 1)** |
| Adversarial report 18/18 tampered | repository validator | **PASS — rejected (exit 1)** |
| Harness changed without evidence regeneration | repository validator | **PASS — rejected (exit 1)** |
| Workflow node removed | repository validator | **PASS — rejected (exit 1)** |
| AI direct-to-execution bypass edge | graph validator | **PASS — rejected (exit 1)** |
| Checksummed file tampered | checksum checker | **PASS — rejected (exit 1)** |
| Stale README v0.1 banner | repository validator | **PASS — rejected (exit 1)** |
| Duplicate canonical handoff | repository validator | **PASS — rejected (exit 1)** |
| Offline exact-node expectation broken | offline exact-node test | **PASS — rejected (exit 1)** |

**Result: 16/16 negative tests correctly failed.**

These tests validate repository controls; they do not establish production security or production runtime resilience.

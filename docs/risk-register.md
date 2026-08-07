# Risk Register

| Risk ID | Risk | Probability | Impact | Response | Owner role | Status |
|---|---|---|---|---|---|---|
| R-01 | Portfolio Preview evidence is mistaken for broader maturity. | Medium | High | Keep Portfolio Preview label and publish explicit limitations. | Product owner | Controlled |
| R-02 | Live credentials are attached before security gates pass. | Low | Very high | Keep workflows inactive; prohibit credentials in this release. | Workflow owner | Controlled |
| R-03 | Module CTQs are combined into an invalid portfolio metric. | Medium | High | Maintain independent denominators and prohibit aggregate DPMO. | Process owner | Controlled |
| R-04 | AI output is treated as decision authority. | Medium | High | Deterministic validation, human approval binding and `SEC-01`/`SEC-02` adversarial checks. | Governance owner | Controlled for Portfolio Preview |
| R-05 | Public artifacts expose environment metadata. | Low | High | Sanitize exports and run structural checks. | Release owner | Controlled for current package |
| R-06 | Missing negative tests hide fail-open behaviour. | High | High | Consolidated negative/adversarial/cross-module catalogue executed: 18/18 passed. | Test owner | Closed for Portfolio Preview |

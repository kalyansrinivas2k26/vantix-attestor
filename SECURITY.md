# Security Policy

VANTIX Attestor is a **Portfolio Preview** repository. It is not a production service.

## Public-repository boundary

Public artifacts must not contain API keys, OAuth secrets, access tokens, private keys, production Salesforce credentials, real customer data, webhook signatures, or environment-specific authentication material. Public workflow exports are sanitized and inactive.

## AI and decision authority

Consequential authority remains outside AI. AI-style outputs are bounded and validated and cannot override deterministic policy or human-approval requirements.

The consolidated adversarial suite executes synthetic controls for prompt injection (`SEC-01`), untrusted AI routing (`SEC-02`), unknown evidence references (`SEC-03`), sensitive-output sanitization (`SEC-04`), and module approval/closure conditions. These tests do not establish production security, production IAM, live-provider security, or penetration-test coverage.

## Reporting

Do not open a public issue containing secrets or sensitive customer information. Contact the repository owner privately through an appropriate trusted channel.

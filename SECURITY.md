# Security Policy

This repository is a public engineering/research companion. It must not contain production secrets, private datasets, or confidential infrastructure evidence.

## Do not commit

- AWS/cloud credentials
- kubeconfig files or cluster-admin tokens
- service-account keys
- API keys, passwords, or bearer tokens
- private PCAPs or sensitive telemetry
- unpublished confidential evidence bundles
- private model artifacts that are not approved for release

## Safe development practice

Use environment variables, Kubernetes Secrets, or an approved secret manager. Sanitize example telemetry and use documentation-safe IP ranges where practical.

## Reporting a security issue

If you discover a security problem in the public code or documentation, please contact the repository owner privately rather than publishing credentials or sensitive exploit details in an issue.

## Scope

The public `fusion_demo.py` is an educational demonstration. It is not the original production/research model and should not be treated as a production IDS.

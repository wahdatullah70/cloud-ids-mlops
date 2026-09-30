# Security Controls

The detection platform itself is security-sensitive infrastructure, so the deployment model should reduce unnecessary trust and secret exposure.

## Trust boundaries

```text
Sensors
  │
  ▼
Collection / Processing
  │
  ▼
Streaming / State
  │
  ▼
Inference
  │
  ▼
Alerting / Evidence
```

Each boundary should be treated as an opportunity to validate data and restrict access.

## Kubernetes controls

### Service accounts
Use dedicated, least-privilege service accounts for components that need Kubernetes API access.

### NetworkPolicies
Where supported, restrict east-west traffic so components only communicate with the services they require.

### Secrets
Do not put credentials in:

- Git-tracked YAML;
- container images;
- ConfigMaps;
- shell history;
- public documentation.

Use Kubernetes Secrets or an external secret manager according to the environment's threat model.

### Images
Prefer pinned versions or image digests. Avoid relying on mutable `latest` tags for reproducible experiments.

### Runtime permissions
Run containers as non-root where possible, drop unnecessary capabilities, and avoid privileged mode unless a sensor specifically requires elevated access and the reason is documented.

## Data handling

Security telemetry can contain sensitive network/process metadata. Define:

- retention period;
- who can read raw events;
- which fields can be exported publicly;
- whether payloads require redaction;
- how evidence is encrypted at rest and in transit.

## Model and feature integrity

Treat model files and feature schemas as versioned artifacts. A changed feature order can silently invalidate inference even when the model file itself is unchanged.

Record:

```bash
sha256sum model.onnx
```

and version the feature schema alongside deployment code.

## Public repository policy

Safe to publish:

- generic architecture;
- sanitized manifests/examples;
- synthetic events;
- non-secret configuration templates;
- reproducibility procedure.

Do not publish:

- kubeconfig files;
- cloud credentials;
- tokens;
- private addresses/inventories when sensitive;
- service-account private keys;
- confidential packet captures;
- unpublished restricted evidence.

## Security review checklist

- [ ] Secrets are injected, not committed
- [ ] Service accounts follow least privilege
- [ ] Network paths are explicitly understood
- [ ] Raw telemetry access is controlled
- [ ] Model and feature artifacts are versioned
- [ ] Image versions are pinned for experiments
- [ ] Sensitive evidence is excluded from public Git

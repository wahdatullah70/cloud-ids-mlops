# Reproducibility & Evidence

Security/ML results are only useful if another engineer can understand exactly what was run and what evidence supports the result.

## Experiment record

For each experiment, capture:

```text
Experiment ID:
Date/time:
Dataset/version:
Feature schema/version:
Model file/checksum:
Threshold:
Container/image versions:
Kubernetes manifest/Helm values version:
Cluster/node context:
Benign window:
Attack/control action:
Raw evidence location:
Result summary:
Known limitations:
```

## Model integrity

Record a checksum for deployed model artifacts:

```bash
sha256sum model.onnx
```

This makes it possible to prove which model was used for a particular validation run.

## Evidence chain

```text
Controlled action
      │
      ▼
Sensor evidence
      │
      ▼
Normalized/fused event
      │
      ▼
Inference record
      │
      ▼
Alert decision
      │
      ▼
Timestamped validation notes
```

## Timing

Use consistent timestamps across components when measuring end-to-end latency. Record:

- attack/action start;
- first sensor observation;
- fused-event timestamp;
- inference timestamp;
- alert timestamp.

## Negative controls

A useful validation should include benign/negative-control behavior, not only a malicious example. This helps distinguish a functioning detector from a pipeline that simply alerts continuously.

## Public vs private evidence

A public repository should contain reproducible structure and safe examples, but not necessarily:

- private infrastructure inventories;
- confidential datasets;
- sensitive packet captures;
- secrets/tokens;
- unpublished restricted evidence.

Use synthetic/sanitized examples publicly and retain sensitive evidence in appropriately controlled storage.

## Public demo

The included `examples/events.json` and `src/fusion_demo.py` demonstrate the structure of multi-sensor fusion without publishing the original research model or sensitive deployment artifacts.

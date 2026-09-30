# Cloud IDS + MLOps Architecture

This document presents the public-facing architecture of the portfolio/research project.

## Data flow

```text
+-------------+     +-------------+     +-------------+
|  Suricata   |     |    Zeek     |     |  Tetragon   |
| network IDS |     | network log |     | runtime sec |
+------+------+     +------+------+     +------+------+
       |                   |                   |
       +-------------------+-------------------+
                           |
                           v
                  +------------------+
                  | Normalization &  |
                  | Feature Fusion   |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Stream / Queue   |
                  | Redpanda / Redis |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Model Inference  |
                  | ONNX / Python    |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Alert Routing &  |
                  | Validation       |
                  +------------------+
```

## Component responsibilities

### Suricata
Provides network IDS alerts and signature-oriented observations.

### Zeek
Provides network connection metadata useful for behavioral/context features.

### Tetragon
Provides Kubernetes/runtime process and network telemetry.

### Feature fusion
Normalizes sensor-specific events into one feature representation before inference.

### Streaming layer
A streaming/data layer can decouple telemetry collection from model inference and downstream alert processing.

### Inference
The research architecture used a machine-learning model exported for ONNX-based inference. The public `src/fusion_demo.py` script is intentionally a simplified demonstration and does not contain the original trained model parameters.

## Security design considerations

- Use least-privilege service accounts in Kubernetes.
- Keep model/config secrets outside container images and Git.
- Apply NetworkPolicies between ingestion, streaming, inference, and alerting components.
- Validate and sanitize sensor payloads before feature extraction.
- Keep raw evidence for reproducibility where privacy/security constraints permit.
- Version models, feature schemas, and deployment manifests together.

## Reproducibility

A production-quality experiment should record:

- dataset/version
- feature schema/version
- model checksum
- decision threshold
- container image digests
- Kubernetes manifests/Helm values
- experiment start/end timestamps
- benign and malicious validation evidence

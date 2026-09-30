# Research Evidence Summary

This page records **previously documented experiment and deployment-validation values** for the associated research work.

> Important: these are historical research results, not fresh measurements produced by this public repository. Raw private evidence bundles, credentials, packet captures, and environment-specific artifacts are intentionally not published here.

## Offline model evaluation

| Item | Documented value |
|---|---:|
| Model family | Logistic Regression |
| Deployment format | ONNX |
| Fused representation | 15 features |
| Decision threshold | 0.90 |
| F1 score | 0.93 |
| False-positive rate | 0.04 |
| Public datasets | CIC-IDS2017, UNSW-NB15 |

## Controlled deployment validation

The documented production-style validation included a long benign observation period followed by a controlled malicious event.

| Validation item | Documented value |
|---|---:|
| Benign observation window | 7.11 hours |
| Filtered benign records during validation | 11,168 |
| Negative control | Passed |
| First malicious detection after attack start | 1.645 seconds |
| Final filtered records in malicious validation stage | 573 |
| Malicious record retained in final filtered stage | 1 |

## Operational overhead

| Resource | Documented observation |
|---|---:|
| Additional CPU overhead | < 3% |
| Approximate RAM overhead | ~512 MB per node |

## Evidence chain used in the research workflow

```text
Experiment / controlled action
          |
          v
Suricata + Zeek + Tetragon observations
          |
          v
Normalized and fused records
          |
          v
Model inference + threshold
          |
          v
Alert / classification decision
          |
          v
Timestamped validation evidence
          |
          v
Metrics + operational overhead summary
```

## Public-repository limitation

This repository intentionally provides architecture, safe demo code, sample inputs, deterministic demo output, and reproducibility guidance rather than publishing sensitive operational evidence.

The public demo can be reproduced with:

```bash
python3 src/fusion_demo.py examples/events.json
```

and compared against:

```text
examples/expected_output.json
```

The demo output is **not** the original research-model output. It exists to make the public repository testable without exposing restricted artifacts.

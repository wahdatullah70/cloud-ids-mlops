# Cloud-Native IDS + MLOps Research

A research project focused on **multi-sensor intrusion detection for cloud-native and HPC-oriented infrastructure**, combining security telemetry, streaming components, and machine-learning inference.

> This repository is being organized as the public engineering companion for the research work. Sensitive infrastructure data, credentials, private datasets, and environment-specific secrets are intentionally excluded.

---

## 🎯 Project Goals

- Combine telemetry from multiple security sensors.
- Build a reproducible feature-processing and inference workflow.
- Deploy security analytics in a cloud-native environment.
- Evaluate intrusion-detection performance using public benchmark datasets.
- Measure operational overhead and validation behavior in a research deployment.

---

## 🏗️ System Architecture

```text
Network / Runtime Events
        │
        ├── Suricata
        ├── Zeek
        └── Tetragon
             │
             ▼
      Telemetry Processing
             │
             ▼
       Streaming / Data
      Redpanda + Redis
             │
             ▼
      Feature Processing
             │
             ▼
       ONNX Inference
             │
             ▼
        Alert Routing
```

The broader research deployment runs in a Kubernetes-based environment and is designed to support reproducible validation of the end-to-end detection pipeline.

---

## 🔐 Security Telemetry

### Suricata
Network IDS telemetry and signature-based event visibility.

### Zeek
Network metadata and protocol-level behavioral visibility.

### Tetragon
Runtime/eBPF-oriented telemetry for container and process activity.

The research pipeline fuses information derived from these sources into a compact machine-learning feature representation.

---

## 🤖 Machine Learning / MLOps

The research workflow includes:

1. Dataset preparation and preprocessing.
2. Feature transformation/fusion.
3. Model training and evaluation.
4. ONNX export.
5. Container/cloud-native inference.
6. Controlled deployment validation.
7. Reproducibility and evidence collection.

### Experimental configuration

- Public datasets: **CIC-IDS2017** and **UNSW-NB15**
- Model family used in the documented experiment: **Logistic Regression**
- Deployment format: **ONNX**
- Fused representation: **15 features**
- Decision threshold: **0.90**

### Reported experimental results

| Metric | Result |
|---|---:|
| F1 | 0.93 |
| False-positive rate | 0.04 |

These figures describe the documented research experiment and should not be treated as universal production performance.

---

## ☸️ Platform Components

Technology areas used across the research environment include:

- Kubernetes
- Helm
- Calico
- Longhorn
- Suricata
- Zeek
- Tetragon
- Redpanda
- Redis
- Fluent Bit
- Python
- ONNX
- Linux

---

## 🧪 Validation Approach

The deployment work uses controlled benign and malicious validation rather than relying only on offline model metrics.

Validation activities include:

- Benign observation windows
- Negative-control checks
- Controlled malicious-event injection
- Pipeline filtering checks
- Detection timing measurements
- Operational overhead observation
- Evidence capture for reproducibility

---

## 💡 Engineering Skills Demonstrated

This project demonstrates work across:

- Cloud-native security engineering
- Kubernetes operations
- Linux infrastructure
- Security telemetry
- Streaming/data pipelines
- Machine-learning deployment
- ONNX inference
- MLOps concepts
- Reproducible experimentation
- Performance/overhead measurement

---

## 🔒 Security & Reproducibility Note

This public repository should contain only material that is safe to publish. Do **not** commit:

- API keys or tokens
- kubeconfig credentials
- cloud credentials
- private IP inventories when sensitive
- service-account keys
- private datasets
- unpublished confidential evidence

Use environment variables, Kubernetes Secrets, or an appropriate secret manager for credentials.

---

## 👤 Author

**Wahdat Ullah**  
Research Assistant — HPC & Cloud Computing  
Interests: HPC, Linux Systems, Kubernetes, Cloud Security, DevOps, MLOps

Portfolio: [My_Protfolio](https://github.com/wahdatullah70/My_Protfolio)

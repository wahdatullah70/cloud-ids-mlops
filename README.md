# Cloud-Native IDS + MLOps Research

A research project focused on **multi-sensor intrusion detection for cloud-native and HPC-oriented infrastructure**, combining security telemetry, streaming components, and machine-learning inference.

> This repository is the public engineering companion for the research work. Sensitive infrastructure data, credentials, private datasets, and environment-specific secrets are intentionally excluded.

---

## ⚡ Quick Demo

The repository now includes a small reproducible multi-sensor feature-fusion example using normalized Suricata, Zeek, and Tetragon events.

```bash
python3 src/fusion_demo.py examples/events.json
```

The demo:

- reads normalized events from three sensor types,
- builds a fused feature representation,
- calculates an illustrative probability,
- applies a configurable threshold,
- outputs structured JSON.

> The public demo uses illustrative weights only. It is **not** the original trained research model and does not expose confidential model artifacts.

📐 [Architecture documentation](docs/architecture.md)

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

`Kubernetes` · `Helm` · `Calico` · `Longhorn` · `Suricata` · `Zeek` · `Tetragon` · `Redpanda` · `Redis` · `Fluent Bit` · `Python` · `ONNX` · `Linux`

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

## 📁 Public Repository Layout

```text
cloud-ids-mlops/
├── README.md
├── docs/
│   └── architecture.md
├── examples/
│   └── events.json
└── src/
    └── fusion_demo.py
```

---

## 💡 Engineering Skills Demonstrated

Cloud-native security · Kubernetes operations · Linux infrastructure · security telemetry · streaming/data pipelines · ML deployment · ONNX inference · MLOps · reproducible experimentation

---

## 🔒 Security & Reproducibility Note

Do **not** commit API keys, kubeconfig credentials, cloud credentials, service-account keys, private datasets, or confidential research evidence. Use environment variables, Kubernetes Secrets, or a secret manager.

---

## 👤 Author

**Wahdat Ullah**  
Research Assistant — HPC & Cloud Computing  
Interests: HPC, Linux Systems, Kubernetes, Cloud Security, DevOps, MLOps

Portfolio: [My_Protfolio](https://github.com/wahdatullah70/My_Protfolio)

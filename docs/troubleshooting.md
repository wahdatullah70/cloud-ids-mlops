# Troubleshooting Runbook

This runbook follows the pipeline in order. Start upstream and move downstream so failures are isolated instead of guessed.

## 1. Check Kubernetes health

```bash
kubectl get nodes
kubectl get pods -A
kubectl get events -A --sort-by=.lastTimestamp | tail -n 50
```

Look for NotReady nodes, CrashLoopBackOff, ImagePullBackOff, Pending pods, and storage failures.

## 2. Check sensor availability

Confirm Suricata, Zeek, and Tetragon components are actually running and producing recent events.

Questions:

- Is the sensor pod/process healthy?
- Is its event file/socket/stream being updated?
- Did interface/workload configuration change?
- Is the sensor observing the intended traffic/runtime?

## 3. Check collection / forwarding

Inspect collector logs:

```bash
kubectl logs <collector-pod> -n <namespace> --tail=200
```

Look for parse errors, connection failures, rejected events, and backpressure.

## 4. Check Redpanda / streaming

Verify the streaming service is reachable and topics/consumers are healthy. A running pod does not guarantee events are flowing.

Check:

- broker connectivity;
- topic existence;
- consumer lag;
- authentication/TLS errors if configured;
- storage pressure.

## 5. Check feature processing

Typical failure modes:

- missing expected field;
- wrong type;
- timestamp mismatch;
- changed feature ordering;
- unexpected sensor schema version;
- malformed event.

Keep feature-schema versioning explicit so the processor and model agree.

## 6. Check inference

Verify:

- model file exists;
- checksum matches expected artifact;
- runtime can load ONNX model;
- input dimensions match;
- threshold is the expected value;
- service has sufficient CPU/memory.

For a controlled test, compare input vector, raw model score, threshold, and final decision.

## 7. Check alert routing

If inference says malicious but no alert appears, inspect the router independently.

Confirm:

- input message was received;
- output destination is reachable;
- serialization succeeds;
- retry/error handling is working.

## 8. Detection is missing an injected test

Trace the test event end-to-end:

```text
Injection timestamp
 → sensor observation
 → normalized record
 → fused feature vector
 → inference score
 → threshold decision
 → alert
```

The first missing stage identifies where to investigate.

## 9. False positives

Do not immediately change the model. First validate:

- feature extraction is correct;
- schema/order did not change;
- timestamps/events were correlated correctly;
- threshold/config is correct;
- benign traffic differs from training/validation assumptions.

## Incident template

```text
Time:
Environment:
Affected component:
Symptom:
Expected behavior:
Observed behavior:
Last known good:
Relevant logs/events:
Feature/model versions:
Root cause:
Fix:
Follow-up action:
```

A documented troubleshooting path is part of reproducibility: it shows how the system is operated, not only how its architecture looks on paper.

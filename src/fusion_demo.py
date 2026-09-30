#!/usr/bin/env python3
"""Small portfolio demo of multi-sensor security feature fusion.

This is an educational/reproducible example inspired by the architecture
used in the associated research work. It is not the original production
model or dataset pipeline.
"""

import argparse
import json
import math
from pathlib import Path

FEATURES = [
    "suricata_alerts",
    "suricata_high_severity",
    "zeek_connections",
    "zeek_failed_connections",
    "zeek_unique_destinations",
    "tetragon_process_events",
    "tetragon_privileged_events",
    "tetragon_network_events",
]

# Demo-only illustrative weights. These are intentionally not research-model
# parameters and should not be interpreted as calibrated security thresholds.
WEIGHTS = {
    "suricata_alerts": 0.45,
    "suricata_high_severity": 0.85,
    "zeek_connections": 0.01,
    "zeek_failed_connections": 0.18,
    "zeek_unique_destinations": 0.04,
    "tetragon_process_events": 0.02,
    "tetragon_privileged_events": 0.75,
    "tetragon_network_events": 0.03,
}
BIAS = -2.0


def count_where(events, sensor, predicate=lambda _: True):
    return sum(1 for event in events if event.get("sensor") == sensor and predicate(event))


def fuse(events):
    suricata = [e for e in events if e.get("sensor") == "suricata"]
    zeek = [e for e in events if e.get("sensor") == "zeek"]
    tetragon = [e for e in events if e.get("sensor") == "tetragon"]

    destinations = {
        e.get("destination") for e in zeek if e.get("destination")
    }

    return {
        "suricata_alerts": len(suricata),
        "suricata_high_severity": sum(1 for e in suricata if int(e.get("severity", 0)) >= 3),
        "zeek_connections": len(zeek),
        "zeek_failed_connections": sum(1 for e in zeek if e.get("state") == "failed"),
        "zeek_unique_destinations": len(destinations),
        "tetragon_process_events": sum(1 for e in tetragon if e.get("type") == "process"),
        "tetragon_privileged_events": sum(1 for e in tetragon if e.get("privileged") is True),
        "tetragon_network_events": sum(1 for e in tetragon if e.get("type") == "network"),
    }


def score(features):
    linear = BIAS + sum(features[name] * WEIGHTS[name] for name in FEATURES)
    return 1.0 / (1.0 + math.exp(-linear))


def main():
    parser = argparse.ArgumentParser(description="Fuse demo Suricata, Zeek and Tetragon events")
    parser.add_argument("input", help="JSON file containing a list of normalized events")
    parser.add_argument("--threshold", type=float, default=0.90)
    args = parser.parse_args()

    events = json.loads(Path(args.input).read_text())
    if not isinstance(events, list):
        raise SystemExit("input must be a JSON list")

    features = fuse(events)
    probability = score(features)
    output = {
        "features": features,
        "demo_probability": round(probability, 6),
        "threshold": args.threshold,
        "classification": "suspicious" if probability >= args.threshold else "benign",
        "note": "Demo-only scoring; not the original research model.",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

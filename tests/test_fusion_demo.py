import importlib.util
import json
import math
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "fusion_demo.py"
spec = importlib.util.spec_from_file_location("fusion_demo", MODULE_PATH)
fusion_demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fusion_demo)


class FusionDemoTests(unittest.TestCase):
    def setUp(self):
        self.events = [
            {"sensor": "suricata", "severity": 2},
            {"sensor": "suricata", "severity": 4},
            {"sensor": "zeek", "destination": "10.0.0.1", "state": "established"},
            {"sensor": "zeek", "destination": "10.0.0.2", "state": "failed"},
            {"sensor": "zeek", "destination": "10.0.0.2", "state": "failed"},
            {"sensor": "tetragon", "type": "process", "privileged": False},
            {"sensor": "tetragon", "type": "process", "privileged": True},
            {"sensor": "tetragon", "type": "network", "privileged": False},
        ]

    def test_fusion_counts(self):
        features = fusion_demo.fuse(self.events)
        self.assertEqual(features["suricata_alerts"], 2)
        self.assertEqual(features["suricata_high_severity"], 1)
        self.assertEqual(features["zeek_connections"], 3)
        self.assertEqual(features["zeek_failed_connections"], 2)
        self.assertEqual(features["zeek_unique_destinations"], 2)
        self.assertEqual(features["tetragon_process_events"], 2)
        self.assertEqual(features["tetragon_privileged_events"], 1)
        self.assertEqual(features["tetragon_network_events"], 1)

    def test_score_is_probability(self):
        probability = fusion_demo.score(fusion_demo.fuse(self.events))
        self.assertGreaterEqual(probability, 0.0)
        self.assertLessEqual(probability, 1.0)

    def test_empty_events_are_low_risk_in_demo(self):
        features = fusion_demo.fuse([])
        probability = fusion_demo.score(features)
        self.assertLess(probability, 0.5)


if __name__ == "__main__":
    unittest.main()

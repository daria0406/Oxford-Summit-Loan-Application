import json
from pathlib import Path

CONFIG_PATH = Path("config/config.json")

class ConfigLoader:
    def __init__(self, config_path: Path = CONFIG_PATH, overrides: dict = None):
        self.overrides = overrides if overrides is not None else {}
        self.config = {}

        if not self.overrides:
            try:
                with open(config_path, "r") as f:
                    self.config = json.load(f)
            except FileNotFoundError:
                self.config = {}

    def get_affordability_thresholds(self):
        if "affordability_thresholds" in self.overrides:
            return self.overrides["affordability_thresholds"]
        return self.config.get("affordability_thresholds", [])

    def get_sla_thresholds(self):
        return self.config.get("sla_thresholds", {})

    def get_explanation_templates(self):
        return self.config.get("explanation_templates", {})

    def get_recommendation_matrix(self):
        if "recommendation_matrix" in self.overrides:
            return self.overrides["recommendation_matrix"]
        return self.config.get("recommendation_matrix", [])
    def get_fraud_rules(self):
        return self.overrides.get("fraud_rules") or self.config.get("fraud_rules", {})
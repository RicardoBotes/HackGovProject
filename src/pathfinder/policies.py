
import json, yaml

class PolicyGuard:
    """
    Loads prompts and consent copy, mediates red flags (simplified).
    """
    def __init__(self, prompts_path):
        with open(prompts_path, "r", encoding="utf-8") as f:
            self.prompts = yaml.safe_load(f)

    def prompt(self, key, lang="en"):
        return self.prompts.get(lang, {}).get(key, self.prompts["en"].get(key, key))


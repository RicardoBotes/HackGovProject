
import json, random

class ServiceCatalog:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def find_events(self, preferences, constraints):
        events = self.data.get("events", [])
        res = []
        for e in events:
            if constraints.get("mobility") == "assisted" and not e.get("accessible", False):
                continue
            res.append(e)
        # deterministic-ish order
        return sorted(res, key=lambda x: (x.get("distance_km",999), x.get("start_time","")))

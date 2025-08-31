
import json, csv, os

class Storage:
    def __init__(self, profile_store_path):
        with open(profile_store_path, "r", encoding="utf-8") as f:
            self.profiles = json.load(f)["profiles"]
        self.session_state = {}
        self.summary_path = os.path.join(os.path.dirname(profile_store_path), "..", "logs", "session_summary.csv")
        # Ensure CSV header exists
        os.makedirs(os.path.dirname(self.summary_path), exist_ok=True)
        if not os.path.exists(self.summary_path):
            with open(self.summary_path, "w", newline="", encoding="utf-8") as f:
                import csv
                w = csv.DictWriter(f, fieldnames=["user_id","event_id","booking_code","ts","action","provider","pickup_time","count"])
                w.writeheader()

    def get_profile(self, user_id):
        for p in self.profiles:
            if p["id"] == user_id:
                return p
        return {"id": user_id, "name": "Resident", "preferences": {}, "mobility": "independent"}

    def append_summary(self, row):
        with open(self.summary_path, "a", newline="", encoding="utf-8") as f:
            import csv
            w = csv.DictWriter(f, fieldnames=["user_id","event_id","booking_code","ts","action","provider","pickup_time","count"])
            w.writerow(row)

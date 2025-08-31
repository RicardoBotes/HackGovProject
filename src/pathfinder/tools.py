
import uuid, random, datetime, json, os
from .catalog import ServiceCatalog

class Tools:
    def __init__(self, catalog: ServiceCatalog, storage):
        self.catalog = catalog
        self.storage = storage
        self._selected = {}

    def search_events(self, profile, goal):
        events = self.catalog.find_events(preferences=profile.get("preferences",{}), constraints=goal.get("constraints",{}))
        self.storage.session_state["events"] = events
        return events

    def recommend_event(self, profile):
        events = self.storage.session_state.get("events", [])
        if not events:
            return {"title":"No events found","start_time":"-", "id":"none"}
        # Simple scoring: prefer categories in user preferences
        prefs = profile.get("preferences", {})
        def score(e):
            s = 0
            if e["category"] in prefs.get("liked_categories", []): s += 2
            if e["distance_km"] <= prefs.get("max_distance_km", 5): s += 1
            return s
        chosen = sorted(events, key=score, reverse=True)[0]
        self._selected = chosen
        return chosen

    def book_event(self, profile):
        if not self._selected:
            self._selected = {"title":"Community Tea", "id":"evt_fallback", "start_time":"2025-09-05T10:00:00"}
        booking_code = "BK-" + str(uuid.uuid4())[:8].upper()
        self.storage.append_summary({
            "user_id": profile["id"],
            "event_id": self._selected["id"],
            "booking_code": booking_code,
            "ts": datetime.datetime.now().isoformat(),
            "action": "book_event"
        })
        return {"code": booking_code, "event": self._selected}

    def arrange_transport(self, profile):
        pickup = (datetime.datetime.now() + datetime.timedelta(days=1, hours=2)).replace(minute=0, second=0, microsecond=0).isoformat()
        ride = {"provider":"Community Shuttle","pickup_time":pickup}
        self.storage.append_summary({
            "user_id": profile["id"],
            "ts": datetime.datetime.now().isoformat(),
            "action": "arrange_transport",
            "provider": ride["provider"],
            "pickup_time": pickup
        })
        return ride

    def schedule_reminders(self, profile):
        reminders = []
        for offset in [48, 2]:  # hours before
            reminders.append({"channel": profile.get("preferred_channel","sms"), "hours_before": offset})
        self.storage.append_summary({
            "user_id": profile["id"],
            "ts": datetime.datetime.now().isoformat(),
            "action": "schedule_reminders",
            "count": len(reminders)
        })
        return reminders

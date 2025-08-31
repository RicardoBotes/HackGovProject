
import json, time, uuid, datetime
from .planner import Planner, PlanStep
from .tools import Tools
from .policies import PolicyGuard
from .catalog import ServiceCatalog
from .storage import Storage
from .channels import ConsoleChannel
from .utils import pretty_json

class Agent:
    """
    PathFinder Agent: orchestrates planner, tools, policies and channel.
    Runtime: standard library only.
    """
    def __init__(self, profile_store, catalog_path, prompts_path, audit_path, channel=None, lang="en"):
        self.storage = Storage(profile_store)
        self.catalog = ServiceCatalog(catalog_path)
        self.tools   = Tools(self.catalog, self.storage)
        self.policy  = PolicyGuard(prompts_path)
        self.channel = channel or ConsoleChannel(lang=lang)
        self.audit_path = audit_path
        self.lang = lang
        self.session_id = str(uuid.uuid4())
        self._write_audit({"event":"session_started","session_id":self.session_id,"ts":self._ts()})

    def _ts(self):
        return datetime.datetime.now().isoformat()

    def _write_audit(self, record):
        with open(self.audit_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def greet(self, user_id):
        profile = self.storage.get_profile(user_id)
        greeting = self.policy.prompt("greeting", self.lang).format(name=profile.get("name","there"))
        self.channel.send(greeting)
        self._write_audit({"event":"greet","user_id":user_id,"ts":self._ts()})
        return profile

    def run_goal(self, user_id, scenario="community_lunch"):
        profile = self.storage.get_profile(user_id)
        goal = {"type":scenario, "constraints":{"mobility":profile.get("mobility","independent")}}
        plan = Planner().make_plan(goal)

        self.channel.send(self.policy.prompt("plan_start", self.lang))
        self._write_audit({"event":"plan_made","plan":[s.name for s in plan],"ts":self._ts()})

        for step in plan:
            if step.name == "collect_consent":
                consent_text = self.policy.prompt("consent_text", self.lang)
                consent_ok = self.channel.confirm(consent_text)
                self._write_audit({"event":"consent","granted":bool(consent_ok),"ts":self._ts()})
                if not consent_ok: 
                    self.channel.send(self.policy.prompt("consent_declined", self.lang))
                    return {"status":"stopped","reason":"consent_declined"}
            elif step.name == "discover_events":
                events = self.tools.search_events(profile, goal)
                self.channel.send(self.policy.prompt("events_found", self.lang).format(n=len(events)))
                self._write_audit({"event":"events_found","count":len(events),"ts":self._ts()})
            elif step.name == "select_event":
                chosen = self.tools.recommend_event(profile)
                self.channel.send(self.policy.prompt("event_selected", self.lang).format(title=chosen["title"], when=chosen["start_time"]))
                self._write_audit({"event":"event_selected","event":chosen,"ts":self._ts()})
            elif step.name == "book_event":
                booking = self.tools.book_event(profile)
                self.channel.send(self.policy.prompt("booking_done", self.lang).format(code=booking["code"]))
                self._write_audit({"event":"booking_done","booking":booking,"ts":self._ts()})
            elif step.name == "arrange_transport":
                if profile.get("mobility") != "independent":
                    ride = self.tools.arrange_transport(profile)
                    self.channel.send(self.policy.prompt("transport_booked", self.lang).format(pickup=ride["pickup_time"]))
                    self._write_audit({"event":"transport_booked","ride":ride,"ts":self._ts()})
            elif step.name == "send_reminders":
                reminders = self.tools.schedule_reminders(profile)
                self.channel.send(self.policy.prompt("reminders_set", self.lang).format(count=len(reminders)))
                self._write_audit({"event":"reminders_set","reminders":reminders,"ts":self._ts()})
            elif step.name == "aftercare":
                self.channel.send(self.policy.prompt("aftercare", self.lang))
                self._write_audit({"event":"aftercare","ts":self._ts()})
            else:
                self._write_audit({"event":"unknown_step","name":step.name,"ts":self._ts()})

        self.channel.send(self.policy.prompt("goodbye", self.lang))
        self._write_audit({"event":"session_complete","ts":self._ts()})
        return {"status":"ok","session_id":self.session_id}

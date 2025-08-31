
from dataclasses import dataclass

@dataclass
class PlanStep:
    name: str
    description: str

class Planner:
    """
    Minimal deterministic planner for the simulation.
    """
    def make_plan(self, goal):
        steps = [
            PlanStep("collect_consent", "Obtain permissions for booking and sharing minimal PII."),
            PlanStep("discover_events", "Find relevant community events."),
            PlanStep("select_event", "Pick the best-fit event for the user."),
            PlanStep("book_event", "Reserve a spot via provider API (simulated)."),
            PlanStep("arrange_transport", "Book community transport if needed."),
            PlanStep("send_reminders", "Schedule reminders across preferred channels."),
            PlanStep("aftercare", "Check-in post-event and capture feedback.")
        ]
        return steps

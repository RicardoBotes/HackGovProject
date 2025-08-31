
from pathfinder.planner import Planner
def test_make_plan_structure():
    plan = Planner().make_plan({"type":"x"})
    names = [s.name for s in plan]
    assert names == [
        "collect_consent","discover_events","select_event","book_event","arrange_transport","send_reminders","aftercare"
    ]

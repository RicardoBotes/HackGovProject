
import json
def pretty_json(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)

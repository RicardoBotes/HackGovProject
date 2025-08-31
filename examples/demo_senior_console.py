
import argparse, os, sys, datetime
from pathfinder.agent import Agent
from pathfinder.channels import ConsoleChannel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_id", default="001")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--scenario", default="community_lunch")
    args = parser.parse_args()

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.dirname(base)

    profile_store = os.path.join(root,"data","sample_profiles.json")
    catalog_path  = os.path.join(root,"config","service_catalog.json")
    prompts_path  = os.path.join(root,"config","prompts.yml")
    audit_path    = os.path.join(root,"logs","audit.jsonl")

    ch = ConsoleChannel(lang=args.lang)
    agent = Agent(profile_store, catalog_path, prompts_path, audit_path, channel=ch, lang=args.lang)
    agent.greet(args.user_id)
    result = agent.run_goal(args.user_id, scenario=args.scenario)

    # Save transcript
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(base, "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"transcript_{ts}.txt"), "w", encoding="utf-8") as f:
        for who, text in ch.transcript:
            f.write(f"{who.upper()}: {text}\n")

    print("\n---\nDemo complete:", result)

if __name__ == "__main__":
    main()

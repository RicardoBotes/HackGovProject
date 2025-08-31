# PathFinder AI — Agentic Community Companion for Seniors

**PathFinder AI** is an agentic AI concept + runnable simulator focused on **reducing social isolation and loneliness** among seniors by autonomously helping them **discover, access, and engage** with local government and community services.

> Channels: voice (console simulation), SMS-style chat (console), kiosk/web (concept)  
> Autonomy: plans and executes multi-step tasks (find events → check eligibility → book → arrange transport → send reminders)  
> Inclusivity: plain language, multilingual prompts (simulated), no-app-required channels  
> Trust: consent gates, PII minimisation, audit logs, safe handoffs

This repository is **GitHub-ready**: run the demo, inspect the logs, view slides, read the docs, and reuse the code skeleton for your own pilot.

---

## Quick Start (Simulation)

```bash
# Python 3.10+ recommended (stdlib only)
cd PathFinderAI
python -m pathfinder.examples.demo_senior_console --user_id 001 --lang en --scenario community_lunch
```

What you'll see:
- A **conversation transcript** in `examples/output/`
- **Audit logs** in `logs/audit.jsonl`
- A **booking confirmation** and **reminder** entries simulated
- A **summary CSV** in `logs/session_summary.csv`

---

## Project Structure

```
PathFinderAI/
  ├── LICENSE
  ├── README.md
  ├── requirements.txt  # stdlib runtime
  ├── src/pathfinder/
  │   ├── __init__.py
  │   ├── agent.py            # Agent loop (planner + tools + policies + audit)
  │   ├── planner.py          # Simple goal decomposition and step graph
  │   ├── tools.py            # Booking, transport, reminders, translation (simulated)
  │   ├── channels.py         # Console channel; interface for SMS/voice adapters
  │   ├── policies.py         # Consent, RBAC, red-flag triggers, PII minimiser
  │   ├── catalog.py          # Service catalog loader/search (JSON schema)
  │   ├── storage.py          # Profiles, preferences, state persistence
  │   ├── simulation.py       # Deterministic seeds & fake data generation
  │   └── utils.py            # Small helpers
  ├── config/
  │   ├── service_catalog.json
  │   └── prompts.yml
  ├── data/
  │   ├── sample_profiles.json
  │   └── sample_events.json
  ├── examples/
  │   ├── demo_senior_console.py
  │   └── output/             # generated transcripts
  ├── tests/
  │   └── test_planner.py
  ├── docs/
  │   ├── PathFinder_Slides.pptx
  │   ├── Presentation_Script.md
  │   ├── Workflow_Evidence.md
  │   ├── Executive_Summary.pdf
  │   ├── Architecture.png
  │   ├── Workflow.png
  │   └── charts/
  │       ├── Outcomes.png
  │       ├── Handoff.png
  │       └── Duration.png
  ├── logs/
  │   ├── audit.jsonl
  │   └── session_summary.csv
  └── PathFinderAI.zip         # bundle of everything
```

---

## Ethical, Privacy & Governance (Australia-aligned)

- **Just-in-time consent** and plain-language explanations are embedded in the agent loop.
- **PII minimisation** and **purpose limitation**: data used only to execute the requested task.
- **Audit logs** (JSONL) and **summary CSV** to support assurance.
- **Red-flag triggers** (e.g., distress) escalate to human responders.

See `docs/Workflow_Evidence.md` for the full DPIA-lite, RACI, and rollout plan.

---

## Extending to Your Council/NGO

- Add services to `config/service_catalog.json` with your events, form fields, and eligibility rules.
- Replace the console channel with an SMS/voice adapter (keep the same `Channel` interface).
- Keep consent text, audit, and red-flag policies intact.

---

## License

MIT — see `LICENSE`.

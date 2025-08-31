
# PathFinder AI — Workflow & Evidence (Ordered, with Rationale)

 2025-08-31T12:49:51.962875

## Phases (Why this order)
1. **Discovery & Safeguards** — stakeholder mapping, DPIA-lite, risk register, red-flag taxonomy.  
   *Why:* prevents harm, clarifies constraints, reduces rework.
2. **Service Mapping & Data Contracts** — top services by demand; API/data sharing agreements; consent copy.  
   *Why:* stable interfaces for safe automation.
3. **MVP (Voice/SMS first)** — low literacy prompts, multilingual intents, accessibility & escalation flows.  
   *Why:* meet digitally excluded users where they are.
4. **Agentic Core Build** — planner, tools, policy guard, audit schema; unit tests for plan graph.  
   *Why:* modular autonomy with guardrails.
5. **Pilot Integrations** — food security alternative, social events, transport; sandbox testing.  
   *Why:* thin slices validate value with low risk.
6. **Safety & Equity Evaluation** — load tests, bias probes, a11y audits, cohort KPIs.  
   *Why:* evidence before scale.
7. **Pilot Launch & Monitoring** — limited suburbs, call-centre training, telemetry dashboards, weekly governance.  
   *Why:* iterate in production with oversight.
8. **Scale & Open APIs** — expand services & councils; publish open spec; federate catalogs.  
   *Why:* interoperability and transparency.

## RACI (Excerpt)
- **Accountable:** Council CIO (data governance), NGO Lead (service quality)  
- **Responsible:** AI Lead, Integrations Lead, Research Lead  
- **Consulted:** Privacy Officer, Accessibility Advisor, Community Board  
- **Informed:** Elected officials, partner NGOs, hotline leads

## Evidence Artefacts (This repo)
- `docs/Architecture.png` and `docs/Workflow.png` — diagrams (high DPI)  
- `docs/PathFinder_Slides.pptx` + `docs/Presentation_Script.md` — presentation with narrative  
- `logs/audit.jsonl`, `logs/session_summary.csv` — audit & summary outputs from demo  
- `docs/charts/` — outcome charts based on simulated sessions  
- `LICENSE`, `README.md`, `requirements.txt` — repository hygiene

## Change Log
- 2025-08-31T12:49:51.962893: Initial repository generation with runnable demo, docs, and diagrams.

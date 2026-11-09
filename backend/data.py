USE_CASES = [
    {"id": 1, "name": "Medical imaging assistance", "area": "Radiology", "benefit": "Supports image-review workflow", "readiness": "Medium"},
    {"id": 2, "name": "Appointment no-show prediction", "area": "Operations", "benefit": "Helps improve scheduling", "readiness": "High"},
    {"id": 3, "name": "Hospital resource forecasting", "area": "Administration", "benefit": "Supports capacity planning", "readiness": "Medium"},
    {"id": 4, "name": "Patient query assistant", "area": "Patient services", "benefit": "Helps route common enquiries", "readiness": "Low"},
]

RISKS = [
    {"risk": "Data privacy and security", "likelihood": "High", "impact": "High", "mitigation": "Use access controls, encryption, and approved data governance."},
    {"risk": "Biased or unrepresentative data", "likelihood": "Medium", "impact": "High", "mitigation": "Evaluate performance across relevant groups and document limitations."},
    {"risk": "Workflow disruption", "likelihood": "Medium", "impact": "Medium", "mitigation": "Pilot with staff feedback and provide training."},
    {"risk": "Insufficient model transparency", "likelihood": "Medium", "impact": "High", "mitigation": "Require explainability, human review, and audit trails."},
]

ROADMAP = [
    {"phase": "1. Discover", "duration": "Weeks 1–2", "tasks": "Identify needs, stakeholders, and suitable use cases."},
    {"phase": "2. Assess", "duration": "Weeks 3–4", "tasks": "Review data readiness, risks, costs, and governance."},
    {"phase": "3. Pilot", "duration": "Weeks 5–8", "tasks": "Run a limited pilot with human oversight and feedback."},
    {"phase": "4. Evaluate", "duration": "Weeks 9–10", "tasks": "Measure outcomes, safety, usability, and operational impact."},
    {"phase": "5. Scale", "duration": "After evaluation", "tasks": "Expand only after approvals, validation, and monitoring plans."},
]

KPIS = [
    {"name": "Use cases identified", "value": "4", "note": "Illustrative sample"},
    {"name": "Risks documented", "value": "4", "note": "Illustrative sample"},
    {"name": "Roadmap phases", "value": "5", "note": "Planning framework"},
    {"name": "Readiness status", "value": "In assessment", "note": "Not a clinical readiness score"},
]

SWOT = {
    "strengths": ["Potential to improve operational efficiency", "Can support evidence-informed planning"],
    "weaknesses": ["Requires reliable, representative data", "Needs staff training and ongoing maintenance"],
    "opportunities": ["Workflow automation", "Better resource planning"],
    "threats": ["Privacy and cybersecurity risks", "Bias, regulation, and lack of trust"],
}

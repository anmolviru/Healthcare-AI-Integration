"""Demonstration data for the Healthcare AI dashboard."""

USE_CASES = [
    {
        "id": 1,
        "name": "Medical Image Analysis",
        "department": "Radiology",
        "description": "AI-assisted review of medical images.",
        "status": "Proposed",
        "priority": "High",
    },
    {
        "id": 2,
        "name": "Appointment Scheduling",
        "department": "Administration",
        "description": "AI-assisted appointment planning.",
        "status": "Proposed",
        "priority": "Medium",
    },
    {
        "id": 3,
        "name": "Patient Readmission Risk",
        "department": "Patient Care",
        "description": "Proposed analysis of readmission risk.",
        "status": "Proposed",
        "priority": "High",
    },
]

RISKS = [
    {
        "id": 1,
        "title": "Patient Data Privacy",
        "category": "Privacy",
        "severity": "High",
        "status": "Open",
    },
    {
        "id": 2,
        "title": "Model Bias",
        "category": "Ethics",
        "severity": "High",
        "status": "Open",
    },
    {
        "id": 3,
        "title": "Staff Training",
        "category": "Operational",
        "severity": "Medium",
        "status": "In Progress",
    },
]

ROADMAP = [
    {
        "phase": "Short Term",
        "activities": [
            "Identify healthcare AI opportunities",
            "Assess organizational readiness",
            "Review privacy and ethical risks",
        ],
    },
    {
        "phase": "Long Term",
        "activities": [
            "Evaluate suitable AI solutions",
            "Conduct clinical validation",
            "Plan responsible deployment",
        ],
    },
]

SWOT = {
    "strengths": ["Growing AI capabilities", "Potential workflow support"],
    "weaknesses": ["Limited technical readiness", "Training requirements"],
    "opportunities": ["Administrative automation", "Research support"],
    "threats": ["Privacy risks", "Algorithmic bias"],
}

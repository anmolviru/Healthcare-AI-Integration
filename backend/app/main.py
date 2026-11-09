
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from .data import USE_CASES, RISKS, ROADMAP, SWOT, KPIS

app = FastAPI(
    title="Healthcare AI Strategy API",
    version="1.0.0",
    description="Educational planning API; not a clinical decision-support service."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class UseCaseIn(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    category: str
    description: str = Field(min_length=5, max_length=300)
    value: int = Field(ge=1, le=5)
    readiness: int = Field(ge=1, le=5)
    fit: int = Field(ge=1, le=5)
    risk: int = Field(ge=1, le=5)
    owner: str

class StatusIn(BaseModel):
    status: Literal["Open", "In progress", "Mitigated", "Closed"]

def score(x):
    benefit = (x["value"] + x["readiness"] + x["fit"]) / 3
    return round(max(0, min(100, (benefit - x["risk"] * 0.35) / 5 * 100)), 1)

@app.get("/")
def root():
    return {
        "service": "Healthcare AI Strategy API",
        "notice": "Fictional planning demo only."
    }

@app.get("/api/health")
def health():
    return {"status": "ok", "clinical_ai": False}

@app.get("/api/summary")
def summary():
    return {
        "use_case_count": len(USE_CASES),
        "risk_count": len(RISKS),
        "open_risks": sum(r["status"] == "Open" for r in RISKS),
        "roadmap_phases": len(ROADMAP),
        "clinical_models_implemented": 0
    }

@app.get("/api/use-cases")
def use_cases():
    return [{**x, "priority_score": score(x)} for x in USE_CASES]

@app.post("/api/use-cases", status_code=201)
def add_use_case(payload: UseCaseIn):
    item = {
        "id": max([x["id"] for x in USE_CASES], default=0) + 1,
        **payload.model_dump(),
        "status": "Proposed"
    }
    USE_CASES.append(item)
    return {**item, "priority_score": score(item)}

@app.get("/api/risks")
def risks():
    return [{**r, "score": r["likelihood"] * r["impact"]} for r in RISKS]

@app.patch("/api/risks/{risk_id}")
def update_risk(risk_id: str, payload: StatusIn):
    for r in RISKS:
        if r["id"] == risk_id:
            r["status"] = payload.status
            return r
    raise HTTPException(404, "Risk not found")

@app.get("/api/roadmap")
def roadmap():
    return ROADMAP

@app.get("/api/swot")
def swot():
    return SWOT

@app.get("/api/kpis")
def kpis():
    return KPIS

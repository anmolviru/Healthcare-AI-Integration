from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import USE_CASES, RISKS, ROADMAP, KPIS, SWOT

app = FastAPI(title="Healthcare AI Integration API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Healthcare AI Integration API is running"}

@app.get("/api/overview")
def overview():
    return {
        "use_cases": USE_CASES,
        "risks": RISKS,
        "roadmap": ROADMAP,
        "kpis": KPIS,
        "swot": SWOT,
    }

@app.get("/api/health")
def health():
    return {"status": "ok"}

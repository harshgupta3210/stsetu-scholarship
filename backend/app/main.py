from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="STSetu Unified Scholarship API",
    version="1.0-demo"
)


class EligibilityRequest(BaseModel):
    category: str = "ST"
    education_level: str = "MCA"
    annual_income: float = 210000


@app.get("/")
def root():
    return {
        "message": "STSetu Unified Scholarship API is running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "mode": "SIH demo",
        "platform": "STSetu"
    }


@app.get("/api/scholarships")
def scholarships():
    return {
        "schemes": [
            "Pre-Matric Scholarship",
            "Post-Matric Scholarship",
            "Top Class Education",
            "National Fellowship for ST",
            "National Overseas Scholarship"
        ]
    }


@app.post("/api/eligibility")
def eligibility(req: EligibilityRequest):
    return {
        "eligible": req.category.upper() == "ST",
        "scheme": "Post-Matric Scholarship",
        "mode": "demo"
    }


@app.get("/api/applications")
def applications():
    return {
        "applications": [
            {
                "id": "ST-2026-10482",
                "status": "Under Verification",
                "verification": "Document Verified"
            }
        ]
    }


@app.get("/api/payments")
def payments():
    return {
        "dbt_status": "Processing",
        "amount": "48000",
        "account": "XXXX XXXX 4821"
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from backend.core.recommender import recommend_assessments

app = FastAPI(
    title="SHL Assessment Recommendation API",
    version="1.0.0"
)

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- MODELS ----------
class RecommendationRequest(BaseModel):
    query: str
    k: int = 10


class AssessmentResponse(BaseModel):
    name: str
    url: str
    description: str
    duration: Optional[int]
    remote_support: str
    adaptive_support: str
    test_type: List[str]


# ---------- ROUTES ----------
@app.get("/")
def root():
    return {"message": "SHL Recommendation API is running"}


@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/recommend", response_model=List[AssessmentResponse])
def recommend(request: RecommendationRequest):
    results = recommend_assessments(
        query=request.query,
        top_k=request.k
    )
    return results

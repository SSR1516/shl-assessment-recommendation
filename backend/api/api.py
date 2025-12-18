from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from backend.core.recommender import recommend_assessments

# ================= APP INIT =================
app = FastAPI(
    title="SHL Assessment Recommendation API",
    description="API to recommend SHL assessments based on hiring requirements",
    version="1.0.0"
)

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow Streamlit, browser, Render
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= REQUEST MODEL =================
class RecommendationRequest(BaseModel):
    query: str
    k: int = 10


# ================= RESPONSE MODEL =================
class AssessmentResponse(BaseModel):
    name: str
    url: str
    description: str
    duration: int | None
    remote_support: str
    adaptive_support: str
    test_type: List[str]


# ================= HEALTH CHECK =================
@app.get("/")
def root():
    return {"status": "SHL Recommendation API is running"}


@app.get("/health")
def health():
    return {"status": "OK"}


# ================= RECOMMEND ENDPOINT =================
@app.post("/recommend", response_model=List[AssessmentResponse])
def recommend(request: RecommendationRequest):
    """
    Takes a hiring requirement (query) and returns top-k recommended SHL assessments
    """
    recommendations = recommend_assessments(
        query=request.query,
        top_k=request.k
    )
    return recommendations

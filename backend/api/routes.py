from fastapi import APIRouter
from backend.models.schema import (
    RecommendationRequest,
    RecommendationResponse
)
from backend.core.recommender import recommend_assessments

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "healthy"}

@router.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    results = recommend_assessments(request.query)
    return {"recommended_assessments": results}

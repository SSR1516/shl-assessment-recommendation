from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.recommender import recommend_assessments

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    k: int = 10

@router.post("/recommend")
def recommend(req: QueryRequest):
    results = recommend_assessments(req.query, req.k)
    return results

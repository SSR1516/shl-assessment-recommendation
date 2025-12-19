from fastapi import FastAPI
from pydantic import BaseModel
from backend.core.recommender import recommend_assessments

app = FastAPI()


class RecommendRequest(BaseModel):
    query: str
    k: int = 10


@app.get("/")
def root():
    return {"message": "SHL Assessment Recommendation API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/recommend")
def recommend(req: RecommendRequest):
    return recommend_assessments(
        query=req.query,
        top_k=req.k
    )

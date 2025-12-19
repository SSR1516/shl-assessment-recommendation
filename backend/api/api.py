from fastapi import FastAPI
from pydantic import BaseModel
<<<<<<< HEAD
from backend.core.recommender import recommend_assessments

app = FastAPI()


class RecommendRequest(BaseModel):
=======
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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9
    query: str
    k: int = 10


<<<<<<< HEAD
@app.get("/")
def root():
    return {"message": "API running"}
=======
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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9


@app.get("/health")
def health():
    return {"status": "ok"}


<<<<<<< HEAD
@app.post("/recommend")
def recommend(req: RecommendRequest):
    return recommend_assessments(
        query=req.query,
        top_k=req.k
    )
=======
@app.post("/recommend", response_model=List[AssessmentResponse])
def recommend(request: RecommendationRequest):
    results = recommend_assessments(
        query=request.query,
        top_k=request.k
    )
    return results
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

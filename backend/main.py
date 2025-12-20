from fastapi import FastAPI
import pandas as pd
from backend.core.embeddings import embed_texts
from backend.core.recommender import recommend

app = FastAPI()

df = pd.read_csv("data/processed/shl_assessments.csv")
texts = (df["name"] + " " + df["description"]).tolist()
embs = embed_texts(texts)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend_api(q: dict):
    q_emb = embed_texts([q["query"]])[0]
    res = recommend(q_emb, embs, df.to_dict("records"))
    return {"results": [r[0] for r in res]}

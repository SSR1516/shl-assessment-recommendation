# SHL Assessment Recommendation System

End-to-end system to recommend SHL assessments using NLP embeddings.

## Features
- SentenceTransformer embeddings
- Recall@10 evaluation
- FastAPI backend
- Streamlit frontend

## Run
```bash
pip install -r requirements.txt
python experiments/generate_predictions.py
python experiments/evaluate.py
uvicorn backend.main:app --reload

---

# 📂 docs

## 📄 `docs/approach.md`
```md
## Approach

We use semantic embeddings (Sentence Transformers) to match job descriptions
with SHL assessments. Recommendations are balanced between
Knowledge (K) and Personality (P) tests.

Evaluation is done using Recall@10 on SHL-provided test data.

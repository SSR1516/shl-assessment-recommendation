import pandas as pd
import os
import re

DATA_PATH = "data/processed/shl_assessments.csv"

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def recommend_assessments(query: str, top_k: int = 10):
    # ---------- SAFETY ----------
    if not query or not isinstance(query, str):
        return []

    if not os.path.exists(DATA_PATH):
        print("❌ CSV not found:", DATA_PATH)
        return []

    try:
        df = pd.read_csv(DATA_PATH, encoding="utf-8", errors="ignore")
    except Exception as e:
        print("❌ CSV load error:", e)
        return []

    if df.empty:
        print("❌ CSV empty")
        return []

    # ---------- PREPROCESS ----------
    df = df.copy()
    df["combined"] = (
        df["name"].fillna("") + " " + df["description"].fillna("")
    ).apply(clean_text)

    query_clean = clean_text(query)
    query_tokens = set(query_clean.split())

    # ---------- SCORING ----------
    scores = []
    for _, row in df.iterrows():
        text_tokens = set(row["combined"].split())
        score = len(query_tokens.intersection(text_tokens))
        scores.append(score)

    df["score"] = scores
    df = df[df["score"] > 0]

    if df.empty:
        return []

    df = df.sort_values("score", ascending=False).head(top_k)

    # ---------- RESPONSE ----------
    results = []
    for _, row in df.iterrows():
        results.append({
            "name": row.get("name", ""),
            "url": row.get("url", ""),
            "description": row.get("description", ""),
            "duration": int(row["duration"]) if str(row.get("duration")).isdigit() else None,
            "remote_support": str(row.get("remote_support", "Unknown")),
            "adaptive_support": str(row.get("adaptive_support", "Unknown")),
            "test_type": (
                row.get("test_type").split(",")
                if isinstance(row.get("test_type"), str)
                else []
            )
        })

    return results

import pandas as pd
import re

DATA_PATH = "data/processed/shl_assessments.csv"

TEST_TYPE_MAP = {
    "K": "Knowledge & Skills",
    "P": "Personality & Behavior",
    "A": "Ability & Aptitude",
    "S": "Simulation",
    "B": "Behavioral",
    "C": "Competency",
    "D": "Development",
    "E": "Exercise"
}


def normalize_test_type(test_list):
    return [TEST_TYPE_MAP[c] for c in test_list if c in TEST_TYPE_MAP]


def recommend_assessments(query: str, top_k: int = 10):
    df = pd.read_csv(DATA_PATH)

    # Clean data
    df["description"] = df["description"].fillna("")
    df["test_type"] = df["test_type"].fillna("[]")

    # Tokenize query
    tokens = re.findall(r"\w+", query.lower())
    tokens = [t for t in tokens if len(t) > 2]

    # Simple scoring
    def score_row(row):
        text = f"{row['name']} {row['description']}".lower()
        return sum(1 for t in tokens if t in text)

    df["score"] = df.apply(score_row, axis=1)

    # Sort
    df = df.sort_values("score", ascending=False)

    # 🚨 GUARANTEED FALLBACK
    results = df.head(top_k).to_dict("records")

    recs = []
    for r in results:
        try:
            raw = eval(r["test_type"]) if isinstance(r["test_type"], str) else r["test_type"]
        except:
            raw = []

        recs.append({
            "name": r["name"],
            "url": r["url"],
            "description": r["description"],
            "duration": None if pd.isna(r["duration"]) else int(float(r["duration"])),
            "remote_support": r.get("remote_support", "Yes"),
            "adaptive_support": r.get("adaptive_support", "No"),
            "test_type": normalize_test_type(raw)
        })

    return recs

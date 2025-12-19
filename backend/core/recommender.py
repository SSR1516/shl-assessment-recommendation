import pandas as pd
import re
import ast

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
    # ✅ SAFE CSV LOAD (pandas 2.x compatible)
    df = pd.read_csv(DATA_PATH, encoding="latin1", engine="python")

    # ✅ Clean columns (NO crashes)
    df["description"] = df["description"].fillna("")
    df["test_type"] = df["test_type"].fillna("[]")

    # ✅ Tokenize query safely
    tokens = re.findall(r"\w+", query.lower())
    tokens = [t for t in tokens if len(t) > 2]

    # ✅ Keyword scoring
    def score_row(row):
        text = f"{row['name']} {row['description']}".lower()
        return sum(1 for t in tokens if t in text)

    df["score"] = df.apply(score_row, axis=1)

    # ✅ Sort by relevance
    df = df.sort_values("score", ascending=False)

    # 🚨 HARD FALLBACK (even if query = "asdfgh")
    if df["score"].max() == 0:
        df["score"] = 1

    results = df.head(top_k).to_dict("records")

    # ✅ Final API-safe response
    recs = []
    for r in results:
        try:
            raw = ast.literal_eval(r["test_type"]) if isinstance(r["test_type"], str) else r["test_type"]
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

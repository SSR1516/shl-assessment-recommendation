import pandas as pd
import os
import re

DATA_PATH = "data/processed/shl_assessments.csv"
<<<<<<< HEAD

# Mapping from code to full label (PDF compliant)
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
    normalized = []
    for code in test_list:
        if code in TEST_TYPE_MAP:
            normalized.append(TEST_TYPE_MAP[code])
    return normalized


def keyword_score(row, query_words):
    text = f"{row['name']} {row['description']}".lower()
    score = 0
    for w in query_words:
        if w in text:
            score += 1
    return score


def detect_domains(query):
    tech_keywords = [
        "java", "python", "developer", "software", "cloud", "sql", "engineering",
        "data", "programming", "coding", "backend", "frontend", "devops"
    ]
    soft_keywords = [
        "communication", "teamwork", "leadership", "collaboration",
        "problem solving", "adaptability", "motivation"
    ]

    q = query.lower()
    return {
        "tech": any(kw in q for kw in tech_keywords),
        "soft": any(kw in q for kw in soft_keywords)
    }
=======

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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

    try:
        df = pd.read_csv(DATA_PATH, encoding="utf-8", errors="ignore")
    except Exception as e:
        print("❌ CSV load error:", e)
        return []

<<<<<<< HEAD
def recommend_assessments(query: str, top_k: int = 10):
    df = pd.read_csv(DATA_PATH)

    # Clean NaNs
    df["description"] = df["description"].fillna("")
    df["test_type"] = df["test_type"].fillna("[]")

    # Tokenize query
    tokens = re.findall(r"\w+", query.lower())
    query_words = [t for t in tokens if len(t) > 2]

    domains = detect_domains(query)

    # Scoring
    df["score"] = df.apply(lambda r: keyword_score(r, query_words), axis=1)

    df_sorted = df.sort_values("score", ascending=False).reset_index(drop=True)

    # If nothing matched → soft fallback
    if df_sorted["score"].max() == 0:
        df_sorted["score"] = 1
=======
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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

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

<<<<<<< HEAD
    # Mixed domain logic
    if domains["tech"] and domains["soft"]:
        tech_df = df_sorted[df_sorted["test_type"].str.contains("K")]
        soft_df = df_sorted[df_sorted["test_type"].str.contains("P")]

        n_each = max(1, top_k // 3)

        picks = []
        picks.extend(tech_df.head(n_each).to_dict("records"))
        picks.extend(soft_df.head(n_each).to_dict("records"))

        seen = {p["url"] for p in picks}

        for _, r in df_sorted.iterrows():
            if len(picks) >= top_k:
                break
            if r["url"] not in seen:
                picks.append(r.to_dict())
                seen.add(r["url"])

        results = picks
    else:
        results = df_sorted.head(top_k).to_dict("records")

    # FINAL GUARANTEED FALLBACK (CRITICAL)
    if len(results) == 0:
        results = df.head(top_k).to_dict("records")

    # Format output
    recs = []
    for r in results:
        try:
            raw_list = eval(r["test_type"]) if isinstance(r["test_type"], str) else r["test_type"]
        except:
            raw_list = []

        recs.append({
            "name": r["name"],
            "url": r["url"],
            "description": r["description"],
            "duration": None if pd.isna(r["duration"]) else int(float(r["duration"])),
            "remote_support": r["remote_support"],
            "adaptive_support": r["adaptive_support"],
            "test_type": normalize_test_type(raw_list)
        })

    return recs
=======
    return results
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

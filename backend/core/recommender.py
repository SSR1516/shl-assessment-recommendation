import pandas as pd
import re

# ---------- helpers ----------

def keyword_score(row, query_words):
    text = f"{row['name']} {row.get('description','')}".lower()
    return sum(1 for w in query_words if w in text)


def detect_domains(query):
    tech_keywords = [
        "java", "python", "developer", "software", "cloud", "sql",
        "engineering", "programming", "coding", "devops"
    ]
    soft_keywords = [
        "collaboration", "teamwork", "communication",
        "leadership", "adaptability", "motivation"
    ]

    q = query.lower()
    return {
        "tech": any(k in q for k in tech_keywords),
        "soft": any(k in q for k in soft_keywords)
    }


# ---------- MAIN FUNCTION (DO NOT CHANGE SIGNATURE) ----------

def recommend_assessments(query: str, df: pd.DataFrame, k: int = 10):
    """
    API compliant recommender
    Returns:
    [
      {"name": "...", "url": "..."},
      ...
    ]
    """

    tokens = re.findall(r"\w+", query.lower())
    query_words = [t for t in tokens if len(t) > 2]

    domains = detect_domains(query)

    df = df.copy()
    df["score"] = df.apply(lambda r: keyword_score(r, query_words), axis=1)

    df = df.sort_values("score", ascending=False).reset_index(drop=True)

    if df["score"].max() == 0:
        df["score"] = 1  # fallback

    results = []

    if domains["tech"] and domains["soft"]:
        tech_df = df[df["test_type"].str.contains("K", na=False)]
        soft_df = df[df["test_type"].str.contains("P", na=False)]

        n_each = max(1, k // 3)

        picks = (
            tech_df.head(n_each).to_dict("records") +
            soft_df.head(n_each).to_dict("records")
        )

        seen = set(p["url"] for p in picks)

        for _, r in df.iterrows():
            if len(picks) >= k:
                break
            if r["url"] not in seen:
                picks.append(r.to_dict())
                seen.add(r["url"])

        results = picks

    else:
        results = df.head(k).to_dict("records")

    # -------- API OUTPUT (STRICT) --------
    return [
        {"name": r["name"], "url": r["url"]}
        for r in results[:k]
    ]

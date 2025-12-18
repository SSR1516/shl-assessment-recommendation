import pandas as pd
from backend.core.recommender import recommend_assessments, normalize_url

TRAIN_PATH = "data/evaluation/train.csv"
K = 10


def main():
    df = pd.read_csv(TRAIN_PATH, encoding="latin1", engine="python")

    hits = 0
    total = len(df)

    for _, row in df.iterrows():
        query = row["Query"]                     # ✅ FIXED case
        gt_url = normalize_url(row["Assessment_url"])

        recommendations = recommend_assessments(query, top_k=K)
        rec_urls = [normalize_url(r["url"]) for r in recommendations]

        if gt_url in rec_urls:
            hits += 1

    recall = hits / total if total else 0
    print(f"✅ Mean Recall@{K}: {recall:.4f}")


if __name__ == "__main__":
    main()

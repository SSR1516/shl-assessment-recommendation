import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))

from backend.core.recommender import recommend_assessments

TEST_PATH = "data/evaluation/test.csv"
OUTPUT_PATH = "data/evaluation/submission.csv"
TOP_K = 10

def main():
    df = pd.read_csv(
        TEST_PATH,
        encoding="latin1",
        engine="python"
    )

    rows = []

    for _, row in df.iterrows():
        query = row["Query"]
        recs = recommend_assessments(query, top_k=TOP_K)

        for r in recs:
            rows.append({
                "Query": query,
                "Assessment_url": r["url"]
            })

    out_df = pd.DataFrame(rows)
    out_df.to_csv(OUTPUT_PATH, index=False)
    print(f"📁 Submission generated → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

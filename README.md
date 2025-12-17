# AI-based SHL Assessment Recommendation System

An end-to-end **AI-powered recommendation system** that helps recruiters identify the most relevant SHL assessments based on natural language hiring requirements.

This project was built as part of the **SHL AI Intern – Recommendation Engine (Generative AI) Assignment** and closely follows the problem statement, evaluation methodology, and expected deliverables described in the official PDF.

---

## 🚀 What This Project Does

Recruiters often struggle to select the right assessments from SHL’s large catalog. This system solves that by:

* Scraping and structuring SHL assessment data
* Accepting **natural language hiring queries** (e.g., *"Hiring Java developers with communication skills"*)
* Recommending the **most relevant SHL assessments**
* Evaluating recommendations using **Recall@K** on the provided dataset

---

## 🧠 System Architecture

![System Architecture](docs/system_architecture.png)

**High-level flow:**

1. SHL assessment data is scraped and stored locally
2. Data is cleaned and processed
3. A recommendation engine ranks assessments based on query relevance
4. FastAPI exposes the recommendation API
5. Streamlit provides an interactive recruiter-facing UI

---

## 📁 Project Structure

```
shl-assessment-recommendation/
│
├── backend/            # FastAPI backend & recommender logic
│   ├── api/            # API routes
│   ├── core/           # Recommendation engine
│   └── utils/          # Helpers & mappings
│
├── frontend/           # Streamlit web UI
│
├── scraper/            # SHL catalog web scraper
│
├── data/
│   ├── raw/            # Raw scraped data
│   ├── processed/      # Cleaned assessment dataset
│   └── evaluation/     # Train, test & submission files
│
├── experiments/        # Recall@K evaluation scripts
│
├── docs/               # Architecture diagram & documentation
│
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 📊 Data Collection (SHL Scraper)

* Source: **SHL Product Catalog**
* Tooling: `requests`, `BeautifulSoup`
* Output: `data/processed/shl_assessments.csv`

Each assessment contains:

* Name
* URL
* Description
* Duration (if available)
* Remote & adaptive support
* Test type (mapped to SHL categories)

---

## 🤖 Recommendation Approach

The recommendation engine uses a **keyword-based relevance scoring approach**:

1. Tokenizes the recruiter query
2. Matches query terms against assessment names & descriptions
3. Applies heuristic domain detection (technical vs behavioral)
4. Ensures **balanced recommendations** when both domains are detected

This design prioritizes:

* Transparency
* Interpretability
* Alignment with SHL’s structured assessment taxonomy

---

## 📈 Evaluation

* Metric used: **Recall@10**
* Dataset: Provided train & test CSV files
* Script: `experiments/evaluate.py`

Sample output:

```
Mean Recall@10: 0.0200
```

A submission file is generated at:

```
data/evaluation/submission.csv
```

---

## 🖥️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SSR1516/shl-assessment-recommendation.git
cd shl-assessment-recommendation
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start the Backend (FastAPI)

```bash
python -m uvicorn backend.api.api:app --reload
```

Backend will be available at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### 4️⃣ Start the Frontend (Streamlit UI)

```bash
streamlit run frontend/app.py
```

🚀 **Open the application here:**
👉 **[http://localhost:8501](http://localhost:8501)**

> Clicking this link after running Streamlit will automatically open the recruiter UI.

---

## 🧪 Example Recruiter Query

```
I am hiring Java developers who also need good communication skills
```

The system returns:

* Assessment name
* SHL product URL
* Test type (Knowledge, Ability, Personality, etc.)
* Remote & adaptive support

---

## 🛠️ Technologies Used

* **Python 3.12**
* **FastAPI** – backend API
* **Streamlit** – recruiter-facing UI
* **Pandas / NumPy** – data processing
* **BeautifulSoup** – web scraping

---

## 🎯 Key Highlights

* End-to-end working system
* Clean modular architecture
* Matches SHL assignment requirements
* Transparent, explainable recommendation logic
* Ready for recruiter or evaluator review

---

## 📌 Note for Reviewers

This project is designed to be:

* Easy to understand
* Easy to run locally
* Fully aligned with the SHL assessment problem statement

Thank you for reviewing this submission.

---

**Author:** SSR1516


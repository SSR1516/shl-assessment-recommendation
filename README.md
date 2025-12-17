# AI-based SHL Assessment Recommendation System 🚀

An end-to-end **AI-powered recommendation system** that helps recruiters identify the most relevant SHL assessments based on natural language hiring requirements.

This project was built as part of the **SHL AI Intern – Recommendation Engine (Generative AI) Assignment** and strictly follows the problem statement, evaluation methodology, and deliverables mentioned in the official SHL PDF.

---

## 🌐 Live Demo

- 🚀 **Streamlit Application (Recruiter UI)**  
  https://shl-assessment.streamlit.app

- ⚙️ **FastAPI Backend (Swagger Docs)**  
  https://shl-backend.onrender.com/docs

> Recruiters can directly open the app, enter a hiring query, and view recommended SHL assessments without any local setup.

---

## 🚀 What This Project Does

Recruiters often struggle to choose the correct assessments from SHL’s large catalog.  
This system solves that problem by:

- Scraping and structuring SHL assessment data
- Accepting **natural language hiring queries**
- Recommending the **most relevant SHL assessments**
- Evaluating results using **Recall@K**

Example query:
Hiring Java developers with strong communication skills

yaml
Copy code

---

## 🧠 System Architecture

![System Architecture](docs/system_architecture.png)

### High-Level Flow
1. SHL catalog is scraped and structured
2. Data is cleaned and stored locally
3. Recruiter submits a natural language query
4. Recommendation engine ranks assessments
5. FastAPI returns ranked results
6. Streamlit UI displays recommendations

The system is intentionally divided into **three clean layers**:
- Frontend (Streamlit)
- Backend (FastAPI)
- Data & Evaluation Layer

---

## 📁 Project Structure

```text
shl-assessment-recommendation/
│
├── backend/
│   ├── api/            # FastAPI routes
│   ├── core/           # Recommendation engine
│   └── utils/          # Helpers & mappings
│
├── frontend/           # Streamlit recruiter UI
│
├── scraper/            # SHL catalog web scraper
│
├── data/
│   ├── raw/            # Raw scraped data
│   ├── processed/      # Cleaned SHL assessments
│   └── evaluation/     # Train, test & submission files
│
├── experiments/        # Recall@K evaluation scripts
│
├── docs/               # Architecture diagrams
│
├── requirements.txt
└── README.md
📊 Data Collection (SHL Scraper)
Source: SHL Product Catalog

Tools: requests, BeautifulSoup

Output: data/processed/shl_assessments.csv

Each assessment contains:

Name

URL

Description

Duration (if available)

Remote & adaptive support

Test type (mapped to SHL categories)

Total assessments scraped: 377

🤖 Recommendation Approach
The recommendation engine uses a transparent, heuristic-based ranking strategy:

Tokenizes the recruiter query

Matches query keywords with assessment name & description

Detects technical vs behavioral intent

Ensures balanced recommendations when both domains are present

Why this approach?
Fully explainable

Lightweight & fast

Aligns with SHL’s structured taxonomy

Easy to evaluate and reproduce

📈 Evaluation
Metric: Mean Recall@10

Dataset: SHL-provided train & test CSV files

Script: experiments/evaluate.py

Sample output:

graphql
Copy code
Mean Recall@10: 0.0200
Submission file generated at:

bash
Copy code
data/evaluation/submission.csv
🖥️ Run the Project Locally
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/SSR1516/shl-assessment-recommendation.git
cd shl-assessment-recommendation
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Start Backend (FastAPI)
bash
Copy code
python -m uvicorn backend.api.api:app --reload
Backend runs at:

cpp
Copy code
http://127.0.0.1:8000
4️⃣ Start Frontend (Streamlit)
bash
Copy code
streamlit run frontend/app.py
Frontend runs at:

arduino
Copy code
http://localhost:8501
🛠️ Tech Stack
Python 3.12

FastAPI

Streamlit

Pandas & NumPy

BeautifulSoup

Uvicorn

🎯 Key Highlights
End-to-end working system

Live deployed demo for recruiters

Clean modular architecture

Fully compliant with SHL assignment

Transparent & explainable logic

Reproducible evaluation pipeline

📌 Note for Reviewers
Live deployment is provided for easy review

Local execution is fully supported

Code is structured, documented, and assignment-aligned

👤 Author
Sejal Singh
📧 Email: sejalsingh910@gmail.com
🌐 GitHub: https://github.com/SSR1516
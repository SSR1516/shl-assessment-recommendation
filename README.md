# SHL Assessment Recommendation System

An end-to-end AI-powered system that recommends relevant SHL assessments based on recruiter hiring queries.  
This project was developed as part of the **SHL AI Intern – Recommendation Engine Assignment**.

---

## 🚀 Problem Statement

Recruiters often struggle to select the most relevant assessments from a large catalog of SHL products.  
The goal of this project is to build a **recommendation system** that maps a recruiter’s hiring requirement or job description to the **top SHL assessments** that best evaluate the required skills.

---

## 🧠 Approach

The solution follows a modular, explainable approach:

1. **Data Collection**  
   - Scraped the SHL Product Catalog to collect assessment metadata such as name, URL, duration, test type, and delivery mode.

2. **Data Processing**  
   - Cleaned and standardized assessment attributes.
   - Encoded test types (Ability, Knowledge, Personality, Simulation, etc.).

3. **Recommendation Logic**  
   - Tokenizes recruiter queries and performs keyword overlap scoring.
   - Detects technical vs behavioral intent in the query.
   - Balances technical (Knowledge/Skills) and soft-skill (Personality/Behavior) assessments when required.
   - Returns top-K ranked assessments.

4. **Backend API**  
   - Built using **FastAPI**, running on **Uvicorn**.
   - Exposes health and recommendation endpoints.

5. **Frontend UI**  
   - Built using **Streamlit** to allow recruiters to test the system interactively.

6. **Evaluation**  
   - Evaluated using **Mean Recall@10** as provided in the assignment dataset.

---

## 🏗 System Architecture

![System Architecture](docs/system_architecture.png)

**Flow Explanation:**
- Streamlit UI accepts recruiter queries.
- FastAPI backend (running on Uvicorn) processes the query.
- Backend dynamically reads the SHL assessments dataset.
- Recommendation logic ranks assessments.
- Top results are returned to the UI.

---

## 📁 Project Structure

shl-assessment-recommendation/
│
├── backend/
│ ├── api/
│ │ └── api.py
│ └── core/
│ └── recommender.py
│
├── frontend/
│ └── app.py
│
├── scraper/
│ └── scrape_shl.py
│
├── experiments/
│ ├── evaluate.py
│ └── generate_submission.py
│
├── data/
│ ├── processed/
│ │ └── shl_assessments.csv
│ └── evaluation/
│ └── submission.csv
│
├── docs/
│ └── architecture_flow_diagram.png
│
├── requirements.txt
└── README.md


---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
python -m pip install -r requirements.txt

2️⃣ Run Backend API
python -m uvicorn backend.api.api:app --reload


Backend will be available at:

http://127.0.0.1:8000


Health check:

http://127.0.0.1:8000/health

3️⃣ Run Frontend (Streamlit)

Open a new terminal window and run:

python -m streamlit run frontend/app.py


Frontend will open at:

http://localhost:8501

🔌 API Endpoints
Health Check
GET /health

Recommendation
POST /recommend


Request Body:

{
  "query": "Java developer with collaboration skills",
  "k": 10
}


Response:

{
  "recommendations": [
    {
      "name": "Java Programming (New)",
      "url": "https://www.shl.com/..."
    }
  ]
}

📊 Evaluation

The system was evaluated using the provided training dataset.

Metric used: Mean Recall@10

Result:

Mean Recall@10 ≈ 0.02

🧪 Submission Output

The final submission file is generated using:

python experiments/generate_submission.py


Output file:

data/evaluation/submission.csv

🛠 Tech Stack

Python

FastAPI

Uvicorn

Streamlit

Pandas

Requests

BeautifulSoup

✅ Key Highlights

Modular and scalable architecture

Explainable recommendation logic

Fully functional backend + frontend

Clean separation of concerns

Recruiter-friendly UI

📌 Notes

The dataset itself does not run on Uvicorn.

Uvicorn runs the FastAPI service, which dynamically loads the dataset on each request.

The architecture allows easy extension with ML or embeddings in the future.

👤 Author

Sejal Singh
GitHub: https://github.com/SSR1516
Gmail : sejalsingh910@gmail.com

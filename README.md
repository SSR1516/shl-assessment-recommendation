
How to Run
## How to Run

### Backend API
```bash
python -m pip install -r requirements.txt
python -m uvicorn backend.api.api:app --reload

Frontend
python -m streamlit run frontend/app.py

### API Endpoints
```md
## API Endpoints
- GET /health   
- POST /recommend
## 🏗 System Architecture

![System Architecture](docs/architecture_flow_diagram.png)

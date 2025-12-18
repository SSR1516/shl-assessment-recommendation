from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="SHL Assessment Recommendation API")

app.include_router(router)

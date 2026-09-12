from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import engine, Base
from routers import (
    upload,
    analyze,
    transform,
    validate,
    results,
    export
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SIH26154 Backend API",
    description="GenAI Platform for Automated Content Transformation",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(transform.router)
app.include_router(validate.router)
app.include_router(results.router)
app.include_router(export.router)

@app.get("/")
def home():
    return {
        "message": "SIH26154 Backend Running Successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
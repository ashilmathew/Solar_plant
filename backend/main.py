from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.organization import Organization
from app.api.organization import router as organization_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Solar Plant Monitoring System"
)

app.include_router(organization_router)


@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }
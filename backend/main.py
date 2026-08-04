from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import create_indexes

from app.api.auth import router as auth_router
from app.api.user import router as user_router

from app.api.organization import router as organization_router
from app.api.plant import router as plant_router
from app.api.device import router as device_router
from app.api.telemetry import router as telemetry_router
from app.api.dashboard import router as dashboard_router
from app.api.analytics import router as analytics_router
from app.api.reports import router as reports_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_indexes()
    yield


app = FastAPI(
    title="Solar Plant Monitoring System",
    lifespan=lifespan,
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication
app.include_router(auth_router)
app.include_router(user_router)

# Existing APIs
app.include_router(organization_router)
app.include_router(plant_router)
app.include_router(device_router)
app.include_router(telemetry_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(reports_router)


@app.get("/")
async def home():
    return {
        "message": "Backend Running"
    }
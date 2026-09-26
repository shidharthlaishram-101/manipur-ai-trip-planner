from fastapi import FastAPI
from pydantic import BaseModel

from services.trip_planner import TripPlanner
from database.database import create_database


app = FastAPI(
    title="Manipur AI Trip Planner API"
)


@app.on_event("startup")
def startup_event():
    create_database()


class TripRequest(BaseModel):
    budget: float
    days: int
    travelers: int
    interests: list[str]


@app.get("/")
def home():
    return {
        "message": "Manipur AI Trip Planner API is running"
    }


@app.post("/plan-trip")
def plan_trip(request: TripRequest):

    planner = TripPlanner(
        budget=request.budget,
        days=request.days,
        travelers=request.travelers,
        interests=request.interests
    )

    result = planner.plan_trip()

    return result
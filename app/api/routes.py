from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import get_weather
from app.core.logic import generate_trip_plan
# from app.config import settings

router = APIRouter()

class TripRequest(BaseModel):
    destination: str
    days: int
    interests: list[str]
    
    
@router.post("/plan-trip")
def plan_trip(request: TripRequest):
    plan = generate_trip_plan(request.destination, request.days, request.interests)
    return {"itinerary": plan}

@router.get("/weather")
async def test_weather(city: str):
    weather = await get_weather(city)
    return weather
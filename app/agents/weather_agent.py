import httpx
from app.config import settings

API_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str) -> dict:
    params = {
        "q": city,
        "appid": settings.WEATHER_API_KEY,
        "units": "metric"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "humidity": data["main"]["humidity"]
        }


from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    DEBUG = os.getenv("DEBUG", False)
    
settings = Settings()


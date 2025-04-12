import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def extract_trip_info_from_prompt(prompt: str) -> dict:
    system_prompt = (
        "You are a helpful travel planner. Extract source, destination, "
        "start date, and end date from user message. "
        "Return JSON with origin, destination, start_date, end_date (YYYY-MM-DD format)."
    )

    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()

    response = chat.send_message(f"{system_prompt}\n\nUser: {prompt}")
    text = response.text.strip()

    # ✅ Use safe eval or json.loads after validation
    return eval(text)  # You can replace with `json.loads(text)` if your LLM outputs valid JSON

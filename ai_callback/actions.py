# ai_callback/actions.py
import requests
import re

###################
# DISCLAIMER ACTIONS
###################

def add_financial_disclaimer(response):
    """
    Append a financial disclaimer to the text.
    """
    disclaimer_text = "\n\n[Disclaimer: This information is not professional financial advice. Please consult a licensed financial advisor.]"
    return response + disclaimer_text

def add_medical_disclaimer(response):
    disclaimer_text = "\n\n[Disclaimer: This information is not professional medical advice. Please consult a certified medical professional.]"
    return response + disclaimer_text

def add_legal_disclaimer(response):
    disclaimer_text = "\n\n[Disclaimer: This information is not professional legal advice. Consult a qualified attorney for legal matters.]"
    return response + disclaimer_text


###################
# MODERATION ACTIONS
###################

def redact_abusive_language(response):
    """
    Replace abusive terms with [REDACTED].
    """
    abusive_keywords = ["idiot", "stupid", "hate you", "dumb", "kill yourself" ,"hell"]
    censored_response = response
    for word in abusive_keywords:
        censored_response = censored_response.replace(word, "[REDACTED]")
    return censored_response


###################
# WEATHER ENRICHMENT
###################

def append_weather_info(response):
    """
    Detect a naive pattern "weather in X" or "climate in X", 
    call a weather API (or mock it), and append real-time info.
    """
    # Regex to capture location
    pattern = r"(?:weather|climate)\s+(?:in\s+)?([A-Z][a-z]+)"
    match = re.search(pattern, response)
    if not match:
        return response

    location = match.group(1)
    
    # Replace with a real API key for actual fetch
    OPENWEATHER_API_KEY = "<YOUR_OPENWEATHER_API_KEY>"
    
    if OPENWEATHER_API_KEY == "<YOUR_OPENWEATHER_API_KEY>":
        # If you don't have a real key, mock the data
        weather_data = f"25°C, Clear Skies (mock data for {location})"
    else:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
        )
        try:
            r = requests.get(url)
            data = r.json()
            if data.get("cod") == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                weather_data = f"{temp}°C, {desc}"
            else:
                weather_data = f"Weather data not available for {location}"
        except Exception as e:
            weather_data = f"Error fetching weather: {str(e)}"

    enriched_response = (
        f"{response}\n\n---\n"
        f"[Real-Time Weather Info for {location}]\n"
        f"{weather_data}\n---"
    )
    return enriched_response


###################
# HANDLE INCOMPLETE RESPONSES
###################

def handle_incomplete_response(response):
    """
    Append a note prompting for more detail or clarity if response is incomplete.
    """
    return response + "\n\n[Note: This response seems incomplete. Please clarify or retry the request.]"


###################
# TOXIC RESPONSE
###################

def redact_entire_text(response):
    """
    If detected as toxic, replace the entire response.
    """
    return "[REDACTED: Toxic content detected]"

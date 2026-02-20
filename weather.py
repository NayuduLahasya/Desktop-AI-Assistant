import requests

API_KEY = "e0234fde181f744c801c8d86eeae6c0e"  # Replace with your OpenWeatherMap API Key

def weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"{temp}°C, {desc.capitalize()}"
    else:
        return "Weather data not found."
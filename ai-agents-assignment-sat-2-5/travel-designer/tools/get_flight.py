# tools/get_flights.py
from agents import function_tool
from typing import TypedDict

class FlightInput(TypedDict):
    source: str
    destination: str
    date: str  # Format: YYYY-MM-DD

@function_tool
async def get_flights(input: FlightInput) -> dict:
    source = input["source"]
    destination = input["destination"]
    date = input["date"]

    # 🧪 Mock data
    flights = [
    {"airline": "AeroNova", "departure": "9:45 AM", "arrival": "12:50 PM", "price": "$340"},
    {"airline": "ZoomJet", "departure": "1:30 PM", "arrival": "4:20 PM", "price": "$295"},
    {"airline": "SkyBridge", "departure": "7:00 PM", "arrival": "10:10 PM", "price": "$325"},
    ]


    return {
        "flights": flights,
        "route": f"{source} → {destination}",
        "date": date
    }

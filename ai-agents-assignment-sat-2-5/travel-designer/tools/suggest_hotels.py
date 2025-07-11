# tools/suggest_hotels.py
from agents import function_tool
from typing import TypedDict

class HotelInput(TypedDict):
    city: str
    budget: str  # Options: "low", "medium", "high"

@function_tool
async def suggest_hotels(input: HotelInput) -> dict:
    city = input["city"]
    budget = input["budget"].lower().strip()

    # Map readable ranges for user reference
    budget_ranges = {
    "low": "$25–55 per night",
    "medium": "$65–110 per night",
    "high": "$140 and above"
}

    # 🧪 Mock hotel data
    mock_hotels = {
        "low": [
    {"name": "Metro Lodge", "price_per_night": "$42", "rating": "3.6"},
    {"name": "Nomad Nest", "price_per_night": "$38", "rating": "4.1"}
    ],
        "medium": [
    {"name": "Horizon Suites", "price_per_night": "$85", "rating": "4.3"},
    {"name": "Vista Comfort", "price_per_night": "$90", "rating": "4.4"}
    ],
        "high": [
    {"name": "The Imperial Bay", "price_per_night": "$210", "rating": "4.9"},
    {"name": "Cloud Nine Retreat", "price_per_night": "$240", "rating": "4.8"}
]
    }

    if budget not in mock_hotels:
        # Budget not recognized — prompt user to choose
        return {
            "message": (
                f"💬 Please choose a hotel budget range:\n"
                f"- `low` ({budget_ranges['low']})\n"
                f"- `medium` ({budget_ranges['medium']})\n"
                f"- `high` ({budget_ranges['high']})"
            )
        }

    return {
        "city": city,
        "budget_range": budget_ranges[budget],
        "hotels": mock_hotels[budget]
    }

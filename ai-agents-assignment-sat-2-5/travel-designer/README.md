# ✈️ Travel Companion Agent

This is a travel planning assistant made using the OpenAI Agent SDK and Chainlit. It helps users plan trips by suggesting destinations, booking mock flights, and sharing fun things to do.

## What It Does

- Asks about your mood, season, and preferred region.
- Suggests travel destinations that match your preferences.
- Books sample (mock) flights and hotels based on budget.
- Recommends food, places to visit, and fun activities.

## Agents Used

- DestinationAgent – Helps find travel destinations based on mood, interests, season, and region.
- ExploreAgent – Suggests local attractions, food, and activities in the selected place.
- BookingAgent – Handles hotel and flight bookings (mocked for this project).

## Tools Used

- `get_flights()` – Generates sample flight details.
- `suggest_hotels()` – Suggests hotels depending on the city and budget.
- `travel_info_generator()` – Matches user mood and season to good travel spots.

## Agent Flow

First, the DestinationAgent talks to the user. Then it hands off to the ExploreAgent for things to do. Finally, the BookingAgent books the mock trip.

Example:
DestinationAgent → ExploreAgent → BookingAgent

## Technologies Used

- OpenAI Agent SDK
- Chainlit (for UI)
- Python

This project is made for learning multi-agent systems and how they can help in real-life tasks like travel planning.
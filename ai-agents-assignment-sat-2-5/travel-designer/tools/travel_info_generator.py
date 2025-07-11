from typing import TypedDict
from agents import function_tool, RunContextWrapper

class TravelInfoInput(TypedDict):
    mood: str
    interests: list[str]
    season: str
    region: str

@function_tool
async def travel_info_generator(wrapper: RunContextWrapper, input: TravelInfoInput) -> dict:
    # Build the LLM prompt dynamically
    prompt = (
        f"A traveler is looking for a getaway tailored to their personality.\n"
f"Here’s what they love:\n"
f"- Current vibe: {input['mood']}\n"
f"- Hobbies or interests: {', '.join(input['interests'])}\n"
f"- Favorite travel season: {input['season']}\n"
f"- Desired region: {input['region']}\n\n"
"Recommend 3 travel destinations that align well with this profile.\n"
"For each suggestion, give a reason why it’s a great fit.\n"
"Respond as a list of dictionaries with keys: name, reason."
    )

    response = await wrapper.llm.complete(prompt)
    return {
        "destinations": response.strip()
    }

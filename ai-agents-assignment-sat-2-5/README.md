🔗 Agentic AI Project — Assignment 2
This project includes three mini agent-based systems built using OpenAI Agent SDK + Runner. Each system simulates real-world use cases by handing off between multiple AI agents and using custom tools.

🧠 Overview of All 3 Agents
💼 1. Career Mentor Agent
Helps students explore career paths by suggesting fields, showing skill roadmaps, and real-world job roles.

Agents:

CareerAgent – suggests career fields based on user interest.

SkillAgent – provides a skill roadmap (beginner to advanced).

JobAgent – explains real-world job options related to the field.

Tool Used: get_career_roadmap()

Handoff Logic:
CareerAgent ➡ SkillAgent ➡ JobAgent

🌍 2. AI Travel Designer Agent
Plans a customized trip based on mood, interests, season, and region.

Agents:

DestinationAgent – recommends destinations.

BookingAgent – shows available flights.

ExploreAgent – suggests hotels, food & activities.

Tools Used: get_flights(), suggest_hotels()

Handoff Logic:
DestinationAgent ➡ BookingAgent ➡ ExploreAgent

🧙 3. Game Master Agent
A fantasy role-play engine with interactive storytelling, battles, and rewards.

Agents:

NarratorAgent – tells the story and sets scenes.

MonsterAgent – handles battle phases.

ItemAgent – gives loot and inventory updates.

Tools Used: roll_dice(), generate_event()

Handoff Logic:
NarratorAgent ⤷ MonsterAgent ⤷ ItemAgent ⤴ back to Narrator

🚀 How to Run
Install uv and create virtual environment:

bash
Copy
Edit
uv venv
uv venv activate
Install packages:

bash
Copy
Edit
pip install openai-agents-sdk openai python-dotenv
Add your OpenAI API key in .env:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
Run the project:

bash
Copy
Edit
uv run main.py
📝 Notes
Each system uses at least 2 agents, 2 tools, and includes handoff logic, as required.

Prompts, tool responses, and flow are customized to make the project unique.
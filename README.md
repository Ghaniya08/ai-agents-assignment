# Agentic AI Project — Assignment 2

This project includes **three multi-agent systems** built using the **OpenAI Agent SDK + Runner**.  
Each system simulates a real-world task using **tool-based agents** and proper **handoff logic**.

---

## Overview of All 3 Agents

---

### Career Mentor Agent

Helps students explore careers by suggesting fields, skill roadmaps, and job roles.

**Agents:**
- `CareerAgent` – Suggests career fields based on interests.
- `SkillAgent` – Provides a beginner-to-advanced skill roadmap.
- `JobAgent` – Explains real-world job roles and job-hunting tips.

**Tool Used:** `get_career_roadmap()`

**Handoff Logic:**
CareerAgent ➡ SkillAgent ➡ JobAgent

markdown
Copy
Edit

---

###  AI Travel Designer Agent

Designs personalized travel plans based on mood, interests, region, and season.

**Agents:**
- `DestinationAgent` – Recommends travel destinations.
- `BookingAgent` – Suggests mock flights and hotel options.
- `ExploreAgent` – Recommends food and local attractions.

**Tools Used:**
- `get_flights()`
- `suggest_hotels()`

**Handoff Logic:**
DestinationAgent ➡ BookingAgent ➡ ExploreAgent

---

### Game Master Agent

Runs an interactive text-based adventure game with battles, loot, and a fantasy story.

**Agents:**
- `NarratorAgent` – Drives the story and gives choices.
- `MonsterAgent` – Manages combat using dice logic.
- `ItemAgent` – Handles inventory and loot after events.

**Tools Used:**
- `roll_dice()`
- `generate_event()`

**Handoff Logic:**
NarratorAgent ➡ MonsterAgent ➡ ItemAgent ➡ back to Narrator


---

## How to Run

### 1. Install `uv` and set up virtual environment:
```bash
uv venv
uv venv activate
2. Install required packages:
bash
Copy
Edit
pip install openai-agents-sdk openai python-dotenv
3. Add your OpenAI API key in .env:
ini
Copy
Edit
GEMINI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
4. Run the app:

uv run
uv chainlit run main.py
Notes
Each project uses at least 2 agents, 2 tools, and proper handoff logic.

Prompts and flows are customized to make each system unique.

Built for practice with multi-agent AI systems using OpenAI SDK.

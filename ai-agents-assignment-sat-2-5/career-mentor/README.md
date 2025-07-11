# 🎓 Career Mentor Agent

This is a career guidance agent built using the OpenAI Agent SDK and Chainlit. It helps users explore different career options based on their interests and goals.

## What It Does

- Starts by asking the user about their interests.
- Suggests possible career fields.
- Shares a skill roadmap from beginner to advanced level.
- Gives real-world job role suggestions and tips.

## Agents Used

- **CareerAgent** – This is the starting agent. It talks to the user and suggests career fields based on their interests.
- **SkillAgent** – After a field is chosen, this agent explains what skills are needed and in what order to learn them.
- **JobAgent** – This agent provides job types, where to find them, and interview tips.

## Agent Flow

The user starts with the CareerAgent. Based on the response, the conversation is passed to the SkillAgent and then to the JobAgent. This flow happens using handoff logic.

Example:
CareerAgent → SkillAgent → JobAgent

## Technologies Used

- OpenAI Agent SDK
- Python
- Chainlit (for frontend interface)
- .env for API key management

## Purpose

This project was made for practice with multi-agent systems. It can be used by students, job seekers, or anyone planning their career path.

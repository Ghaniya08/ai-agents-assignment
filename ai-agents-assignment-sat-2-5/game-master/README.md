# 🧙 Game Master Agent

This is a fantasy adventure game built with the OpenAI Agent SDK. It lets users play a text-based game where they explore magical places, fight monsters, and collect treasure.

## What It Does

- Tells a fantasy story and reacts to your choices.
- Starts an adventure and gives you options to choose from.
- If danger appears, it takes you into battle.
- If you win or explore, you get rewards like items or gold.

## Agents Used

- NarratorAgent – Starts and continues the story. It also gives choices like “Go left or right?”
- MonsterAgent – Activated when there's a fight. It describes battles and asks you to roll dice.
- ItemAgent – Gives you loot like weapons, gold, or special items after events or battles.

## Tools Used

- `roll_dice()` – Used to decide the outcome of fights.
- `generate_event()` – Random events during the adventure.

## Agent Flow

The game starts with the NarratorAgent. If a fight begins, it hands off to MonsterAgent. If treasure is found, it hands off to ItemAgent. After that, it returns to the narrator to continue the story.

Example:
NarratorAgent → MonsterAgent → ItemAgent → NarratorAgent

## Technologies Used

- OpenAI Agent SDK
- Chainlit (for user interface)
- Python

## How to End

Type `end` any time to stop the game. The story will finish and reset everything.
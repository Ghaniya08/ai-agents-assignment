import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from setup_config import model, external_client, google_gemini_config
from expert.destination_agent import destination_agent
from expert.explore_agent import explore_agent
from expert.booking_agent import booking_agent

@cl.on_chat_start
async def start():
    # Initialize session state
    await cl.Message(
    "Hello traveler! Ready to plan your next unforgettable adventure? "
    "Tell me what kind of trip you're dreaming about—relaxation, exploration, or something wild?"
).send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": msg.content})

    thinking = await cl.Message("Planning...").send()

    try:
        result = await Runner.run(
            destination_agent,
            history,
            run_config=google_gemini_config
            )
        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
            thinking.content = f"❌ Error: {e}"
            await thinking.update()

import os
import dotenv
dotenv.load_dotenv()
from openai import AsyncOpenAI
import chainlit as cl

cl.instrument_openai()

@cl.on_chat_start
async def main():
    await cl.Message(content="Hi there!").send()

    res = await cl.AskActionMessage(
        content="Choose LLM!",
        actions=[
            cl.Action(name="gpt-4o-mini", value="openai", label="🫧 GPT 4o Mini"),
            cl.Action(name="gemini-1.5-flash", value="gemini", label="✨ Gemini"),
            cl.Action(name="llama-3.2-3B", value="huggingface", label="🤗 Llama 3.2"),
        ],
    ).send()

    if res:
        client = None
        settings = {
            "temperature": 0.8,
            "max_tokens": 1024,
            "stream": True
        }

        if res.get("value") == "openai":
            client = AsyncOpenAI(
                base_url="https://api.openai.com/v1",
                api_key=os.getenv("OPENAI_API_KEY")
            )
            settings["model"] = "gpt-4o-mini"

        elif res.get("value") == "gemini":
            client = AsyncOpenAI(
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=os.getenv("GEMINI_API_KEY")
            )
            settings["model"] = "gemini-1.5-flash"

        elif res.get("value") == "huggingface":
            client = AsyncOpenAI(
                base_url="https://api-inference.huggingface.co/v1/",
                api_key=os.getenv("HF_TOKEN")
            )
            settings["model"] = "meta-llama/Llama-3.2-3B-Instruct"

        cl.user_session.set("client", client)
        cl.user_session.set("settings", settings)
        


@cl.on_message
async def on_message(message: cl.Message):
    client = cl.user_session.get("client")
    settings = cl.user_session.get("settings")

    msg = cl.Message(content="")
    async for chunk in await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and cheerful assistant"
            },
            {
                "role": "user",
                "content": message.content
            }
        ],
        **settings
    ):
        token = chunk.choices[0].delta.content
        if token:
            await msg.stream_token(token)
    
    await msg.send()
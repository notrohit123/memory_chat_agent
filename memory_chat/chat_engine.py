from openai import OpenAI
from memory_chat.memory_manager import memory_store
import os

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

client = OpenAI(api_key=api_key)

def get_response(prompt, persona="default"):
    system_prompt = {
        "default": "You are a helpful assistant.",
        "therapist": "You are a kind and supportive therapist.",
        "coder": "You are an expert software engineer."
    }.get(persona, "You are a helpful assistant.")

    messages = [{"role": "system", "content": system_prompt}] + memory_store.get_conversation()
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    memory_store.append_user_message(prompt)
    memory_store.append_assistant_message(reply)
    return reply

from openai import OpenAI
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def llm_call(query, messages):

    history = ""

    for chat in messages:
        history += f"""
User: {chat['q']}
Assistant: {chat['a']}
"""
    profile = {}

    if os.path.exists("profile.json"):
        with open("profile.json", "r", encoding="utf-8") as file:
            profile = json.load(file)
    prompt = f"""

{SYSTEM_PROMPT}

User Profile:
{profile}

Previous Conversation:
{history}

Current Question:
{query}

"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
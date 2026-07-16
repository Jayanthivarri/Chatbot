from openai import OpenAI
from dotenv import load_dotenv
import os

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
    profile = ""

    if os.path.exists("profile.txt"):
        with open("profile.txt", "r", encoding="utf-8") as file:
            profile = file.read()

    prompt = f"""
You are a helpful AI assistant.

Instructions:
- Answer only in fluent English.
- Use the previous conversation whenever it is relevant.
- Remember facts shared by the user (such as name, skills, preferences, education, etc.).
- If the user asks about previous conversations, answer from the conversation history.
- Do not mix languages.
- Do not repeat words.
- Keep answers clear, concise, and natural.
- Use bullet points only when listing items.


User Profile:
{profile}

Previous Conversation:
{history}

Current Question:

{query}

Answer naturally. If the current question refers to previous conversation, use the previous conversation.
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

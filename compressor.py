from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def compress_messages(messages):

    history = ""

    for chat in messages:

        history += f"""
User: {chat['q']}
Assistant: {chat['a']}
"""

    prompt = f"""
Summarize the following conversation.

Keep only:

- User name
- Important facts
- Preferences
- Previous tasks
- Anything useful for future conversation

Conversation:

{history}

Return only the summary.
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
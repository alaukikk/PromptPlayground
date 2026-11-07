import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
MODEL_ID = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

def generate_response(prompt, system_instruction=None):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")
    client = Groq(api_key=api_key)
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        temperature=0.3,
        max_tokens=900
    )
    return response.choices[0].message.content

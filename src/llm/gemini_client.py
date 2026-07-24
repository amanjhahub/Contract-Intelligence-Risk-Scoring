import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(context, question):

    prompt = f"""
You are an AI Contract Assistant.

Answer ONLY using the information provided in the context below.

If the answer is not present in the context, reply:
"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
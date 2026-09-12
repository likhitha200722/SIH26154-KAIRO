import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def transform_content(
    source_text: str,
    audience: str,
    tone: str,
    language: str,
    objective: str,
    output_type: str
):

    prompt = f"""
You are an AI content transformation engine.

Transform the SOURCE MATERIAL according to the requirements.

IMPORTANT RULES:
1. Preserve all important facts from the source.
2. Do NOT invent statistics, dates, names, locations, or claims.
3. Do NOT change the factual meaning.
4. Adapt the content to the requested audience.
5. Follow the requested tone.
6. Follow the requested language.
7. Follow the requested objective.
8. Follow the requested output type.
9. If information is missing, do not make it up.
10. Return only the transformed content.

SOURCE MATERIAL:
{source_text}

AUDIENCE:
{audience}

TONE:
{tone}

LANGUAGE:
{language}

OBJECTIVE:
{objective}

OUTPUT TYPE:
{output_type}

Now transform the source material.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
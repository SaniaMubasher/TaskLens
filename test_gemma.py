import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents=(
        "Summarize this notice in one sentence: "
        "Submit the assignment by Monday."
    )
)

print(response.text)
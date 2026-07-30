import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


class GeminiService:

    def generate_response(self, prompt):

        try:

            response = client.models.generate_content(
                model="models/gemini-3.6-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"Error: {e}"
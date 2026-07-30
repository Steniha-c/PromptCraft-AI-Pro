from gemini_service import GeminiService

gemini = GeminiService()

response = gemini.generate_response(
    "Explain recursion in Python in simple words."
)

print("\nGemini Response:\n")
print(response)
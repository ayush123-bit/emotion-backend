import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

# Load .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_emotion_analysis(text: str):
    prompt = (
        f"Analyze the following sentence and identify the primary emotion and a confidence score out of 1. "
        f"Respond in the format: Emotion: <emotion>, Confidence: <score>\n\n"
        f"Sentence: \"{text}\""
    )

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    result_text = response.text

    # Example: "Emotion: Anxious, Confidence: 0.87"
    match = re.search(r"Emotion:\s*(\w+),\s*Confidence:\s*([0-9.]+)", result_text)

    if match:
        emotion = match.group(1)
        confidence = float(match.group(2))
    else:
        emotion = "Unknown"
        confidence = 0.0

    return emotion, confidence

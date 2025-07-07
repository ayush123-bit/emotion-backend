from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.gemini import get_emotion_analysis

app = FastAPI()

# Enable CORS for all domains (for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ReflectionInput(BaseModel):
    text: str

# Response model (optional)
class EmotionResponse(BaseModel):
    emotion: str
    confidence: float

@app.post("/analyze", response_model=EmotionResponse)
async def analyze_emotion(data: ReflectionInput):
    emotion, confidence = get_emotion_analysis(data.text)
    return {"emotion": emotion, "confidence": confidence}

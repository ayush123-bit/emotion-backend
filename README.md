
# 🧠 Emotion Reflection API (FastAPI + Gemini)

This backend service analyzes user reflections and returns the detected **emotion** along with a **confidence score**, using the Google Gemini Pro API.

---

## 🚀 Features

- Accepts text-based reflections from users
- Calls Google Gemini Pro model for emotion detection
- Returns emotion + confidence score in a clean JSON format
- CORS enabled for frontend integration

---

## 📁 Folder Structure

```
emotion-backend/
├── main.py                # FastAPI app
├── utils/
│   └── gemini.py          # Gemini API integration
├── .env                   # Contains your Gemini API key
├── requirements.txt       # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```
git clone https://github.com/ayush123-bit/emotion-backend
cd emotion-backend
```

### 2. Create a virtual environment

```bash
conda create -n emotion-api python=3.10
conda activate emotion-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env`

Create a file named `.env` in the root of the backend folder:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

You can get your Gemini API key from [https://makersuite.google.com/app](https://makersuite.google.com/app).

---

## ▶️ Run the Backend Server

```bash
uvicorn main:app --reload
```

Server runs on: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Test it via:

```json
POST /analyze
{
  "text": "I feel really overwhelmed with everything."
}
```

Response:
```json
{
  "emotion": "Stressed",
  "confidence": 0.92
}
```

---

## ✅ API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| POST   | /analyze  | Analyzes emotion in text |

---

## 📦 Requirements

- Python 3.10+
- FastAPI
- Google GenerativeAI SDK
- Python-dotenv

Install everything with:

```bash
pip install -r requirements.txt
```

---

## 💡 Example Prompt to Gemini

```
Analyze the following sentence and identify the primary emotion and a confidence score out of 1.
Respond in the format: Emotion: <emotion>, Confidence: <score>

Sentence: "I feel sad and unmotivated today."
```

---

## 🧠 Credits

Built with ❤️ using:
- FastAPI
- Gemini Pro API
- React (Frontend)

---

## 📝 License

MIT License

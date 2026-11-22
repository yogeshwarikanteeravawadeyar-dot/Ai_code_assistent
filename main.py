from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Code Assistant Running 🚀"}

@app.post("/chat")
def chat(request: dict):
    user_input = request.get("message", "")
    response = generate_response(user_input)
    return {"response": response}

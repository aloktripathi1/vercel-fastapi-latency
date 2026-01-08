from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
def analyze(payload: dict):
    return {"status": "ok"}


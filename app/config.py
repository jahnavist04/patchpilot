import os
from dotenv import load_dotenv

load_dotenv()

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY", "")
NEBIUS_BASE_URL = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1/")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# Ultra only for the hard step (patching); Nano/Super for quick calls
MODELS = {
    "patch": os.getenv("MODEL_ULTRA", ""),
    "classify": os.getenv("MODEL_NANO", ""),
    "explain": os.getenv("MODEL_SUPER", ""),
}

MAX_ATTEMPTS = 3

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")
REPLICATE_BASE_URL = "https://api.replicate.com/v1/predictions"
MODEL_VERSION_NAME = os.getenv("MODEL_VERSION_NAME")
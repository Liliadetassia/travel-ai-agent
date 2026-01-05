import os
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

APIFY_BASE_URL = "https://api.apify.com/v2"
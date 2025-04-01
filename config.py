# config.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")
FRED_BASE_URL = os.getenv("FRED_BASE_URL", "https://api.stlouisfed.org/fred")
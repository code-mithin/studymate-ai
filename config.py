"""App settings, read from environment variables (.env locally, dashboard vars on Render)."""
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env if present; harmless if missing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    DATABASE = os.getenv("DATABASE_PATH", os.path.join(BASE_DIR, "database", "studymate.db"))
    MAX_INPUT_CHARS = 12000

# config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "PlantHealthAnalyzer")
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    ENVIROMENT = os.getenv("ENV")


def get_config():
    return Config

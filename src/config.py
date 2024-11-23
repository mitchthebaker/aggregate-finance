import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("ENVIRONMENT") == "DEV"
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT", "3101"))
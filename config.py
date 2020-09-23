from dotenv import load_dotenv
import os

load_dotenv()

def api_key():
  return os.getenv("API_KEY")
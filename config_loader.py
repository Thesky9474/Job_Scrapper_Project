import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "SENDER_EMAIL": os.getenv("SENDER_EMAIL"),
        "RECEIVER_EMAIL": os.getenv("RECEIVER_EMAIL"),
        "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD")
    }
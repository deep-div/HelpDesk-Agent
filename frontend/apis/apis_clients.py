import requests
from dotenv import load_dotenv
import os

path = ".env"
load_dotenv(dotenv_path = path) 
 
# Url
url_chat_service = os.getenv("CHAT_SERVICE")

class Api:
    def __init__(self, base_url=url_chat_service):
        self.base_url = base_url

    def chat_ui(self, payload: dict):
        url = f"{self.base_url}/chat-get-prompt-from-ui/"
        response = requests.post(url, json=payload)
        return response.json()

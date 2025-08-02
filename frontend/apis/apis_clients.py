from backend.app.models.data_models import RegisterComplaint, ComplaintStatus, Prompt
import requests

class Api:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def chat_ui(self, payload: Prompt):
        url = f"{self.base_url}/chat-get-prompt-from-ui/"
        response = requests.post(url, json=payload)
        return response.json()

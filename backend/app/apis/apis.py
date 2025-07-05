from backend.app.models.data_models import RegisterComplaint, ComplaintStatus
import requests

class Api:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def register_complaints(self, payload: RegisterComplaint):
        url = f"{self.base_url}/register-complaints/"
        response = requests.post(url, json=payload)
        return response.json()

    def check_status(self, payload: ComplaintStatus):
        url = f"{self.base_url}/status/"
        response = requests.post(url, json=payload)
        return response.json()

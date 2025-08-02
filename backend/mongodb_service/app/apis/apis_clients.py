from backend.mongodb_service.app.models.data_models import RegisterComplaint, ComplaintStatus
from backend.mongodb_service.app.core.config import url_mongodb_service
import requests

class Api:
    def __init__(self, base_url= url_mongodb_service):
        self.base_url = base_url

    def register_complaints(self, payload: RegisterComplaint):
        print(payload)
        url = f"{self.base_url}/register-complaint-mongodb/"
        response = requests.post(url, json=payload, timeout=5)
        return response.json()

    def check_status(self, payload: ComplaintStatus):
        url = f"{self.base_url}/check-complaint-status-mongodb/"
        response = requests.post(url, json=payload, timeout=5)
        return response.json()

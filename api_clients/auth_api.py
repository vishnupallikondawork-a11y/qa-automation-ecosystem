import requests
from utils.config import API_BASE_URL
from utils.logger import get_logger

class AuthAPI:

    def __init__(self):
        self.logger = get_logger()
    
    def login(self, email, password):

        self.logger.info(
            "Sending login API request"
        )
        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{API_BASE_URL}/verifyLogin",
            data = payload
        )
        
        self.logger.info(
            f"Response Status Code: {response.status_code}"
        )
        return response
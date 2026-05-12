from utils.logger import get_logger
import requests
from utils.config import API_BASE_URL
class ProductAPI:
    def __init__(self):
        self.logger = get_logger()
    
    def get_all_products(self):
        self.logger.info("Send product list API request")
        response = requests.get(f"{API_BASE_URL}/productsList")
        self.logger.info(f"Response Status Code: {response.status_code}")

        return response
    
    def get_invalid_products_api(self):

        self.logger.info(
            "Sending Invalid products API request"
        )
        response = requests.get(
            f"{API_BASE_URL}/invalidEndpoint"
        )

        return response
import pytest
from api_clients.product_api import ProductAPI
from utils.api_utils import APIUtils


@pytest.mark.api
@pytest.mark.regression

def test_get_all_products():
    products = ProductAPI()
    response = products.get_all_products()
    response_body = response.json()
    
    APIUtils.validate_status_code(response, 200)
    APIUtils.validate_response_code(response_body, 200)
    assert len(response_body["products"]) > 0 
    
    first_product = response_body["products"][0]

    APIUtils.validate_key_exists(first_product,"id")
    APIUtils.validate_key_exists(first_product,"name")
    APIUtils.validate_key_exists(first_product,"price")

def test_invalid_products_api():
    product_api = ProductAPI()
    response = product_api.get_invalid_products_api()

    APIUtils.validate_status_code(response, 404)
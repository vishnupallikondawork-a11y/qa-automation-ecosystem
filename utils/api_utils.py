class APIUtils:

    @staticmethod
    def validate_status_code(response, expected_code):

        assert response.status_code == expected_code, (
            f"Expected status code {expected_code},"
            f"but got {response.status}"
        )

    @staticmethod
    def validate_response_code(response_body, expected_code):

        assert response_body["responseCode"] == expected_code, (
            f"Expected response code {expected_code}, "
            f"but got {response_body['responseCode']}"
        )

    @staticmethod
    def validate_key_exists(data, key):

        assert key in data, (
            f"Key '{key}' not found in response"
        )
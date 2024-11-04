import json
from pathlib import Path


class ApiSupport:

    def __init__(self, api):
        self.api = api

    def get_response_body(self):
        """
        Navigate the web driver to the specified URL.
        """
        json_response = self.api.response.json()
        return json_response

    def get_response_value(self, field_name):
        """
        Retrieve the value of a specified field from the JSON response.
        Args:
            field_name (str): The name of the field to retrieve from the JSON response.
        Returns:
            The value associated with the specified field name in the JSON response.
        """
        json_response = self.get_response_body()
        return json_response[field_name]

    def validate_response_attribute_equals(self, field_name, expected_value):
        """
        Validate that the specified field in the JSON response matches the expected value.

        Args:
            field_name (str): The name of the field to retrieve from the JSON response.
            expected_value (Any): The value expected for the specified field.

        Raises:
            AssertionError: If the actual value does not match the expected value.
        """
        value = self.get_response_value(field_name)
        assert str(value) == str(
            expected_value
        ), f"Expected value: {expected_value}, got: {value}"

    def validate_response_attribute_not_none(self, field_name):
        """
        Validate that the specified field in the JSON response is not None.

        Args:
            field_name (str): The name of the field to retrieve from the JSON response.

        Raises:
            AssertionError: If the value of the specified field is None.
        """
        value = self.get_response_value(field_name)
        assert value is not None, f"Expected value: {value} is None"

    @staticmethod
    def parse_json(filename):
        """
        Load and parse a JSON file from the schemas directory.

        Args:
            filename (str): The name of the JSON file to load.

        Returns:
            dict: The parsed JSON content as a dictionary.
        """
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    def check_status_code(self, name: str = None, expect_code: int = 200):
        """
        Check if the HTTP response status code matches the expected status code.

        Args:
            name (str, optional): A label for the request being checked, used in error messages.
            expect_code (int, optional): The expected HTTP status code. Defaults to 200.

        Raises:
            AssertionError: If the actual status code does not match the expected code.
        """
        actual_code = self.api.response.status_code
        assert actual_code == expect_code, (
            f"Request for {name} failed.\n"
            f"Request URL: {self.api.response.request.method}"
            f":{self.api.response.request.url}\n"
            f"Request body: {self.api.response.request.body}\n"
            f"Expected status code: {expect_code}\n"
            f"Actual status code: {actual_code}\n"
            f"Reason: {self.api.response.reason}\n"
            f"Text: {self.api.response.text}"
        )

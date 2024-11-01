import json
from pathlib import Path


class ApiSupport:

    def __init__(self, api):
        self.api = api

    def get_response_body(self):
        json_response = self.api.response.json()
        return json_response

    def get_response_value(self, field_name):
        json_response = self.get_response_body()
        return json_response[field_name]

    def validate_response_attribute_equals(self, field_name, expected_value):
        value = self.get_response_value(field_name)
        assert str(value) == str(
            expected_value
        ), f"Expected value: {expected_value}, got: {value}"

    def prepare_json_for_request(self, json_file):
        json_body = self.parse_json(json_file)
        return json.dumps(json_body)

    def validate_response_attribute_not_none(self, field_name):
        value = self.get_response_value(field_name)
        assert value is not None, f"Expected value: {value} is Null"

    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    def check_status_code(self, name: str = None, expect_code: int = 200):
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

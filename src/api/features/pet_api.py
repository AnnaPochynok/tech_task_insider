import json

from src.api.client.api_support import ApiSupport


class PetApi:

    def __init__(self, api):
        self.api = api
        self.support = ApiSupport(api)
        self.pet_endpoint = "/pet"
        self.status_endpoint = "/findByStatus"
        self.image_endpoint = "/uploadImage"

    def post_pet(self, pet_id: int, name: str, status: str):
        json_body = self.create_pet_request_body(
            pet_id=pet_id, name=name, status=status
        )
        self.api.post(url=self.api.api_url, endpoint=self.pet_endpoint, body=json_body)

    def get_pet_by_id(self, pet_id: int):
        self.api.get(url=self.api.api_url, endpoint=f"{self.pet_endpoint}/{pet_id}")

    def get_pets_by_status(self, status):
        self.api.get(
            url=self.api.api_url,
            endpoint=self.pet_endpoint + self.status_endpoint,
            params=f"status={status}",
        )

    def edit_pet(self, pet_id, name: str = None, status: str = None):
        json_body = self.create_pet_request_body(
            pet_id=pet_id, name=name, status=status
        )
        self.api.put(url=self.api.api_url, endpoint=self.pet_endpoint, body=json_body)

    def update_pet_by_id(self, pet_id, name: str, status: str):
        form_data = {"name": name, "status": status}
        self.api.post(
            url=self.api.api_url,
            endpoint=f"{self.pet_endpoint}/{pet_id}",
            body=form_data,
            headers=self.api.formdata_headers,
        )

    def delete_pet_by_id(self, pet_id):
        self.api.delete(url=self.api.api_url, endpoint=f"{self.pet_endpoint}/{pet_id}")

    def create_pet_request_body(self, pet_id: int, name: str, status: str):
        create_body = self.support.parse_json("pet.json")
        create_body["id"] = pet_id
        create_body["name"] = name
        create_body["status"] = status
        json_body = json.dumps(create_body)
        return json_body

    def check_response_contains_correct_id(self, pet_id):
        self.support.validate_response_attribute_equals("id", pet_id)

    def check_response_contains_correct_name(self, pet_name):
        self.support.validate_response_attribute_equals("name", pet_name)

    def check_response_contains_correct_status(self, pet_status):
        self.support.validate_response_attribute_equals("status", pet_status)

    def check_all_pets_have_correct_status(self, pet_status):
        pets_list = self.support.get_response_body()
        for pet in pets_list:
            current_status = pet["status"]
            assert (
                current_status == pet_status
            ), f"Expected {pet_status}, got {current_status}"

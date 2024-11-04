import json

from src.api.client.api_support import ApiSupport


class PetApi:
    """A client for interacting with the Pet API, providing methods to perform CRUD operations
    on pet data and validate API responses."""

    def __init__(self, api):
        self.api = api
        self.support = ApiSupport(api)
        self.pet_endpoint = "/pet"
        self.status_endpoint = "/findByStatus"
        self.image_endpoint = "/uploadImage"

    def post_pet(self, pet_id: int, name: str, status: str):
        """
        Create a new pet entry.

        Args:
            pet_id (int): The unique ID of the pet.
            name (str): The name of the pet.
            status (str): The status of the pet (e.g., available, pending, sold).
        """
        json_body = self.create_pet_request_body(
            pet_id=pet_id, name=name, status=status
        )
        self.api.post(url=self.api.api_url, endpoint=self.pet_endpoint, body=json_body)

    def get_pet_by_id(self, pet_id: int):
        """
        Retrieve pet information by pet ID.

        Args:
            pet_id (int): The ID of the pet to retrieve.
        """
        self.api.get(url=self.api.api_url, endpoint=f"{self.pet_endpoint}/{pet_id}")

    def get_pets_by_status(self, status):
        """
        Retrieve a list of pets by their status.

        Args:
            status (str): The status to filter pets by (e.g., available, pending, sold).
        """
        self.api.get(
            url=self.api.api_url,
            endpoint=self.pet_endpoint + self.status_endpoint,
            params=f"status={status}",
        )

    def edit_pet(self, pet_id, name: str = None, status: str = None):
        """
        Update pet information by pet ID.

        Args:
            pet_id (int): The ID of the pet to update.
            name (str, optional): The new name of the pet.
            status (str, optional): The new status of the pet.
        """
        json_body = self.create_pet_request_body(
            pet_id=pet_id, name=name, status=status
        )
        self.api.put(url=self.api.api_url, endpoint=self.pet_endpoint, body=json_body)

    def update_pet_by_id(self, pet_id, name: str, status: str):
        """
        Update specific attributes of a pet using form data.

        Args:
            pet_id (int): The ID of the pet to update.
            name (str): The new name of the pet.
            status (str): The new status of the pet.
        """
        form_data = {"name": name, "status": status}
        self.api.post(
            url=self.api.api_url,
            endpoint=f"{self.pet_endpoint}/{pet_id}",
            body=form_data,
            headers=self.api.formdata_headers,
        )

    def delete_pet_by_id(self, pet_id):
        """
        Delete a pet by its ID.

        Args:
            pet_id (int): The ID of the pet to delete.
        """
        self.api.delete(url=self.api.api_url, endpoint=f"{self.pet_endpoint}/{pet_id}")

    def create_pet_request_body(self, pet_id: int, name: str, status: str):
        """
        Create the JSON body for a pet request.

        Args:
            pet_id (int): The unique ID of the pet.
            name (str): The name of the pet.
            status (str): The status of the pet.

        Returns:
            str: A JSON string representing the pet data.
        """
        create_body = self.support.parse_json("pet.json")
        create_body["id"] = pet_id
        create_body["name"] = name
        create_body["status"] = status
        json_body = json.dumps(create_body)
        return json_body

    def check_response_contains_correct_id(self, pet_id):
        """
        Validate that the response contains the correct pet ID.

        Args:
            pet_id (int): The expected ID of the pet.
        """
        self.support.validate_response_attribute_equals("id", pet_id)

    def check_response_contains_correct_name(self, pet_name):
        """
        Validate that the response contains the correct pet name.

        Args:
            pet_name (str): The expected name of the pet.
        """
        self.support.validate_response_attribute_equals("name", pet_name)

    def check_response_contains_correct_status(self, pet_status):
        """
        Validate that the response contains the correct pet status.

        Args:
            pet_status (str): The expected status of the pet.
        """
        self.support.validate_response_attribute_equals("status", pet_status)

    def check_all_pets_have_correct_status(self, pet_status):
        """
        Validate that all pets in the response have the correct status.

        Args:
            pet_status (str): The expected status for all pets.
        """
        pets_list = self.support.get_response_body()
        for pet in pets_list:
            current_status = pet["status"]
            assert (
                current_status == pet_status
            ), f"Expected {pet_status}, got {current_status}"

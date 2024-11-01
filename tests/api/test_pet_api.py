from random import randint

import pytest

from src.api.client.api_support import ApiSupport
from src.api.features.pet_api import PetApi
from data.constants import ApiConstants


@pytest.mark.usefixtures("api")
class TestApiPet:

    @pytest.fixture(autouse=True)
    def pre_test(self, api):
        self.api = api
        self.pet_api = PetApi(api)
        self.support = ApiSupport(api)

    @pytest.mark.parametrize(
        "status",
        [
            ApiConstants.PET_STATUS_AVAILABLE,
            ApiConstants.PET_STATUS_PENDING,
            ApiConstants.PET_STATUS_SOLD,
        ],
    )
    def test_add_pet_with_different_valid_statuses(self, status):
        pet_id = randint(1, 1000)
        self.pet_api.post_pet(pet_id=pet_id, name=ApiConstants.PET_NAME, status=status)
        self.support.check_status_code(expect_code=200)
        self.pet_api.check_response_contains_correct_id(pet_id=pet_id)
        self.pet_api.check_response_contains_correct_name(
            pet_name=ApiConstants.PET_NAME
        )
        self.pet_api.check_response_contains_correct_status(pet_status=status)

    def test_id_generates_if_no_id_in_request(self):
        self.pet_api.post_pet(
            pet_id=None, name=ApiConstants.PET_NAME, status=ApiConstants.PET_STATUS_SOLD
        )
        self.support.check_status_code(expect_code=200)
        self.support.validate_response_attribute_not_none("id")

    def test_get_added_pet(self):
        pet_id = randint(1, 1000)
        self.pet_api.post_pet(
            pet_id=pet_id,
            name=ApiConstants.PET_NAME,
            status=ApiConstants.PET_STATUS_AVAILABLE,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.get_pet_by_id(pet_id=pet_id)
        self.support.check_status_code(expect_code=200)
        self.pet_api.check_response_contains_correct_id(pet_id=pet_id)

    def test_get_pet_with_unknown_id(self):
        self.pet_api.get_pet_by_id(pet_id=10000000000)
        self.support.check_status_code(expect_code=404)
        self.support.validate_response_attribute_equals(
            "message", ApiConstants.ERROR_M_PET_NOT_FOUND
        )

    def test_update_existed_pet_name_status(self):
        self.pet_api.post_pet(
            pet_id=ApiConstants.PET_ID,
            name=ApiConstants.PET_NAME,
            status=ApiConstants.PET_STATUS_AVAILABLE,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.edit_pet(
            pet_id=ApiConstants.PET_ID,
            name=ApiConstants.PET_NEW_NAME,
            status=ApiConstants.PET_STATUS_SOLD,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.get_pet_by_id(pet_id=ApiConstants.PET_ID)
        self.pet_api.check_response_contains_correct_name(
            pet_name=ApiConstants.PET_NEW_NAME
        )
        self.pet_api.check_response_contains_correct_status(
            pet_status=ApiConstants.PET_STATUS_SOLD
        )

    def test_update_existed_pet_to_unknown_status(self):
        self.pet_api.edit_pet(
            pet_id=ApiConstants.PET_ID, name=ApiConstants.PET_NEW_NAME, status="Existed"
        )
        self.support.check_status_code(expect_code=200)

    def test_find_pet_by_status(self):
        self.pet_api.get_pets_by_status(status=ApiConstants.PET_STATUS_SOLD)
        self.support.check_status_code(expect_code=200)
        self.pet_api.check_all_pets_have_correct_status(
            pet_status=ApiConstants.PET_STATUS_SOLD
        )

    def test_find_pet_by_unknown_status(self):
        self.pet_api.get_pets_by_status(status="Hello")
        self.support.check_status_code(expect_code=200)

    def test_update_pet_by_id(self):
        self.pet_api.post_pet(
            pet_id=ApiConstants.PET_ID,
            name=ApiConstants.PET_NAME,
            status=ApiConstants.PET_STATUS_AVAILABLE,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.update_pet_by_id(
            pet_id=ApiConstants.PET_ID,
            name=ApiConstants.PET_NEW_NAME,
            status=ApiConstants.PET_STATUS_PENDING,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.get_pet_by_id(pet_id=ApiConstants.PET_ID)
        self.pet_api.check_response_contains_correct_name(
            pet_name=ApiConstants.PET_NEW_NAME
        )
        self.pet_api.check_response_contains_correct_status(
            pet_status=ApiConstants.PET_STATUS_PENDING
        )

    def test_update_pet_by_unknown_id(self):
        self.pet_api.update_pet_by_id(
            pet_id=1000000000000000,
            name=ApiConstants.PET_NEW_NAME,
            status=ApiConstants.PET_STATUS_PENDING,
        )
        self.support.check_status_code(expect_code=404)
        self.support.validate_response_attribute_equals(
            "message", ApiConstants.ERROR_M_NOT_FOUND
        )

    def test_delete_existed_pet(self):
        pet_id = randint(1, 1000)
        self.pet_api.post_pet(
            pet_id=pet_id,
            name=ApiConstants.PET_NAME,
            status=ApiConstants.PET_STATUS_AVAILABLE,
        )
        self.support.check_status_code(expect_code=200)
        self.pet_api.delete_pet_by_id(pet_id=pet_id)
        self.support.check_status_code(expect_code=200)
        self.support.validate_response_attribute_equals("message", pet_id)
        self.pet_api.get_pet_by_id(pet_id=pet_id)
        self.support.check_status_code(expect_code=404)
        self.support.validate_response_attribute_equals(
            "message", ApiConstants.ERROR_M_PET_NOT_FOUND
        )

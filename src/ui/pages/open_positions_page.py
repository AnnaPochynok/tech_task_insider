from src.ui.pages.base_page import BasePage
from src.ui.locators import open_positions_locators


class OpenPositionsPage(BasePage):

    def verify_department_filter_already_filled(self, department):
        elem = open_positions_locators.get_department_filter_with_selected_value(department)
        self.wait_until_element_appears(elem)

    def filter_position_by_location(self, location):
        self.click_element(open_positions_locators.LOCATION_FILTER)
        self.wait_until_element_appears(open_positions_locators.LOCATION_FILTER_LIST)
        location_locator = open_positions_locators.get_filter_locator_by_location(location)
        self.wait_until_element_appears(location_locator)
        self.click_element(location_locator)

    def verify_jobs_listed(self, jobs_expected_number):
        self.wait_until_listing_reloads(open_positions_locators.JOBS_LISTING, jobs_expected_number)

    def verify_job_departments_in_the_list(self, department):
        items = self.get_list_of_elements(open_positions_locators.JOBS_LIST_DEPARTMENTS)
        for i in items:
            text = i.text
            assert text == department, f"Expected text: {department}, got {text}"

    def verify_job_locations_in_the_list(self, location):
        items = self.get_list_of_elements(open_positions_locators.JOBS_LIST_LOCATIONS)
        for i in items:
            text = i.text
            assert text == location, f"Expected text: {location}, got {text}"

    def click_on_view_role(self):
        self.hover_to_element(open_positions_locators.JOB_LIST_FIRST_JOB)
        self.wait_until_element_appears(open_positions_locators.VIEW_ROLE_BUTTON)
        self.click_element(open_positions_locators.VIEW_ROLE_BUTTON)

    def verify_redirection(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        url = self.get_current_url()
        assert "lever" in url, f'Expect link with "Lever" inside, got {url}'

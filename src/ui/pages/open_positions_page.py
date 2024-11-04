from src.ui.pages.base_page import BasePage
from src.ui.locators import open_positions_locators


class OpenPositionsPage(BasePage):
    """A page class for interacting with the open positions section,
    inheriting from BasePage to utilize common web interaction methods."""

    def verify_department_filter_already_filled(self, department):
        """
        Verify that the specified department filter is already selected.

        Args:
            department (str): The department name to verify.

        Raises:
            TimeoutException: If the element does not appear within the wait time.
        """
        elem = open_positions_locators.get_department_filter_with_selected_value(department)
        self.wait_until_element_appears(elem)

    def filter_position_by_location(self, location):
        """
        Filter job positions by the specified location.

        Args:
            location (str): The location to filter positions by.
        """
        self.click_element(open_positions_locators.LOCATION_FILTER)
        self.wait_until_element_appears(open_positions_locators.LOCATION_FILTER_LIST)
        location_locator = open_positions_locators.get_filter_locator_by_location(location)
        self.wait_until_element_appears(location_locator)
        self.click_element(location_locator)

    def verify_jobs_listed(self, jobs_expected_number):
        """
        Verify that the expected number of job listings are displayed.

        Args:
            jobs_expected_number (int): The expected number of job listings.
        """
        self.wait_until_listing_reloads(open_positions_locators.JOBS_LISTING, jobs_expected_number)

    def verify_job_departments_in_the_list(self, department):
        """
        Verify that all job listings match the specified department.

        Args:
            department (str): The department name to verify.

        Raises:
            AssertionError: If any job listing does not match the expected department.
        """
        items = self.get_list_of_elements(open_positions_locators.JOBS_LIST_DEPARTMENTS)
        for i in items:
            text = i.text
            assert text == department, f"Expected text: {department}, got {text}"

    def verify_job_locations_in_the_list(self, location):
        """
        Verify that all job listings match the specified location.

        Args:
            location (str): The location name to verify against.

        Raises:
            AssertionError: If any job listing does not match the expected location.
        """
        items = self.get_list_of_elements(open_positions_locators.JOBS_LIST_LOCATIONS)
        for i in items:
            text = i.text
            assert text == location, f"Expected text: {location}, got {text}"

    def click_on_view_role(self):
        """Click on the "View Role" button for the first job listing."""
        self.hover_to_element(open_positions_locators.JOB_LIST_FIRST_JOB)
        self.wait_until_element_appears(open_positions_locators.VIEW_ROLE_BUTTON)
        self.click_element(open_positions_locators.VIEW_ROLE_BUTTON)

    def verify_redirection(self):
        """
        Verify that the user is redirected to the correct URL for the job listing.

        Raises:
            AssertionError: If the current URL does not contain "lever".
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
        url = self.get_current_url()
        assert "lever" in url, f'Expect link with "Lever" inside, got {url}'

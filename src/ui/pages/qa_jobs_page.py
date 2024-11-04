from src.ui.pages.base_page import BasePage
from src.ui.locators import qa_page_locators
from data.constants import TestConstants


class QAJobsPage(BasePage):
    """A page class for interacting with the Quality Assurance careers section,
    inheriting from BasePage to utilize common web interaction methods."""

    URL = "https://useinsider.com/careers/quality-assurance/"

    def open_qa_career_page(self):
        """
        Navigate to the Quality Assurance careers page.

        Raises:
            AssertionError: If the page title does not match the expected value.
        """
        self.go_to_url(self.URL)
        text = self.get_text_from_locator(qa_page_locators.QA_TITLE_PAGE)
        assert text == TestConstants.DEPARTMENT_FOR_TEST, (
            f"Expected text: {TestConstants.DEPARTMENT_FOR_TEST}, got {text}"
        )

    def open_all_qa_jobs_page(self):
        """Click on the button to view all available Quality Assurance job listings."""
        self.click_element(qa_page_locators.SEE_ALL_QA_JOBS_BUTTON)

    def click_accept_all(self):
        """Click on the button to accept all cookies or policies on the page."""
        self.click_element(qa_page_locators.ACCEPT_ALL_BUTTON)

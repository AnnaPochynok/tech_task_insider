from src.ui.pages.base_page import BasePage
from src.ui.locators import qa_page_locators
from data.constants import TestConstants


class QAJobsPage(BasePage):
    URL = "https://useinsider.com/careers/quality-assurance/"

    def open_qa_career_page(self):
        self.go_to_url(self.URL)
        text = self.get_text_from_locator(qa_page_locators.QA_TITLE_PAGE)
        assert text == TestConstants.DEPARTMENT_FOR_TEST, (
            f"Expected text: {TestConstants.DEPARTMENT_FOR_TEST}, got {text}"
        )

    def open_all_qa_jobs_page(self):
        self.click_element(qa_page_locators.SEE_ALL_QA_JOBS_BUTTON)

    def click_accept_all(self):
        self.click_element(qa_page_locators.ACCEPT_ALL_BUTTON)

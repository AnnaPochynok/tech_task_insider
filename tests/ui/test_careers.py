import pytest

from src.ui.pages.home_page import HomePage
from src.ui.pages.career_page import CareerPage
from src.ui.pages.qa_jobs_page import QAJobsPage
from src.ui.pages.open_positions_page import OpenPositionsPage
from data.constants import TestConstants


@pytest.mark.usefixtures("driver")
class TestCareers:

    @pytest.fixture(autouse=True)
    def pre_test(self, driver):
        self.home_page = HomePage(driver)
        self.career_page = CareerPage(driver)
        self.qa_jobs_page = QAJobsPage(driver)
        self.open_positions_page = OpenPositionsPage(driver)

    def test_opened_jobs_filtering(self):
        self.home_page.open_home_page()
        self.home_page.check_home_page_is_opened()

        self.home_page.go_to_careers()
        self.career_page.verify_career_blocks()

        self.qa_jobs_page.open_qa_career_page()
        self.qa_jobs_page.click_accept_all()
        self.qa_jobs_page.open_all_qa_jobs_page()
        self.open_positions_page.verify_department_filter_already_filled(department=TestConstants.DEPARTMENT_FOR_TEST)

        self.open_positions_page.filter_position_by_location(location=TestConstants.LOCATION_FOR_TEST)
        self.open_positions_page.verify_jobs_listed(jobs_expected_number=1)
        self.open_positions_page.verify_job_departments_in_the_list(department=TestConstants.DEPARTMENT_FOR_TEST)
        self.open_positions_page.verify_job_locations_in_the_list(location=TestConstants.LOCATION_FOR_TEST)
        self.open_positions_page.click_on_view_role()

        self.open_positions_page.verify_redirection()

    def test_open_main_page_negative_screenshot_check(self):
        self.home_page.open_home_page()
        self.home_page.check_home_page_is_opened_negative()

from src.ui.pages.base_page import BasePage
from src.ui.locators import home_page_locators


class HomePage(BasePage):

    URL = "https://useinsider.com/"

    def open_home_page(self):
        self.go_to_url(self.URL)

    def go_to_careers(self):
        self.click_element(home_page_locators.COMPANY_MENU)
        self.click_element(home_page_locators.COMPANY_MENU_CAREERS)

    def check_home_page_is_opened(self):
        text = self.get_text_from_locator(home_page_locators.HOME_PAGE_H1)
        assert (
            text
            == "#1 AI-native\nOmnichannel Experience\nand Customer Engagement Platform"
        ), "Home page did not open"

    def check_home_page_is_opened_negative(self):
        text = self.get_text_from_locator(home_page_locators.HOME_PAGE_H1)
        assert text == "Hello!", "Home page did not open"

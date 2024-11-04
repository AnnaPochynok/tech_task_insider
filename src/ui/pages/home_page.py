from src.ui.pages.base_page import BasePage
from src.ui.locators import home_page_locators


class HomePage(BasePage):
    """A page class for interacting with the home page of the Insider website,
    inheriting from BasePage to utilize common web interaction methods."""

    URL = "https://useinsider.com/"

    def open_home_page(self):
        """Navigate to the home page of the Insider website."""
        self.go_to_url(self.URL)

    def go_to_careers(self):
        """Navigate to the careers section of the Insider website."""
        self.click_element(home_page_locators.COMPANY_MENU)
        self.click_element(home_page_locators.COMPANY_MENU_CAREERS)

    def check_home_page_is_opened(self):
        """
        Verify that the home page has opened correctly.

        Raises:
            AssertionError: If the header text does not match the expected value.
        """
        text = self.get_text_from_locator(home_page_locators.HOME_PAGE_H1)
        assert (
            text
            == "#1 AI-native\nOmnichannel Experience\nand Customer Engagement Platform"
        ), "Home page did not open"

    def check_home_page_is_opened_negative(self):
        """
        Verify that the home page did not open correctly.

        Raises:
            AssertionError: If the header text matches the expected negative value.
        """
        text = self.get_text_from_locator(home_page_locators.HOME_PAGE_H1)
        assert text == "Hello!", "Home page did not open"

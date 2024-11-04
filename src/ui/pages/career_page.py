from src.ui.locators import career_page_locators
from src.ui.pages.base_page import BasePage


class CareerPage(BasePage):
    """A page class for interacting with the career section,
    inheriting from BasePage to utilize common web interaction methods."""

    def verify_career_blocks(self):
        """
        Verify that Locations Block, Teams Block and Life at Insider Block sections are displayed on the page.

        Raises:
            AssertionError: If any of the blocks are not displayed.
        """
        self.element_is_displayed(career_page_locators.LOCATIONS_BLOCK)
        self.element_is_displayed(career_page_locators.TEAMS_BLOCK)
        self.element_is_displayed(career_page_locators.LIFE_AT_INSIDER_BLOCK)

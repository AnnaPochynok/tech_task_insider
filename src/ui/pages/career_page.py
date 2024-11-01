from src.ui.locators import career_page_locators
from src.ui.pages.base_page import BasePage


class CareerPage(BasePage):
    def verify_career_blocks(self):
        self.element_is_displayed(career_page_locators.LOCATIONS_BLOCK)
        self.element_is_displayed(career_page_locators.TEAMS_BLOCK)
        self.element_is_displayed(career_page_locators.LIFE_AT_INSIDER_BLOCK)

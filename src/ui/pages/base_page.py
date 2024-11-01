import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(driver)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        elem = self.driver.find_element(By.XPATH, locator)
        elem.click()

    def hover_to_element(self, locator):
        elem = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.actions.move_to_element(elem).perform()

    def get_list_of_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def element_is_displayed(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed(), "This element is not displaying"

    def get_text_from_locator(self, locator):
        return self.driver.find_element(By.XPATH, locator).text

    def wait_until_element_appears(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element

    def count_number_of_elements(self, locator):
        return len(self.driver.find_elements(By.XPATH, locator))

    def wait_until_listing_reloads(self, jobs_selector, expected_quantity=1):
        attempts_counter = 0
        while (
            self.count_number_of_elements(jobs_selector) > expected_quantity
            and attempts_counter <= 5
        ):
            time.sleep(1)
            attempts_counter += 1

    def get_current_url(self):
        return self.driver.current_url

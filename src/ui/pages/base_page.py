import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """A base class for web pages, providing common methods to interact with elements
    using Selenium WebDriver."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(driver)

    def go_to_url(self, url):
        """
        Navigate to a specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.driver.get(url)

    def get_current_url(self):
        """
        Retrieve the current URL of the page.

        Returns:
            str: The current URL.
        """
        return self.driver.current_url

    def click_element(self, locator):
        """
        Click an element specified by an XPath locator.

        Args:
            locator (str): The XPath of the element to click.
        """
        elem = self.driver.find_element(By.XPATH, locator)
        elem.click()

    def hover_to_element(self, locator):
        """
        Scroll to and hover over an element specified by an XPath locator.

        Args:
            locator (str): The XPath of the element to hover over.
        """
        elem = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.actions.move_to_element(elem).perform()

    def get_list_of_elements(self, locator):
        """
        Retrieve a list of elements matching the specified XPath locator.

        Args:
            locator (str): The XPath of the elements to find.

        Returns:
            list[WebElement]: A list of elements matching the locator.
        """
        return self.driver.find_elements(By.XPATH, locator)

    def element_is_displayed(self, locator):
        """
        Assert that an element specified by an XPath locator is displayed.

        Args:
            locator (str): The XPath of the element to check.

        Raises:
            AssertionError: If the element is not displayed.
        """
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed(), "This element is not displaying"

    def get_text_from_locator(self, locator):
        """
        Retrieve the text of an element specified by an XPath locator.

        Args:
            locator (str): The XPath of the element to retrieve text from.

        Returns:
            str: The text of the element.
        """
        return self.driver.find_element(By.XPATH, locator).text

    def wait_until_element_appears(self, locator):
        """
        Wait until an element specified by an XPath locator is present.

        Args:
            locator (str): The XPath of the element to wait for.

        Returns:
            WebElement: The located element.
        """
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element

    def count_number_of_elements(self, locator):
        """
        Count the number of elements matching the specified XPath locator.

        Args:
            locator (str): The XPath of the elements to count.

        Returns:
            int: The number of elements matching the locator.
        """
        return len(self.driver.find_elements(By.XPATH, locator))

    def wait_until_listing_reloads(self, jobs_selector, expected_quantity=1):
        """
        Wait until the number of elements matching the selector is below or equal to the expected quantity.

        Args:
            jobs_selector (str): The XPath of the elements to count.
            expected_quantity (int, optional): The target number of elements. Defaults to 1.
        """
        attempts_counter = 0
        while (
            self.count_number_of_elements(jobs_selector) > expected_quantity
            and attempts_counter <= 5
        ):
            time.sleep(1)
            attempts_counter += 1

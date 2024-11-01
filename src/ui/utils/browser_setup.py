from selenium import webdriver


def setup_browser(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser not supported")
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

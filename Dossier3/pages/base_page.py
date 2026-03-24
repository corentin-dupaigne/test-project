from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_text_in_element(self, locator: tuple, text: str) -> bool:
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_invisible(self, locator: tuple) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_url_contains(self, fragment: str) -> bool:
        return self.wait.until(EC.url_contains(fragment))

    def wait_for_elements(self, locator: tuple) -> list:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def fill(self, locator: tuple, value: str) -> None:
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator: tuple) -> None:
        self.wait_for_clickable(locator).click()

    def get_text(self, locator: tuple) -> str:
        return self.wait_for_visible(locator).text

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def is_present(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def scroll_to(self, locator: tuple) -> WebElement:
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

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

    # wait for element to be visible
    def wait_for_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    # wait for element to be clickable
    def wait_for_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Wait for a specific text to appear in an element
    def wait_for_text_in_element(self, locator, text: str) -> bool:
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    # wait for an element to disappear
    def wait_for_invisible(self, locator: tuple[str, str]):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # wait for the url to contain a fragment
    def wait_for_url_contains(self, fragment: str) -> bool:
        return self.wait.until(EC.url_contains(fragment))

    # Wait for multiple elements
    def wait_for_elements(self, locator: tuple[str, str]) -> list:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # Fill an input
    def fill(self, locator: tuple, value: str) -> None:
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator: tuple) -> None:
        element = self.wait_for_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        try:
            self.wait_for_clickable(locator).click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].click();", self.wait_for_clickable(locator)
            )

    # Wait for an element to be visible and return its content
    def get_text(self, locator: tuple) -> str:
        return self.wait_for_visible(locator).text

    #
    def is_visible(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def is_present(self, locator: tuple[str, str], timeout: int = 5) -> bool:
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

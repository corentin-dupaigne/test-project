from selenium.webdriver.common.by import By
from pages.base_page import BasePage

ADMIN_URL = "https://automationintesting.online/admin"


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "input#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button#doLogin")

    ERROR_ALERT = (By.CSS_SELECTOR, "div.alert-danger")

    def open(self) -> "AdminLoginPage":
        self.driver.get(ADMIN_URL)
        self.wait_for_visible(self.USERNAME_INPUT)
        return self

    def login(self, username: str, password: str) -> None:
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_ALERT)

    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_ALERT)

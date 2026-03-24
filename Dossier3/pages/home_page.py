from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

BASE_URL = "https://automationintesting.online/"


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "div.hotel-logoUrl img")

    ROOM_CARDS = (By.CSS_SELECTOR, "div.room-card")
    FIRST_BOOK_BUTTON = (By.XPATH, "(//a[contains(text(),'Book now')])[1]")

    BOOKING_FORM = (By.CSS_SELECTOR, "div.room-booking-form")
    CALENDAR_DAYS = (By.CSS_SELECTOR, "div.rbc-day-bg:not(.rbc-off-range-bg)")
    CALENDAR_NEXT_MONTH = (By.CSS_SELECTOR, "button.rbc-btn-group button:last-child")
    BOOKING_FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstname']")
    BOOKING_LASTNAME = (By.CSS_SELECTOR, "input[name='lastname']")
    BOOKING_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    BOOKING_PHONE = (By.CSS_SELECTOR, "input[name='phone']")
    BOOKING_SUBMIT = (By.CSS_SELECTOR, "button#doReservation")
    BOOKING_CANCEL = (By.CSS_SELECTOR, "button.btn-secondary")

    BOOKING_CONFIRMATION = (By.CSS_SELECTOR, "h2.card-title")
    BOOKING_ERROR = (By.CSS_SELECTOR, "div.alert-danger")
    BOOKING_VALIDATION_ERRORS = (By.CSS_SELECTOR, "div.alert.alert-danger p")

    CONTACT_NAME = (By.CSS_SELECTOR, "input#name")
    CONTACT_EMAIL = (By.CSS_SELECTOR, "input#email")
    CONTACT_PHONE = (By.CSS_SELECTOR, "input#phone")
    CONTACT_SUBJECT = (By.CSS_SELECTOR, "input#subject")
    CONTACT_MESSAGE = (By.CSS_SELECTOR, "textarea#description")
    CONTACT_SUBMIT = (By.CSS_SELECTOR, "#contact button.btn-primary")
    CONTACT_SUCCESS = (By.CSS_SELECTOR, "#contact h3")
    CONTACT_VALIDATION_ERRORS = (By.CSS_SELECTOR, "div.alert.alert-danger p")

    def open(self) -> "HomePage":
        self.driver.get(BASE_URL)
        self.wait_for_elements(self.ROOM_CARDS)
        return self

    def fill_contact_form(
        self,
        name: str,
        email: str,
        phone: str,
        subject: str,
        message: str,
    ) -> None:
        self.scroll_to(self.CONTACT_NAME)
        self.fill(self.CONTACT_NAME, name)
        self.fill(self.CONTACT_EMAIL, email)
        self.fill(self.CONTACT_PHONE, phone)
        self.fill(self.CONTACT_SUBJECT, subject)
        self.fill(self.CONTACT_MESSAGE, message)

    def submit_contact_form(self) -> None:
        self.click(self.CONTACT_SUBMIT)

    def get_contact_success_message(self) -> str:
        return self.get_text(self.CONTACT_SUCCESS)

    def get_contact_validation_errors(self) -> list[str]:
        elements = self.wait_for_elements(self.CONTACT_VALIDATION_ERRORS)
        return [el.text for el in elements]

    def is_contact_success_visible(self) -> bool:
        return self.is_visible(self.CONTACT_SUCCESS)

    def is_contact_error_visible(self) -> bool:
        return self.is_present(self.CONTACT_VALIDATION_ERRORS)

    def click_book_first_room(self) -> None:
        self.click(self.FIRST_BOOK_BUTTON)
        self.wait_for_visible(self.BOOKING_FORM)

    def fill_booking_form(
        self,
        firstname: str,
        lastname: str,
        email: str,
        phone: str,
    ) -> None:
        self.fill(self.BOOKING_FIRSTNAME, firstname)
        self.fill(self.BOOKING_LASTNAME, lastname)
        self.fill(self.BOOKING_EMAIL, email)
        self.fill(self.BOOKING_PHONE, phone)

    def submit_booking(self) -> None:
        self.click(self.BOOKING_SUBMIT)

    def cancel_booking(self) -> None:
        self.click(self.BOOKING_CANCEL)
        self.wait_for_invisible(self.BOOKING_FORM)

    def is_booking_confirmation_visible(self) -> bool:
        return self.is_visible(self.BOOKING_CONFIRMATION)

    def get_booking_validation_errors(self) -> list[str]:
        elements = self.wait_for_elements(self.BOOKING_VALIDATION_ERRORS)
        return [el.text for el in elements]

    def select_booking_dates_via_calendar(self) -> None:
        self.wait_for_visible(self.BOOKING_FORM)
        days = self.wait_for_elements(self.CALENDAR_DAYS)

        start_day = days[10]
        end_day = days[12]

        actions = ActionChains(self.driver)
        actions.click_and_hold(start_day).pause(0.3).move_to_element(end_day).release().perform()

    def get_room_count(self) -> int:
        rooms = self.wait_for_elements(self.ROOM_CARDS)
        return len(rooms)

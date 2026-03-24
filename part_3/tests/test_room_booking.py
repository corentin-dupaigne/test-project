import pytest
from pages.home_page import HomePage
from data.test_data import BOOKING_DATA


class TestBookingHappyPath:

    def test_book_button_opens_calendar(self, driver):
        page = HomePage(driver).open()
        assert page.get_room_count() >= 1, "At least one room must exist to test booking."

        page.click_book_first_room()
        assert page.is_visible(HomePage.BOOKING_CALENDAR), (
            "The booking calendar should appear after clicking 'Book this room'."
        )

    def test_cancel_booking_closes_modal(self, driver):
        page = HomePage(driver).open()
        page.click_book_first_room()
        assert page.is_visible(HomePage.BOOKING_CALENDAR)

        page.cancel_booking()
        assert not page.is_visible(HomePage.BOOKING_CALENDAR, timeout=5), (
            "The booking calendar should close after clicking 'Cancel'."
        )

    @pytest.mark.booking_full
    def test_full_booking_with_valid_data_shows_confirmation(self, driver):
        page = HomePage(driver).open()
        page.click_book_first_room()

        page.select_booking_dates_via_calendar()

        data = BOOKING_DATA["valid"]
        page.fill_booking_form(
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
        )
        page.submit_booking()

        assert page.is_booking_confirmation_visible(), (
            "A confirmation message should appear after a valid booking submission."
        )


class TestBookingNegativePath:

    def test_submit_without_dates_shows_validation_error(self, driver):
        page = HomePage(driver).open()
        page.click_book_first_room()

        data = BOOKING_DATA["valid"]
        page.fill_booking_form(
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
        )
        page.submit_booking()

        assert not page.is_booking_confirmation_visible(), (
            "A confirmation should NOT appear without selected dates."
        )
        errors = page.get_booking_validation_errors()
        assert len(errors) >= 1, (
            "At least one validation error should appear when no dates are selected."
        )

    def test_submit_without_firstname_shows_error(self, driver):
        page = HomePage(driver).open()
        page.click_book_first_room()
        page.select_booking_dates_via_calendar()

        data = BOOKING_DATA["missing_firstname"]
        page.fill_booking_form(
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
        )
        page.submit_booking()

        errors = page.get_booking_validation_errors()
        assert len(errors) >= 1, (
            "A validation error should appear when the first name is missing."
        )

    def test_submit_with_invalid_email_shows_error(self, driver):
        page = HomePage(driver).open()
        page.click_book_first_room()
        page.select_booking_dates_via_calendar()

        data = BOOKING_DATA["invalid_email"]
        page.fill_booking_form(
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
        )
        page.submit_booking()

        errors = page.get_booking_validation_errors()
        assert len(errors) >= 1, (
            "A validation error should appear for an invalid email address."
        )

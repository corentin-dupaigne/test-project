import pytest
from pages.home_page import HomePage
from data.test_data import CONTACT_FORM


class TestContactFormHappyPath:

    def test_valid_submission_shows_success(self, driver):
        page = HomePage(driver).open()
        data = CONTACT_FORM["valid"]

        page.fill_contact_form(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            subject=data["subject"],
            message=data["message"],
        )
        page.submit_contact_form()

        assert page.is_contact_success_visible(), (
            "Expected a success banner after valid contact-form submission."
        )
        success_text = page.get_contact_success_message()
        assert data["name"] in success_text or "Thanks" in success_text, (
            f"Success message did not reference the sender's name. Got: '{success_text}'"
        )


class TestContactFormNegativePath:

    def test_missing_name_shows_error(self, driver):
        page = HomePage(driver).open()
        data = CONTACT_FORM["missing_name"]

        page.fill_contact_form(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            subject=data["subject"],
            message=data["message"],
        )
        page.submit_contact_form()

        assert not page.is_contact_success_visible(), (
            "Success banner should NOT appear when the name field is empty."
        )
        assert page.is_contact_error_visible(), (
            "A validation error should be visible when the name field is empty."
        )

    def test_message_too_short_shows_error(self, driver):
        page = HomePage(driver).open()
        data = CONTACT_FORM["short_message"]

        page.fill_contact_form(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            subject=data["subject"],
            message=data["message"],
        )
        page.submit_contact_form()

        assert not page.is_contact_success_visible(), (
            "Success banner should NOT appear when the message is too short."
        )
        assert page.is_contact_error_visible(), (
            "A validation error should be visible for a too-short message."
        )

    def test_invalid_email_shows_error(self, driver):
        page = HomePage(driver).open()
        data = CONTACT_FORM["invalid_email"]

        page.fill_contact_form(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            subject=data["subject"],
            message=data["message"],
        )
        page.submit_contact_form()

        assert not page.is_contact_success_visible(), (
            "Success banner should NOT appear with an invalid email."
        )
        assert page.is_contact_error_visible(), (
            "A validation error should be visible for an invalid email."
        )

    def test_empty_form_shows_multiple_errors(self, driver):
        page = HomePage(driver).open()

        page.fill_contact_form(
            name="", email="", phone="", subject="", message=""
        )
        page.submit_contact_form()

        errors = page.get_contact_validation_errors()
        assert len(errors) >= 1, (
            f"Expected at least one validation error for an empty form, got {len(errors)}."
        )

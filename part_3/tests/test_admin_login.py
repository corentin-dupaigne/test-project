import pytest
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from data.test_data import ADMIN_CREDENTIALS


class TestAdminLoginHappyPath:

    def test_valid_credentials_redirect_to_dashboard(self, driver):
        creds = ADMIN_CREDENTIALS["valid"]
        login_page = AdminLoginPage(driver).open()
        login_page.login(username=creds["username"], password=creds["password"])

        dashboard = AdminDashboardPage(driver)
        assert dashboard.is_logged_in(), (
            "The logout button should be visible after a successful admin login."
        )

    def test_admin_can_logout(self, driver):
        creds = ADMIN_CREDENTIALS["valid"]
        login_page = AdminLoginPage(driver).open()
        login_page.login(username=creds["username"], password=creds["password"])

        dashboard = AdminDashboardPage(driver)
        assert dashboard.is_logged_in()
        dashboard.logout()

        login_page_again = AdminLoginPage(driver)
        assert login_page_again.is_visible(AdminLoginPage.USERNAME_INPUT), (
            "Username field should be visible after logging out."
        )


class TestAdminLoginNegativePath:

    def test_wrong_password_shows_error(self, driver):
        creds = ADMIN_CREDENTIALS["invalid_password"]
        login_page = AdminLoginPage(driver).open()
        login_page.login(username=creds["username"], password=creds["password"])

        assert login_page.is_error_visible(), (
            "An error alert should appear for a wrong password."
        )
        assert login_page.is_visible(AdminLoginPage.USERNAME_INPUT), (
            "The user should remain on the login page after entering a wrong password."
        )

    def test_unknown_user_shows_error(self, driver):
        creds = ADMIN_CREDENTIALS["invalid_user"]
        login_page = AdminLoginPage(driver).open()
        login_page.login(username=creds["username"], password=creds["password"])

        assert login_page.is_error_visible(), (
            "An error alert should appear for an unknown username."
        )

    def test_empty_credentials_shows_error(self, driver):
        creds = ADMIN_CREDENTIALS["empty"]
        login_page = AdminLoginPage(driver).open()
        login_page.login(username=creds["username"], password=creds["password"])

        assert login_page.is_error_visible(), (
            "An error alert should appear when credentials are empty."
        )

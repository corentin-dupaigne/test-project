import pytest
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from data.test_data import ADMIN_CREDENTIALS, ROOM_DATA


@pytest.fixture(autouse=True)
def admin_logged_in(driver):
    creds = ADMIN_CREDENTIALS["valid"]
    AdminLoginPage(driver).open().login(
        username=creds["username"], password=creds["password"]
    )
    return AdminDashboardPage(driver)


class TestAdminRoomsHappyPath:

    def test_create_single_room_appears_in_list(self, driver):
        dashboard = AdminDashboardPage(driver)
        data = ROOM_DATA["valid_single"]

        dashboard.create_room(
            name=data["name"],
            room_type=data["type"],
            accessible=data["accessible"],
            price=data["price"],
        )

        assert dashboard.is_room_present(data["name"]), (
            f"Room '{data['name']}' should be visible in the list after creation."
        )

    def test_create_double_room_with_features(self, driver):
        dashboard = AdminDashboardPage(driver)
        data = ROOM_DATA["valid_double"]

        dashboard.create_room(
            name=data["name"],
            room_type=data["type"],
            accessible=data["accessible"],
            price=data["price"],
            features=data.get("features"),
        )

        assert dashboard.is_room_present(data["name"]), (
            f"Room '{data['name']}' should appear in the list after creation."
        )

    def test_delete_room_removes_it_from_list(self, driver):
        dashboard = AdminDashboardPage(driver)
        data = ROOM_DATA["valid_single"]

        dashboard.create_room(
            name=data["name"],
            room_type=data["type"],
            accessible=data["accessible"],
            price=data["price"],
        )
        count_after_create = dashboard.get_room_count()

        dashboard.delete_room(data["name"])

        count_after_delete = dashboard.get_room_count()
        assert count_after_delete < count_after_create, (
            f"Room count should decrease after deletion (was {count_after_create}, now {count_after_delete})."
        )


class TestAdminRoomsNegativePath:

    def test_create_room_without_price_shows_error(self, driver):
        dashboard = AdminDashboardPage(driver)
        data = ROOM_DATA["missing_price"]
        count_before = dashboard.get_room_count()

        dashboard.create_room(
            name=data["name"],
            room_type=data["type"],
            accessible=data["accessible"],
            price=data["price"],
        )

        count_after = dashboard.get_room_count()
        assert count_after == count_before, (
            "Room count should not increase when the price field is empty."
        )

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):

    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btn-outline-danger")

    ROOM_ROWS = (By.CSS_SELECTOR, "div[data-testid='roomlisting']")
    ROOM_FORM_NAME = (By.CSS_SELECTOR, "input#roomName")
    ROOM_FORM_TYPE = (By.CSS_SELECTOR, "select#type")
    ROOM_FORM_ACCESSIBLE = (By.CSS_SELECTOR, "select#accessible")
    ROOM_FORM_PRICE = (By.CSS_SELECTOR, "input#roomPrice")
    ROOM_FORM_CREATE = (By.CSS_SELECTOR, "button#createRoom")

    AMENITY_WIFI = (By.CSS_SELECTOR, "input#wifiCheckbox")
    AMENITY_TV = (By.CSS_SELECTOR, "input#tvCheckbox")
    AMENITY_RADIO = (By.CSS_SELECTOR, "input#radioCheckbox")
    AMENITY_REFRESHMENTS = (By.CSS_SELECTOR, "input#refreshCheckbox")
    AMENITY_SAFE = (By.CSS_SELECTOR, "input#safeCheckbox")
    AMENITY_VIEWS = (By.CSS_SELECTOR, "input#viewsCheckbox")

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGOUT_BUTTON)

    def logout(self) -> None:
        self.click(self.LOGOUT_BUTTON)

    def create_room(
        self,
        name: str,
        room_type: str,
        accessible: bool,
        price: str,
        features: list[str] | None = None,
    ) -> None:

        self.fill(self.ROOM_FORM_NAME, name)

        Select(self.wait_for_visible(self.ROOM_FORM_TYPE)).select_by_visible_text(room_type)
        Select(self.wait_for_visible(self.ROOM_FORM_ACCESSIBLE)).select_by_visible_text(
            "true" if accessible else "false"
        )

        self.fill(self.ROOM_FORM_PRICE, price)

        if features:
            amenity_map = {
                "WiFi": self.AMENITY_WIFI,
                "TV": self.AMENITY_TV,
                "Radio": self.AMENITY_RADIO,
                "Refreshments": self.AMENITY_REFRESHMENTS,
                "Safe": self.AMENITY_SAFE,
                "Views": self.AMENITY_VIEWS,
            }
            for feature in features:
                locator = amenity_map.get(feature)
                if locator:
                    checkbox = self.wait_for_visible(locator)
                    if not checkbox.is_selected():
                        checkbox.click()

        self.click(self.ROOM_FORM_CREATE)
        self.driver.refresh()
        self.wait_for_elements(self.ROOM_ROWS)

    def delete_room(self, room_name: str) -> None:
        locator = (
            By.XPATH,
            f"//div[@data-testid='roomlisting']"
            f"[.//*[@id='roomName{room_name}']]"
            f"//span[contains(@class,'roomDelete')]",
        )
        self.click(locator)
        self.driver.refresh()
        self.wait_for_elements(self.ROOM_ROWS)

    def get_room_names(self) -> list[str]:
        rows = self.wait_for_elements(self.ROOM_ROWS)
        names = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "p")
            if cells:
                names.append(cells[0].text)
        return names

    def is_room_present(self, room_name: str) -> bool:
        return room_name in self.get_room_names()

    def get_room_count(self) -> int:
        return len(self.wait_for_elements(self.ROOM_ROWS))

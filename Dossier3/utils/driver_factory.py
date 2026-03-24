import os
from selenium import webdriver


def create_driver(browser: str = "chrome", headless: bool = False) -> webdriver.Remote:
    browser = os.environ.get("BROWSER", browser).lower()
    headless = bool(int(os.environ.get("HEADLESS", int(headless))))

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(0)
    driver.maximize_window()
    return driver

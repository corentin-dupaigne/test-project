import pytest
from utils.driver_factory import create_driver

"""
    Opens a browser before each test, gives it to the test, then closes it when the test is done.
"""
@pytest.fixture(scope="function")
def driver():
    d = create_driver()
    yield d
    d.quit()

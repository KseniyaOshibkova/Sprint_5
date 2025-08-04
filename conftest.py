import pytest
from selenium import webdriver

from url import Url
from tests.locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.HOST.value)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=False)
def locators(driver):
    return Locators(driver)

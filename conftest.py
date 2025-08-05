import pytest
from selenium import webdriver

from url import Url
from locators import Locators


@pytest.fixture
def driver():
    # Фикстура создает экземпляр класса для каждого теста, открывает главную страницу, закрывает браузер
    driver = webdriver.Chrome()
    driver.get(Url.HOST.value)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=False)
def locators(driver):
    # Класс обернут в фикстуру для прокидывания ее в параметры тестов
    return Locators(driver)

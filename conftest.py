import pytest
from selenium import webdriver

from data.url import Url
from pages.create_lisiting_page.create_lisiting_page import CreateLisiningPage
from pages.login_page.login_page import LoginPage
from pages.profile_page.profile_page import ProfilePage


@pytest.fixture
def driver():
    # Фикстура создает экземпляр класса для каждого теста, открывает главную страницу, закрывает браузер
    driver = webdriver.Chrome()
    driver.get(Url.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function', autouse=False)
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope='function', autouse=False)
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture(scope='function', autouse=False)
def create_lisiting_page(driver):
    return CreateLisiningPage(driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string

from selenium.webdriver.support.wait import WebDriverWait

from url import Url


class Locators:
    def __init__(self, driver):
        self.driver = driver

        self.login_and_registration_button = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
        self.no_account_button = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
        self.email_input = (By.CSS_SELECTOR, "input[name='email'].input_inputStandart__JweLZ")
        self.password_input = (By.CSS_SELECTOR, "input[name='password'].input_inputStandart__JweLZ")
        self.repeat_password_input = (By.CSS_SELECTOR, "input[name='submitPassword'].input_inputStandart__JweLZ")
        self.create_account_button = (By.XPATH, "//button[text()='Создать аккаунт']")
        self.post_advertisement_button = (By.XPATH, "//button[text()='Разместить объявление']")
        self.authorized_user_avatar = (By.CSS_SELECTOR, "svg.svgSmall")
        self.authorized_user_name = (By.XPATH, "//h3[@class='profileText name']")
        self.regisration_error = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")

    @staticmethod
    def generate_email():
        """Генерирует email"""
        return f"test{random.randint(1000000, 9999999)}@example.com"

    def fill_generate_email(self):
        """Заполняет поле email сгенерированным значением"""
        self.fill_input(self.email_input, self.generate_email())

    def click_element(self, locator):
        """Кликает по элементу"""
        self.driver.find_element(*locator).click()

    def fill_input(self, locator, value):
        """Заполняет поле ввода"""
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def fill_inputs(self, locators_and_values):
        """Заполняет несколько полей ввода"""
        for locator, value in locators_and_values:
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(value)

    def fill_password_fields(self, password, repeat_password):
        """Заполняет поля паролей"""
        self.fill_input(self.password_input, password)
        self.fill_input(self.repeat_password_input, repeat_password)

    def check_current_url_under_authorized_user(self):
        """Проверяет переход на главную страницу, отображение аватара и имени пользователя"""
        assert self.driver.current_url == Url.HOST.value

    def check_displayed_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        assert element.is_displayed()

    def check_text(self, locator, value):
        actual = self.driver.find_element(*locator).text
        assert actual == value.value

    def fields_highlighted_red(self, field_locators, expected_hex_color):
        """Проверяет, что все указанные поля имеют заданный цвет рамки"""
        for locator in field_locators:
            element = self.driver.find_element(*locator)
            border_value = element.value_of_css_property("border")
            assert expected_hex_color.lower() in border_value.lower()

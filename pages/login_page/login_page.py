from selenium.webdriver.common.by import By

from data.url import Url
from helpers.helpers import Helpers
from pages.base_page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.login_button = (By.XPATH, "//button[contains(@class, 'button') and .='Войти']")
        self.logout_button = (By.XPATH, "//button[contains(text(), 'Выйти')]")
        self.no_account_button = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
        self.email_input = (By.CSS_SELECTOR, "input.input_inputStandart__JweLZ[name='email']")
        self.password_input = (By.CSS_SELECTOR, "input[name='password'].input_inputStandart__JweLZ")
        self.repeat_password_input = (By.CSS_SELECTOR, "input[name='submitPassword'].input_inputStandart__JweLZ")
        self.create_account_button = (By.XPATH, "//button[text()='Создать аккаунт']")
        self.modal_window_authorize = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")
        self.parent_element = (By.XPATH, "./..")
        self.pls_login_title = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
        self.login_and_registration_button = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
        self.warning_error = (By.XPATH, "//span[contains(@class, 'input_span__yWPqB') and text()='Ошибка']")

    def fill_generate_email(self):
        """Заполняет поле email сгенерированным значением"""
        self.fill_input(self.email_input, Helpers.generate_email())
        return Helpers.generate_email()

    def fields_highlighted_red(self, field_locators, expected_hex_color):
        """Проверяет, что все указанные поля имеют заданный цвет рамки"""
        self.waiting_for_element(self.warning_error)
        # Конвертировать HEX в RGB
        expected_rgb = (f"rgb({int(expected_hex_color[0:2], 16)}, {int(expected_hex_color[2:4], 16)}, "
                        f"{int(expected_hex_color[4:6], 16)})")
        # Проверить, что у всех переданных элементов цвет совпадает с ожидаемым
        for locator in field_locators:
            elements = self.find_elements(locator)
            for element in elements:
                # Получить родительский div
                parent = element.find_element(*self.parent_element)
                actual_color = parent.value_of_css_property("border-color")
                # Сравнить заданный цвет с полученным
                assert expected_rgb == actual_color

    def user_login(self, email, password):
        """Авторизация пользователя"""
        self.click_element(self.login_and_registration_button)
        # Заполнить поля Email и Password
        self.fill_inputs([
            (self.email_input, email),
            (self.password_input, password)])
        # Кликнуть по кнопке "Войти"
        self.click_element(self.login_button)

    def user_logout(self):
        """Выходит из аккаунта пользователя"""
        self.click_element(self.logout_button)

    def open_registration_form(self):
        """Открывает форму регистрации"""
        self.click_element(self.login_and_registration_button)
        self.click_element(self.no_account_button)

    def fill_registration_form_and_create_acc(self, email, password, repeat_password):
        """Заполяет форму регистрации и кликает создать аккаунт"""
        self.fill_inputs([
            (self.email_input, email),
            (self.password_input, password),
            (self.repeat_password_input, repeat_password)])
        self.click_element(self.create_account_button)

    def check_text_error_in_modal_window(self, expected_text):
        """Проверяет наличие текста Ошибка в модальном окне регистрации"""
        self.check_text(self.modal_window_authorize, expected_text)

    def fields_autorize_highlighted_red(self, color):
        """Проверяет подсветку полей email, password, repeat password"""
        self.fields_highlighted_red([
            self.email_input, self.password_input, self.repeat_password_input], color)

    def check_display_title_in_modal_window_create(self):
        """Проверяет отображение заголовка 'Чтобы разместить объявление, авторизуйтесь' в модальном окне"""
        self.check_display_title_in_modal_window(self.modal_window_authorize, self.pls_login_title)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

from selenium.webdriver.support.wait import WebDriverWait

from url import Url


class Locators:
    def __init__(self, driver):
        self.driver = driver

        self.login_and_registration_button = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
        self.no_account_button = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
        self.email_input = (By.CSS_SELECTOR, "input.input_inputStandart__JweLZ[name='email']")
        self.password_input = (By.CSS_SELECTOR, "input[name='password'].input_inputStandart__JweLZ")
        self.repeat_password_input = (By.CSS_SELECTOR, "input[name='submitPassword'].input_inputStandart__JweLZ")
        self.create_account_button = (By.XPATH, "//button[text()='Создать аккаунт']")
        self.authorized_user_avatar = (By.CSS_SELECTOR, "svg.svgSmall")
        self.authorized_user_name = (By.XPATH, "//h3[@class='profileText name']")
        self.registration_error = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
        self.login_button = (By.XPATH, "//button[contains(@class, 'button') and .='Войти']")
        self.logout_button = (By.XPATH, "//button[contains(text(), 'Выйти')]")
        self.modal_window_authorize = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")
        self.post_advertisement_button = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and normalize-space()="
                                                    "'Разместить объявление']")
        self.title_ad_input = (By.CSS_SELECTOR, "input[name='name']")
        self.product_description_nput = (By.XPATH, "//textarea[@name='description']")
        self.product_price_input = (By.XPATH, "//input[@name='price']")
        self.drop_down_list_cities = (By.CSS_SELECTOR, "input[name='city'][readonly]")
        self.drop_down_product_category= (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw")
        self.by_state_radiobutton = (By.XPATH, "//label[text()='Б/У']/preceding-sibling::div[contains(@class, "
                                               "'radioUnput_inputRegular__FbVbr')]")
        self.publish_ad_button = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and normalize-space()="
                                            "'Опубликовать']")
        self.select_dropdown_cities_button = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, "
                                                 "'dropDownMenu_arrow')]")
        self.select_dropdown_category_button = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw > "
                                                                 "button.dropDownMenu_arrowDown__pfGL1")


    @staticmethod
    def generate_email():
        """Генерирует email"""
        return f"test{random.randint(1000000, 9999999)}@example.com"

    def fill_generate_email(self):
        """Заполняет поле email сгенерированным значением"""
        self.fill_input(self.email_input, self.generate_email())

    def click_element(self, locator):
        """Кликает по элементу"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        element.click()

    def fill_input(self, locator, value):
        """Заполняет поле ввода"""
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def fill_inputs(self, locators_and_values):
        """Заполняет поля ввода переданные в списке"""
        for locator, value in locators_and_values:
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(value)

    def check_current_url_under_authorized_user(self):
        """Проверяет переход на главную страницу"""
        assert self.driver.current_url == Url.HOST.value

    def check_displayed_element(self, locator):
        """Проверяет отображение элемента"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        assert element.is_displayed()

    def check_not_displayed_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))
        assert element

    def check_text(self, locator, value):
        """Проверяет соответствие полученного текста из элемента с константой"""
        actual = self.driver.find_element(*locator).text
        assert actual == value.value

    def fields_highlighted_red(self, field_locators, expected_hex_color):
        """Проверяет, что все указанные поля имеют заданный цвет рамки"""
        # Конвертировать HEX в RGB
        expected_rgb = (f"rgb({int(expected_hex_color[0:2], 16)}, {int(expected_hex_color[2:4], 16)}, "
                        f"{int(expected_hex_color[4:6], 16)})")
        # Проверить, что у всех переданных элементов цвет совпадает с ожидаемым
        for locator in field_locators:
            element = self.driver.find_element(*locator)
            # Получить родительский div
            parent = element.find_element(By.XPATH, "./..")
            actual_color = parent.value_of_css_property("border-color")
            # Сравнить заданный цвет с полученным
            assert expected_rgb == actual_color

    def test_check_display_title_in_modal_window(self, window_locator, title_text):
        """Проверяет отображение заголовка в модальном окне"""
        # Найти модальное окно
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(window_locator))
        # Найти заголовок внутри окна
        title = modal.find_element(
            By.XPATH, f".//*[contains(text(), '{title_text}')]")
        # Проверить видимость заголовка
        assert title.is_displayed()


    def select_drop_down_list_item(self, trigger_button, dropdown_options_locator, option_text):
        """Открывает выпадающий список и кликает по значению списка"""
        # Кликнуть по кнопке открытия списка
        self.click_element(trigger_button)
        # Ожидать появления вариантов списка
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(dropdown_options_locator))
        # Сформировать локатор элемента списка и кликнуть по нему
        option_locator = (By.XPATH,
        f"//div[@class='dropDownMenu_options__CmHmm']"  # контейнер списка
        f"//button[.//span[normalize-space()='{option_text}']]")  # кнопка с нужным текстом
        self.click_element(option_locator)

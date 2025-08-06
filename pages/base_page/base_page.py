from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.url import Url


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, timeout=5):
        """Кликает по элементу"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        element.click()
        return self

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
        return self.driver.current_url == Url.BASE_URL

    def check_displayed_element(self, locator):
        """Проверяет отображение элемента"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def check_not_displayed_element(self, locator):
        """Проверяет, что элемент не отображается"""
        element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))
        return element

    def check_text(self, locator, value):
        """Проверяет соответствие полученного текста из элемента с константой"""
        actual = self.driver.find_element(*locator).text
        return actual == value.value

    def check_display_title_in_modal_window(self, window_locator, title_locator):
        """Проверяет отображение заголовка в модальном окне"""
        # Найти модальное окно
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(window_locator))
        # Найти заголовок внутри окна
        title = modal.find_element(*title_locator)
        # Проверить видимость заголовка
        return title.is_displayed()

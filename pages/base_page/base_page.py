from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.dropdown_item_template = ("xpath", ".//*[contains(text(), '{}')]")

    def waiting_for_element(self, locator):
        """Ожидает заданный элемент"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return element

    def waiting_for_url(self, expected_url):
        """Ожидает заданный url"""
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url))

    def find_elements(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_elements(by, value)

    def find_element(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_element(by, value)

    def scroll_for_element(self, element):
        """Скролит до элемиента"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, locator, timeout=5, retries=3):
        """Кликает по элементу"""
        for attempt in range(retries):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise

    def fill_input(self, locator, value):
        """Заполняет поле ввода"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def fill_inputs(self, locators_and_values):
        """Заполняет поля ввода переданные в списке"""
        for locator, value in locators_and_values:
            self.fill_input(locator, value)

    def check_current_url_under_authorized_user(self, url):
        """Проверяет переход на главную страницу"""
        return self.driver.current_url == url

    def check_displayed_element(self, locator):
        """Проверяет отображение элемента"""
        element = self.waiting_for_element(locator)
        return element.is_displayed()

    def check_not_displayed_element(self, locator):
        """Проверяет, что элемент не отображается"""
        element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))
        return element

    def check_text(self, locator, expected_text):
        """Проверяет соответствие полученного текста из элемента с константой"""
        actual = self.find_element(locator).text
        return actual == expected_text

    def check_display_title_in_modal_window(self, window_locator, title_locator):
        """Проверяет отображение заголовка в модальном окне"""
        # Найти модальное окно
        modal = self.waiting_for_element(window_locator)
        # Найти заголовок внутри окна
        title = modal.find_element(*title_locator)
        # Проверить видимость заголовка
        return title.is_displayed()

    def select_drop_down_list_item(self, trigger_button, dropdown_locator, item_text):
        """Открывает выпадающий список и кликает по значению списка"""
        # Кликнуть по кнопке открытия списка
        self.click_element(trigger_button)
        # Ожидать появления вариантов списка
        self.waiting_for_element(dropdown_locator)
        # Сформировать локатор элемента списка и кликнуть по нему
        locator = (self.dropdown_item_template[0],
                   self.dropdown_item_template[1].format(item_text))
        self.click_element(locator)

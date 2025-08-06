from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from pages.base_page.base_page import BasePage


class CreateLisiningPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_drop_down_list_item(self, trigger_button, dropdown_options_locator, option_text):
        """Открывает выпадающий список и кликает по значению списка"""
        # Кликнуть по кнопке открытия списка
        self.click_element(trigger_button)
        # Ожидать появления вариантов списка
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(dropdown_options_locator))
        # Сформировать локатор элемента списка и кликнуть по нему
        option_locator = Locators.BUTTON_IN_LIST_CONTAINER  # кнопка с нужным текстом в списке
        self.click_element(option_locator)

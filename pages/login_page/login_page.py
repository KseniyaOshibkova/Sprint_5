from helpers.helpers import Helpers
from pages.base_page.base_page import BasePage
from locators.locators import Locators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_generate_email(self):
        """Заполняет поле email сгенерированным значением"""
        self.fill_input(Locators.EMAIL_INPUT, Helpers.generate_email())

    def fields_highlighted_red(self, field_locators, expected_hex_color):
        """Проверяет, что все указанные поля имеют заданный цвет рамки"""
        # Конвертировать HEX в RGB
        expected_rgb = (f"rgb({int(expected_hex_color[0:2], 16)}, {int(expected_hex_color[2:4], 16)}, "
                        f"{int(expected_hex_color[4:6], 16)})")
        # Проверить, что у всех переданных элементов цвет совпадает с ожидаемым
        for locator in field_locators:
            element = self.driver.find_element(*locator)
            # Получить родительский div
            parent = element.find_element(Locators.PARENT_ELEMENT)
            actual_color = parent.value_of_css_property("border-color")
            # Сравнить заданный цвет с полученным
            assert expected_rgb == actual_color

from selenium.webdriver.common.by import By
from data.url import Url
from data.data_create_ad import DataForAdTests
from pages.base_page.base_page import BasePage


class CreateLisiningPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.post_advertisement_button = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and normalize-space()="
                                                    "'Разместить объявление']")
        self.title_ad_input = (By.CSS_SELECTOR, "input[name='name']")
        self.product_description_input = (By.XPATH, "//textarea[@name='description']")
        self.product_price_input = (By.XPATH, "//input[@name='price']")
        self.drop_down_list_cities = (By.CSS_SELECTOR, "input[name='city'][readonly]")
        self.drop_down_product_category = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw")
        self.publish_ad_button = (By.XPATH,
                             "//button[contains(@class, 'buttonPrimary') and normalize-space()='Опубликовать']")
        self.select_dropdown_cities_button = (By.XPATH, "//input[@name='city']/following-sibling::button[contains"
                                                        "(@class, ""'dropDownMenu_arrow')]")
        self.select_dropdown_category_button = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw > "
                                                            "button.dropDownMenu_arrowDown__pfGL1")
        self.button_in_list_container = (By.XPATH, f"//div[@class='dropDownMenu_options__CmHmm']//button"
                                              "[.//span[normalize-space()='{option_text}']]")

    def select_drop_down_list_item_cities(self, city_name):
        """Открывает выпадающий список городов и кликает по значению списка"""
        self.select_drop_down_list_item(
            trigger_button=self.select_dropdown_cities_button,
            dropdown_locator=self.drop_down_list_cities,
            item_text=city_name)

    def select_drop_down_list_item_category(self, category_text):
        """Открывает выпадающий список категорий и кликает по значению списка"""
        self.select_drop_down_list_item(
            trigger_button=self.select_dropdown_category_button,
            dropdown_locator=self.drop_down_product_category,
            item_text=category_text)

    def  open_post_advertisement(self):
        """Открывает форму размещения объявления"""
        self.click_element(self.post_advertisement_button)

    def fill_inputs_create_lisiting(self, title, description, price):
        """Заполняет поля «Название», «Описание товара» и «Стоимость»"""
        self.fill_inputs([
            (self.title_ad_input, title),
            (self.product_description_input, description),
            (self.product_price_input, price)])

    def select_item_condition(self, condition_text):
        """Выбирает состояние товара"""
        locator = (self.dropdown_item_template[0],
                   self.dropdown_item_template[1].format(condition_text))
        self.click_element(locator)

    def create_and_public_ad(self):
        """Размещает объявление с заданными параметрами"""
        # Кликнуть по кнопке "Разместить объявление"
        self.open_post_advertisement()
        # Заполнить поля «Название», «Описание товара» и «Стоимость»
        self.fill_inputs_create_lisiting(
            title=DataForAdTests.AD_TITLE.value,
            description=DataForAdTests.PRODUCT_DESCRIPTION.value,
            price=DataForAdTests.PRODUCT_PRICE.value)
        # Выбрать Город
        self.select_drop_down_list_item_cities(
            city_name=DataForAdTests.SPB_CITIES.value)
        # Выбрать категорию
        self.select_drop_down_list_item_category(
            category_text=DataForAdTests.BOOKS_CATEGORY.value)
        # Выбрать «Состояние товара»
        self.select_item_condition(
            condition_text=DataForAdTests.BY.value)
        # Нажать кнопку «Опубликовать»
        self.click_element(
            self.publish_ad_button)

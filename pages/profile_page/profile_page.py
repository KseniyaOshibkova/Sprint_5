from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.url import Url
from locators.locators import Locators
from pages.base_page.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_last_advertisement(self, expected_title):
        """Проверяет последнее поданное объявление в личном профиле"""
        # Дождаться загрузки страницы профиля
        WebDriverWait(self.driver, 15).until(
            EC.url_to_be(Url.PROFILE_PAGE))
        # Получить все объявления
        all_ads = self.driver.find_elements(Locators.ALL_AD)

        # Проскролить к последнему объявлению
        last_ad = all_ads[-1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", last_ad)

        # Получить заголовок
        title_element = last_ad.find_element(Locators.LAST_AD)
        actual_title = title_element.text

        # Проверить соответствие заголовков
        assert actual_title == expected_title

from selenium.webdriver.common.by import By
from data.url import Url
from pages.base_page.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.authorized_user_avatar = (By.XPATH, "//button[contains(@class, 'circleSmall')]")
        self.authorized_user_name = (By.XPATH, "//h3[@class='profileText name']")
        self.all_ad = (By.CSS_SELECTOR, "div.card")
        self.last_ad = (By.CLASS_NAME, "h2")
        self.accept_button = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(., 'Применить')]")

    def verify_last_advertisement(self, expected_title):
        """Проверяет последнее поданное объявление в личном профиле"""
        self.waiting_for_element(self.accept_button)
        # Перейти в профиль пользователя
        self.click_element(self.authorized_user_avatar)
        # Дождаться загрузки страницы профиля
        self.waiting_for_url(Url.PROFILE_PAGE)
        # Получить все объявления
        all_ads = self.find_elements(self.all_ad)
        # Проскролить к последнему объявлению
        last_ad = all_ads[-1]
        self.scroll_for_element(last_ad)
        # Получить заголовок
        title_element = last_ad.find_element(*self.last_ad)
        actual_title = title_element.text

        # Проверить соответствие заголовков
        assert actual_title == expected_title

    def check_name_authorized_user(self, expected_text):
        """Проверяет имя авторизованного пользователя"""
        actual = self.find_element(self.authorized_user_name)
        return actual == expected_text

    def check_displayed_avatar(self):
        """Проверяет отображение аватара авторизованного пользователя"""
        element = self.waiting_for_element(self.authorized_user_avatar)
        return element.is_displayed()

    def check_not_displayed_avatar(self):
        """Проверяет что аватар авторизованного пользователя не отображается"""
        element = self.waiting_for_element(self.authorized_user_avatar)
        return not element.is_displayed()

    def check_not_displayed_user_name(self):
        """Проверяет что имя авторизованного пользователя не отображается"""
        self.check_not_displayed_element(self.authorized_user_name)

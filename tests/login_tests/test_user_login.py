from data.data_for_all_tests import DataForAllTests
from locators.locators import Locators


def test_user_login(driver, login_page):
    # Открыть форму регистрации
    login_page.click_element(Locators.LOGIN_AND_REGISTRATION_BUTTON)
    # Заполнить поля Email и Password
    login_page.fill_inputs([
        (Locators.EMAIL_INPUT, DataForAllTests.REPEAT_LOGIN.value),
        (Locators.PASSWORD_INPUT, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Войти"
    login_page.click_element(Locators.LOGIN_BUTTON)

    # Проверить отображение аватара авторизованного пользователя
    login_page.check_displayed_element(Locators.AUTHORIZED_USER_AVATAR)
    # Проверить имя авторизованного пользователя
    login_page.check_text(
        Locators.AUTHORIZED_USER_NAME, DataForAllTests.USER)
    # Проверить текущий url
    login_page.check_current_url_under_authorized_user()

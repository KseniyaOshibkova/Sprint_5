from data.data_for_all_tests import DataForAllTests
from locators.locators import Locators



def test_user_registration(driver, login_page, profile_page):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    login_page.click_element(Locators.LOGIN_AND_REGISTRATION_BUTTON)
    login_page.click_element(Locators.NO_ACCOUNT_BUTTON)
    # Заполнить поля Email и Password уже зарегистрированными данными
    login_page.fill_generate_email()
    login_page.fill_inputs([
        (Locators.PASSWORD_INPUT, DataForAllTests.PASSWORD.value),
        (Locators.REPEAT_PASSWORD_INPUT, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Создать аккаунт"
    login_page.click_element(Locators.CREATE_ACCOUNT_BUTTON)

    # Проверить отображение аватара авторизованного пользователя
    profile_page.check_displayed_element(Locators.AUTHORIZED_USER_AVATAR)
    # Проверить имя авторизованного пользователя
    profile_page.check_text(
        Locators.AUTHORIZED_USER_NAME, DataForAllTests.USER)
    # Проверить текущий url
    profile_page.check_current_url_under_authorized_user()

from data.data_for_all_tests import DataForAllTests
from locators.locators import Locators


def test_registering_existing_user(driver, login_page):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    login_page.click_element(Locators.LOGIN_AND_REGISTRATION_BUTTON)
    login_page.click_element(Locators.NO_ACCOUNT_BUTTON)
    # Заполнить поля Email и Password уже зарегистрированными данными
    login_page.fill_input(
        Locators.EMAIL_INPUT,
        DataForAllTests.REPEAT_LOGIN.value)
    login_page.fill_inputs([
        (Locators.PASSWORD_INPUT, DataForAllTests.PASSWORD.value),
        (Locators.REPEAT_PASSWORD_INPUT, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Создать аккаунт"
    login_page.click_element(Locators.CREATE_ACCOUNT_BUTTON)

    # Проверить отображение текста "Ошибка"
    login_page.check_displayed_element(Locators.REGISTRATION_ERROR)
    # Проверить, что поля Email, Пароль и Повторите пароль выделены красным
    login_page.fields_highlighted_red(
        [Locators.EMAIL_INPUT,
         Locators.PASSWORD_INPUT,
         Locators.REPEAT_PASSWORD_INPUT],
        DataForAllTests.RED_COLOR.value)

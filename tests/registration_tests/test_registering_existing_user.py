import time

from data.data_for_all_tests import DataForAllTests


def test_registering_existing_user(driver, locators):
    # Открывает форму регистрации и кликает "Нет аккаунта"
    locators.click_element(locators.login_and_registration_button)
    locators.click_element(locators.no_account_button)
    # Заполнение полей email и password уже зарегистрированными данными
    locators.fill_input(
        locator=locators.email_input,
        value=DataForAllTests.REPEAT_LOGIN.value)
    locators.fill_inputs([
        (locators.password_input, DataForAllTests.PASSWORD.value),
        (locators.repeat_password_input, DataForAllTests.PASSWORD.value)])
    # Клик по кнопке создания аккаунта
    locators.click_element(locators.create_account_button)

    # Проверка отображения текста "Ошибка"
    locators.check_displayed_element(locators.registration_error)
    # Проверка поля Email, Пароль и Повторите пароль выделены красным
    locators.fields_highlighted_red(
        [locators.email_input,
         locators.password_input,
         locators.repeat_password_input],
        DataForAllTests.RED_COLOR.value)

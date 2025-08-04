from data.data_for_all_tests import DataForAllTests



def test_user_logout(driver, locators):
    # Открыть форму регистрации
    locators.click_element(locators.login_and_registration_button)
    # Заполнить поля Email и Password
    locators.fill_inputs([
        (locators.email_input, DataForAllTests.REPEAT_LOGIN.value),
        (locators.password_input, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Войти"
    locators.click_element(locators.login_button)
    # Кликнуть по кнопке "Выйти"
    locators.click_element(locators.logout_button)

    # Проверить, что аватара авторизованного пользователя больше не отображается
    locators.check_not_displayed_element(locators.authorized_user_avatar)
    # Проверить, имя авторизованного пользователя больше не отображается
    locators.check_not_displayed_element(locators.authorized_user_name)

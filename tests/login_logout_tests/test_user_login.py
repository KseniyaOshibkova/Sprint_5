from data.data_for_all_tests import DataForAllTests



def test_user_login(driver, locators):
    # Открыть форму регистрации
    locators.click_element(locators.login_and_registration_button)
    # Заполнить поля Email и Password
    locators.fill_inputs([
        (locators.email_input, DataForAllTests.REPEAT_LOGIN.value),
        (locators.password_input, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Войти"
    locators.click_element(locators.login_button)

    # Проверить отображение аватара авторизованного пользователя
    locators.check_displayed_element(locators.authorized_user_avatar)
    # Проверить имя авторизованного пользователя
    locators.check_text(
        locators.authorized_user_name, DataForAllTests.USER)
    # Проверить текущий url
    locators.check_current_url_under_authorized_user()

from data.data_for_all_tests import DataForAllTests


def test_user_registration(driver, locators):
    # Открывает форму регистрации и кликает "нет аккаунта"
    locators.click_element(locators.login_and_registration_button)
    locators.click_element(locators.no_account_button)
    # Заполнение полей
    locators.fill_generate_email()
    locators.fill_inputs([
        (locators.password_input, DataForAllTests.PASSWORD.value),
        (locators.repeat_password_input, DataForAllTests.PASSWORD.value)])
    # Клик по кнопке создания аккаунта
    locators.click_element(locators.create_account_button)

    # Проверка отображения аватара авторизованного пользователя
    locators.check_displayed_element(locators.authorized_user_avatar)
    # Проверка имени авторизованного пользователя
    locators.check_text(
        locators.authorized_user_name, DataForAllTests.USER)
    # Проверка текущего url
    locators.check_current_url_under_authorized_user()

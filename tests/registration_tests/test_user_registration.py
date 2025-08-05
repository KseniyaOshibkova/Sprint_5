from data.data_for_all_tests import DataForAllTests


def test_user_registration(locators):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    locators.click_element(locators.login_and_registration_button)
    locators.click_element(locators.no_account_button)
    # Заполнить поля Email, Пароль и Повторите пароль
    locators.fill_generate_email()
    locators.fill_inputs([
        (locators.password_input, DataForAllTests.PASSWORD.value),
        (locators.repeat_password_input, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Создать аккаунт"
    locators.click_element(locators.create_account_button)

    # Проверить отображение аватара авторизованного пользователя
    locators.check_displayed_element(locators.authorized_user_avatar)
    # Проверить имя авторизованного пользователя
    locators.check_text(
        locators.authorized_user_name, DataForAllTests.USER)
    # Проверить текущий url
    locators.check_current_url_under_authorized_user()

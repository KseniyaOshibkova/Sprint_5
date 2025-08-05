from data.data_for_all_tests import DataForAllTests



def test_user_registration_with_email_not_by_mask(locators):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    locators.click_element(locators.login_and_registration_button)
    locators.click_element(locators.no_account_button)
    # Заполнить поля Email и Password не по маске
    locators.fill_input(
        locator=locators.email_input,
        value=DataForAllTests.NO_MASK_LOGIN.value)
    locators.fill_inputs([
        (locators.password_input, DataForAllTests.PASSWORD.value),
        (locators.repeat_password_input, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Создать аккаунт"
    locators.click_element(locators.create_account_button)

    # Проверить отображение текста "Ошибка"
    locators.check_displayed_element(locators.registration_error)
    # Проверить, что поля Email, Пароль и Повторите пароль выделены красным
    locators.fields_highlighted_red(
        [locators.email_input,
         locators.password_input,
         locators.repeat_password_input],
        DataForAllTests.RED_COLOR.value)
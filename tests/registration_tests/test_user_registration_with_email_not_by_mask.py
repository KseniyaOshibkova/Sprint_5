from data.data_login import DataForLoginTests



def test_user_registration_with_email_not_by_mask(driver, login_page):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    login_page.open_registration_form()
    # Заполнить поля Email, Password и Repeat password не по маске и нажать создать аккаунт
    login_page.fill_registration_form_and_create_acc(
        email=DataForLoginTests.NO_MASK_LOGIN.value,
        password=DataForLoginTests.PASSWORD.value,
        repeat_password=DataForLoginTests.PASSWORD.value)


    # Проверить отображение текста "Ошибка"
    login_page.check_text_error_in_modal_window(
        expected_text=DataForLoginTests.ERROR.value)
    # Проверить, что поля Email, Пароль и Повторите пароль выделены красным
    login_page.fields_autorize_highlighted_red(
        color=DataForLoginTests.RED_COLOR.value)

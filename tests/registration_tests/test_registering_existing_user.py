from data.data_login import DataForLoginTests


def test_registering_existing_user(driver, login_page):
    # Открыть форму регистрации
    login_page.open_registration_form()
    # Заполнить поля Email, Password и Repeat password уже зарегистрированными данными и нажать создать аккаунт
    login_page.fill_registration_form_and_create_acc(
        email=DataForLoginTests.REPEAT_LOGIN.value,
        password=DataForLoginTests.PASSWORD.value,
        repeat_password=DataForLoginTests.PASSWORD.value)

    # Проверить отображение текста "Ошибка"
    login_page.check_text_error_in_modal_window(
        expected_text=DataForLoginTests.ERROR.value)
    # Проверить, что поля Email, Пароль и Повторите пароль выделены красным
    login_page.fields_autorize_highlighted_red(
        color=DataForLoginTests.RED_COLOR.value)

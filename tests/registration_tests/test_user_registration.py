from data.data_login import DataForLoginTests
from data.url import Url


def test_user_registration(driver, login_page, profile_page):
    # Открыть форму регистрации и кликнуть "Нет аккаунта"
    login_page.open_registration_form()
    # Заполнить поля Email, Password  и Repeat password и нажать создать аккаунт
    login_page.fill_registration_form_and_create_acc(
        email=login_page.fill_generate_email(),
        password=DataForLoginTests.PASSWORD.value,
        repeat_password=DataForLoginTests.PASSWORD.value)

    # Проверить отображение аватара авторизованного пользователя
    profile_page.check_displayed_avatar()
    # Проверить имя авторизованного пользователя
    profile_page.check_name_authorized_user(
        expected_text=DataForLoginTests.USER.value)
    # Проверить текущий url
    profile_page.check_current_url_under_authorized_user(
        url=Url.BASE_URL)

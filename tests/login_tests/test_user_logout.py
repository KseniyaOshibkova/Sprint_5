from data.data_login import DataForLoginTests


def test_user_logout(driver, login_page, profile_page):
    # Авторизоваться
    login_page.user_login(
        email=DataForLoginTests.REPEAT_LOGIN.value,
        password=DataForLoginTests.PASSWORD.value)
    # Кликнуть по кнопке "Выйти"
    login_page.user_logout()

    # Проверить, что аватара авторизованного пользователя больше не отображается
    profile_page.check_not_displayed_avatar()
    # Проверить, имя авторизованного пользователя больше не отображается
    profile_page.check_not_displayed_user_name()

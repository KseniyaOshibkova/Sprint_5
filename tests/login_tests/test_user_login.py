from data.data_login import DataForLoginTests
from data.url import Url


def test_user_login(driver, login_page, profile_page):
    # Авторизоваться
    login_page.user_login(
        email=DataForLoginTests.REPEAT_LOGIN.value,
        password=DataForLoginTests.PASSWORD.value)

    # Проверить отображение аватара авторизованного пользователя
    profile_page.check_displayed_avatar()
    # Проверить имя авторизованного пользователя
    profile_page.check_name_authorized_user(
        expected_text=DataForLoginTests.USER.value)
    # Проверить текущий url
    login_page.check_current_url_under_authorized_user(
        url=Url.BASE_URL)

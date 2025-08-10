from data.data_create_ad import DataForAdTests
from data.data_login import DataForLoginTests


def test_creation_ad_authorized_user(driver, login_page,create_lisiting_page, profile_page):
    # Авторизоваться
    login_page.user_login(
        email=DataForLoginTests.REPEAT_LOGIN.value,
        password=DataForLoginTests.PASSWORD.value)
    # Разместить объявление
    create_lisiting_page.create_and_public_ad()

   # Проверить, что в блоке «Мои объявления» отображается созданное объявление
    profile_page.verify_last_advertisement(
        expected_title=DataForAdTests.AD_TITLE.value)

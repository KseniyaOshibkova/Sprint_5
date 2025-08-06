from data.data_for_all_tests import DataForAllTests
from locators.locators import Locators


def test_creation_ad_authorized_user(driver, login_page,create_lisiting_page):
    # Открыть форму регистрации
    login_page.click_element(
        Locators.LOGIN_AND_REGISTRATION_BUTTON)
    # Заполнить поля Email и Password
    login_page.fill_inputs([
        (Locators.EMAIL_INPUT, DataForAllTests.REPEAT_LOGIN.value),
        (Locators.PASSWORD_INPUT, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Войти"
    login_page.click_element(
        Locators.LOGIN_BUTTON)
    # Кликнуть по кнопке "Разместить объявление"
    login_page.click_element(Locators.POST_ADVERTISEMENT_BUTTON)
    # Заполнить поля «Название», «Описание товара» и «Стоимость»
    create_lisiting_page.fill_inputs([
        (Locators.TITLE_AD_INPUT, DataForAllTests.AD_TITLE.value),
        (Locators.PRODUCT_DESCRIPTION_INPUT, DataForAllTests.PRODUCT_DESCRIPTION.value),
        (Locators.PRODUCT_PRICE_INPUT, DataForAllTests.PRODUCT_PRICE.value)])
    # Выбрать Город
    create_lisiting_page.select_drop_down_list_item(
        Locators.SELECT_DROPDOWN_CITIES_BUTTON,
        Locators.DROP_DOWN_LIST_CITIES,
        DataForAllTests.SPB_CITIES.value)
    # Выбрать категорию
    create_lisiting_page.select_drop_down_list_item(
        Locators.SELECT_DROPDOWN_CATEGORY_BUTTON,
        Locators.DROP_DOWN_PRODUCT_CATEGORY,
        DataForAllTests.BOOKS_CATEGORY.value)
    # Выбрать «Состояние товара»
    create_lisiting_page.click_element(
        Locators.BY_STATE_RADIOBUTTON)
    # Нажать кнопку «Опубликовать»
    create_lisiting_page.click_element(
        Locators.PUBLISH_AD_BUTTON)
    # Перейти в профиль пользователя
    create_lisiting_page.click_element(
        Locators.AUTHORIZED_USER_AVATAR)

   # Проверить, что в блоке «Мои объявления» отображается созданное объявление
    create_lisiting_page.verify_last_advertisement(
        DataForAllTests.AD_TITLE.value)

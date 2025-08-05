import time

from data.data_for_all_tests import DataForAllTests



def test_creation_ad_authorized_user(locators):
    # Открыть форму регистрации
    locators.click_element(locators.login_and_registration_button)
    # Заполнить поля Email и Password
    locators.fill_inputs([
        (locators.email_input, DataForAllTests.REPEAT_LOGIN.value),
        (locators.password_input, DataForAllTests.PASSWORD.value)])
    # Кликнуть по кнопке "Войти"
    locators.click_element(locators.login_button)
    time.sleep(2)
    # Кликнуть по кнопке "Разместить объявление"
    locators.click_element(locators.post_advertisement_button)
    # Заполнить поля «Название», «Описание товара» и «Стоимость»
    locators.fill_inputs([
        (locators.title_ad_input, DataForAllTests.AD_TITLE.value),
        (locators.product_description_nput, DataForAllTests.PRODUCT_DESCRIPTION.value),
        (locators.product_price_input, DataForAllTests.PRODUCT_PRICE.value)])
    # Выбрать Город
    locators.select_drop_down_list_item(
        locators.select_dropdown_cities_button,
        locators.drop_down_list_cities,
        DataForAllTests.SPB_CITIE.value)
    # Выбрать категорию
    locators.select_drop_down_list_item(
        locators.select_dropdown_category_button,
        locators.drop_down_product_category,
        DataForAllTests.BOOKS_CATEGORY.value)
    # Выбрать «Состояние товара»
    locators.click_element(locators.by_state_radiobutton)
    # Нажать кнопку «Опубликовать»
    locators.click_element(locators.publish_ad_button)
    # Перейти в профиль пользователя
    locators.click_element(locators.authorized_user_avatar)

   # Проверить, что в блоке «Мои объявления» отображается созданное объявление

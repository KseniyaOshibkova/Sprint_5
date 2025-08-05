from data.data_for_all_tests import DataForAllTests



def test_ad_creation_unauthorized_user(locators):
    # Нажать кнопку "Разместить объявление"
    locators.click_element(locators.post_advertisement_button)

    # Проверить отображение заголовка в модальном окне
    locators.test_check_display_title_in_modal_window(
        window_locator=locators.modal_window_authorize,
        title_text=DataForAllTests.AUTHORIZE_WINDOW_TITLE.value)

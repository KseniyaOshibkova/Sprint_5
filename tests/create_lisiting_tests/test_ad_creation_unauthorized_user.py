from locators.locators import Locators



def test_ad_creation_unauthorized_user(driver,login_page):
    # Нажать кнопку "Разместить объявление"
    login_page.click_element(Locators.POST_ADVERTISEMENT_BUTTON)

    # Проверить отображение заголовка в модальном окне
    login_page.check_display_title_in_modal_window(
        Locators.MODAL_WINDOW_AUTHORIZE,
        Locators.PLS_LOGIN_TITLE)

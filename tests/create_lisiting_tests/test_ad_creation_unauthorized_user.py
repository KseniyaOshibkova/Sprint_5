



def test_ad_creation_unauthorized_user(driver, login_page, create_lisiting_page):
    # Нажать кнопку "Разместить объявление"
    create_lisiting_page.open_post_advertisement()

    # Проверить отображение заголовка в модальном окне
    login_page.check_display_title_in_modal_window_create()

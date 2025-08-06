from selenium.webdriver.common.by import By

class Locators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.input_inputStandart__JweLZ[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'].input_inputStandart__JweLZ")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword'].input_inputStandart__JweLZ")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    AUTHORIZED_USER_AVATAR = (By.XPATH, "//button[contains(@class, 'circleSmall')]")
    AUTHORIZED_USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    REGISTRATION_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and .='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    MODAL_WINDOW_AUTHORIZE = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")
    POST_ADVERTISEMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and normalize-space()="
                                           "'Разместить объявление']")
    TITLE_AD_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PRODUCT_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRODUCT_PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    DROP_DOWN_LIST_CITIES = (By.CSS_SELECTOR, "input[name='city'][readonly]")
    DROP_DOWN_PRODUCT_CATEGORY = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw")
    BY_STATE_RADIOBUTTON = (By.XPATH, "//label[text()='Б/У']/preceding-sibling::div[contains(@class, "
                                      "'radioUnput_inputRegular__FbVbr')]")
    PUBLISH_AD_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and normalize-space()='Опубликовать']")
    SELECT_DROPDOWN_CITIES_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, "
                                               "'dropDownMenu_arrow')]")
    SELECT_DROPDOWN_CATEGORY_BUTTON = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw > "
                                                        "button.dropDownMenu_arrowDown__pfGL1")
    ALL_AD = (By.CSS_SELECTOR, "div.card")
    LAST_AD = (By.CLASS_NAME, "h2")
    PARENT_ELEMENT = (By.XPATH, "./..")
    BUTTON_IN_LIST_CONTAINER = (By.XPATH, f"//div[@class='dropDownMenu_options__CmHmm']""//button"
                                          "[.//span[normalize-space()='{option_text}']]")
    PLS_LOGIN_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

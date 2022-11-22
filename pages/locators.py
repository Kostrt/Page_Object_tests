from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_USERNAME = (By.NAME, "login-username") #  test 
    LOGIN_PASSWORD = (By.NAME, "login-password") # test
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2") # test
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT_CHECK = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_CHECK = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_USERNAME = (By.NAME, "login-username") #  test incorrect
    LOGIN_PASSWORD = (By.NAME, "login-password1") # test inc
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password21") # test
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


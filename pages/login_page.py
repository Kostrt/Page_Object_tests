from .base_page import BasePage
from .locators import LoginPageLocators
import time
from selenium import webdriver

email = str(time.time()) + "@fakemail.org"
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in LoginPageLocators.LOGIN_URL, "Login url have no 'login1' "  # реализуйте проверку на корректный url адрес
    

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login_Username form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login_PASSWORD form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration_PASSWORD form is not presented"

    def register_new_user(self):
        user_login = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email = str(time.time()) + "@fakemail.org"
        user_login.send_keys(email)
        user_passwoed1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        user_passwoed1.send_keys("Qwerty12345678QQQ")
        user_passwoed2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        user_passwoed2.send_keys("Qwerty12345678QQQ")
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_submit.click()
       

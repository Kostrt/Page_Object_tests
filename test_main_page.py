from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        page = MainPage(browser, link)  
        page.open()                      
        page.go_to_login_page()          

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()    
 
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_should_be_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
def test_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
def test_should_be_register_form(browser):  
    page = LoginPage(browser, link)
    page.open() 
    page.should_be_register_form()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_empty_basket_message()
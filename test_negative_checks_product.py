from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.should_adding_product_to_basket()
    page.should_not_be_success_message()
 
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_not_be_success_message()
 
@pytest.mark.xfail(reason="this bug should be for presentation")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.should_adding_product_to_basket()
    page.should_success_message_is_disappeared()
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_LINK), "Button 'ADD to basket' is not presented"
        add_basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_LINK)
        add_basket_link.click()
    
    def after_adding_chek_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_check = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_CHECK)
        assert name_product.text== name_product_check.text, "Name at basket incorrect"
    
    def after_adding_chek_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product_check = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_CHECK)
        assert price_product.text == price_product_check.text, "Price at basket incorrect"

        # assert price_product.get_attribute("value")== price_product_check.get_attribute("value"), "Price at basket incorrect"

    
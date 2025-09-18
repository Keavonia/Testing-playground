from .locators import ProductPageLocators, ProductCardLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def go_to_main_page(self):
        self.browser.find_element(*ProductPageLocators.BACK_TO_PRODUCTS).click()

    def add_to_shopping_cart_product_page(self):
        self.browser.find_element(*ProductCardLocators.ADD_TO_CART).click()

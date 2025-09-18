from .locators import ShoppingCartLocators, MainPageLocators
from .base_page import BasePage


class ShoppingCartPage(BasePage):
    def go_to_main_page(self):
        self.browser.find_element(*ShoppingCartLocators.BUTTON_CONTINUE_SHOPPING).click()

    def go_to_checkout_page(self):
        self.browser.find_element(*ShoppingCartLocators.BUTTON_CHECKOUT).click()

    def should_not_be_item_in_cart(self):
        assert self.is_not_element_present(*ShoppingCartLocators.ITEM_IN_CART), \
            "The product should not be in the cart, but it is."

    def should_be_item_in_cart(self):
        assert self.is_element_present(*ShoppingCartLocators.ITEM_IN_CART), \
            "The product should be in the cart, but it's not there."

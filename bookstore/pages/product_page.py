from .base_page import BasePage
from .locators import ProductPageLocators, MessagesAfterAdding


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_product_name_in_success_message(self):
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message_text = self.browser.find_element(*MessagesAfterAdding.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name_text == success_message_text, \
            f"Product name in message should be '{product_name_text}', but got '{success_message_text}'"

    def should_be_product_price_in_success_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_text = self.browser.find_element(*MessagesAfterAdding.BASKET_TOTAL_ALERT).text
        basket_total_price = basket_total_text.split()[-1]
        assert product_price == basket_total_price, \
            f"Product price should be '{product_price}', but basket shows '{basket_total_price}'"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*MessagesAfterAdding.SUCCESS_MESSAGE), \
            "Success message should not be present, but it is"

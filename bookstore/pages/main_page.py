from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
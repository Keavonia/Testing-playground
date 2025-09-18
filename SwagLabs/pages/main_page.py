from .base_page import BasePage
from .locators import MainPageLocators, ProductSortLocators


class MainPage(BasePage):
    """
    Sorting
    """

    def should_be_sort(self):
        assert self.is_element_present(*MainPageLocators.PRODUCT_SORT), 'Product sorting is not present.'

    def sort_az(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_SORT).click()
        self.browser.find_element(*ProductSortLocators.AZ).click()

    def sort_za(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_SORT).click()
        self.browser.find_element(*ProductSortLocators.ZA).click()

    def sort_lohi(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_SORT).click()
        self.browser.find_element(*ProductSortLocators.LOHI).click()

    def sort_hilo(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_SORT).click()
        self.browser.find_element(*ProductSortLocators.HILO).click()

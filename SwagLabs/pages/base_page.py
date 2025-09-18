from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from bookstore.pages.locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from SwagLabs.pages.locators import MainPageLocators, HeaderLocators, FooterLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # def go_to_login_page(self):
    #     self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID).click()

    def confirm_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    """Header"""

    def should_be_bm_menu(self):
        assert self.is_element_present(*HeaderLocators.MENU_BUTTON), 'Menu is not present.'

    def should_be_logo(self):
        assert self.is_element_present(*HeaderLocators.LOGO), 'Logo is not present.'

    def should_be_shopping_cart(self):
        assert self.is_element_present(*HeaderLocators.SHOPPING_CART), 'Shopping cart is not present.'

    def go_to_shopping_cart(self):
        self.browser.find_element(*HeaderLocators.SHOPPING_CART).click()

    """Footer"""

    def should_be_social_twitter(self):
        assert self.is_element_present(*FooterLocators.SOCIAL_TWITTER), 'Social Twitter is not present.'

    def should_be_social_facebook(self):
        assert self.is_element_present(*FooterLocators.SOCIAL_FACEBOOK), 'Facebook is not present.'

    def should_be_social_linkedin(self):
        assert self.is_element_present(*FooterLocators.SOCIAL_LINKEDIN), 'Linkedin is not present.'

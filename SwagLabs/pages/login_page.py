from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def authorization_user(self, username, password):
        username_field = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        button_login = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)

        username_field.send_keys(username)
        password_field.send_keys(password)

        button_login.click()

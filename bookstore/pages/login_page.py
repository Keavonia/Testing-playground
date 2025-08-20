from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"В текущей ссылке ({current_url}), 'login' не найден"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def  register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pswd1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        pswd2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_field.send_keys(email)
        pswd1_field.send_keys(password)
        pswd2_field.send_keys(password)

        register_button.click()
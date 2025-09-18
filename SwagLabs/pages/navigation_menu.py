from .base_page import BasePage
from .locators import NavigationMenuLocators, MainPageLocators


class NavigationMenu(BasePage):
    def open_bm_menu(self):
        self.browser.find_element(*MainPageLocators.MENU_BUTTON).click()

    def should_be_menu_items(self):
        self.should_be_all_items_in_menu()
        self.should_be_about_in_menu()
        self.should_be_logout_in_menu()
        self.should_be_reset_in_menu()
        self.should_be_close_in_menu()

    def should_be_all_items_in_menu(self):
        assert self.is_element_present(*NavigationMenuLocators.ALL_ITEMS), 'All items menu item is not present.'

    def should_be_about_in_menu(self):
        assert self.is_element_present(*NavigationMenuLocators.ABOUT), 'About menu item is not present.'

    def should_be_logout_in_menu(self):
        assert self.is_element_present(*NavigationMenuLocators.LOGOUT), 'Logout menu item is not present.'

    def should_be_reset_in_menu(self):
        assert self.is_element_present(
            *NavigationMenuLocators.RESET_APP_STATE), 'Reset App State menu item is not present.'

    def should_be_close_in_menu(self):
        assert self.is_element_present(*NavigationMenuLocators.CLOSE_BUTTON), 'Close button not present.'

    def go_to_all_items(self):
        self.browser.find_element(*NavigationMenuLocators.ALL_ITEMS).click()

    def go_to_about_page(self):
        self.browser.find_element(*NavigationMenuLocators.ABOUT).click()

    def go_to_logout(self):
        self.browser.find_element(*NavigationMenuLocators.LOGOUT).click()

    def go_to_reset_app_state(self):
        self.browser.find_element(*NavigationMenuLocators.RESET_APP_STATE).click()

    def close_bm_menu(self):
        self.browser.find_element(*NavigationMenuLocators.CLOSE_BUTTON).click()

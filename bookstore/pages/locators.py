from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")


class MessagesAfterAdding():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success div.alertinner > strong")
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, "div.alert-info div.alertinner > p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, "div.basket-items > div.row")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


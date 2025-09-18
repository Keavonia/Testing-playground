from selenium.webdriver.common.by import By


class HeaderLocators():
    MENU_BUTTON = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    SHOPPING_CART = (By.CSS_SELECTOR, "a.shopping_cart_link")

    LOGO = (By.CSS_SELECTOR, "div.app_logo")


class FooterLocators():
    SOCIAL_TWITTER = (By.CSS_SELECTOR, "li.social_twitter")
    SOCIAL_FACEBOOK = (By.CSS_SELECTOR, "li.social_facebook")
    SOCIAL_LINKEDIN = (By.CSS_SELECTOR, "li.social_linkedin")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_wrapper-inner")

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='user-name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")

    BUTTON_LOGIN = (By.CSS_SELECTOR, "input[name='login-button']")


class MainPageLocators():
    PRODUCT_SORT = (By.CSS_SELECTOR, "select.product_sort_container")


class ProductSortLocators():
    AZ = (By.CSS_SELECTOR, "option[value='az']")
    ZA = (By.CSS_SELECTOR, "option[value='za']")
    LOHI = (By.CSS_SELECTOR, "option[value='lohi']")
    HILO = (By.CSS_SELECTOR, "option[value='hilo']")


class NavigationMenuLocators():
    ALL_ITEMS = (By.CSS_SELECTOR, "a#inventory_sidebar_link")
    ABOUT = (By.CSS_SELECTOR, "a#about_sidebar_link")
    LOGOUT = (By.CSS_SELECTOR, "a#logout_sidebar_link")
    RESET_APP_STATE = (By.CSS_SELECTOR, "a#reset_sidebar_link")

    CLOSE_BUTTON = (By.CSS_SELECTOR, "button#react-burger-cross-btn")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.inventory_details_name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.inventory_details_price")
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "button.btn.btn_secondary.back.btn_large.inventory_details_back_button")


class ProductCardLocators():
    PRODUCT_CARD = (By.CSS_SELECTOR, "div.inventory_item")

    PRODUCT_CARD_NAME = (By.CSS_SELECTOR, "div.inventory_item_name")
    PRODUCT_CARD_IMAGE = (By.CSS_SELECTOR, "img.inventory_item_img")
    PRODUCT_CARD_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")
    CARD_ADD_TO_CART = (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")


class ShoppingCartLocators():
    MISSING_ITEM_IN_CART = (By.CSS_SELECTOR, "div.removed_cart_item")
    ITEM_IN_CART = (By.CSS_SELECTOR, "div.cart_item")

    CART_QUANTITY = (By.CSS_SELECTOR, "div.cart_quantity")

    BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, "button.btn.btn_secondary.btn_medium.back")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "button.btn.btn_action.btn_medium.checkout_button")


class CheckoutYourInformationPageLocators():
    CHECKOUT_INFO_CONTAINER = (By.CSS_SELECTOR, "div.checkout_info_container")

    FIRST_NAME = (By.CSS_SELECTOR, "input#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "input#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "input#postal-code")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message-container")
    CLOSE_BUTTON_ERROR = (By.CSS_SELECTOR, "button.error-button")

    BUTTON_CANCEL = (By.CSS_SELECTOR, "button.btn.btn_secondary.btn_medium.back.cart_cancel_link")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input.submit-button.btn.btn_primary.cart_button.btn_action")


class CheckoutOverviewPageLocators():
    CART_QUANTITY = (By.CSS_SELECTOR, "div.cart_quantity")

    ITEM_TOTAL = (By.CSS_SELECTOR, "div.summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, "div.summary_tax_label")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.summary_total_label")


class CheckoutCompletePageLocators():
    COMPLETE_CONTAINER = (By.CSS_SELECTOR, "div#checkout_complete_container")

    BUTTON_BACK_HOME = (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small")

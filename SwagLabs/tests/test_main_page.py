from SwagLabs.pages.main_page import MainPage
from SwagLabs.pages.navigation_menu import NavigationMenu
from SwagLabs.pages.product_card import ProductCard
from SwagLabs.pages.shopping_cart_page import ShoppingCartPage

# link = 'https://www.youtube.com/'
link = 'https://www.saucedemo.com/inventory.html'


class TestHeaderFooter():
    def test_should_be_header_footer(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()
        page.should_be_logo()
        page.should_be_shopping_cart()

        page.should_be_social_twitter()
        page.should_be_social_facebook()
        page.should_be_social_linkedin()


class TestMenuMainPage():
    def test_menu_open_all_items_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        menu = NavigationMenu(browser, browser.current_url)
        menu.open_bm_menu()
        menu.should_be_menu_items()

        menu.go_to_all_items()

    def test_menu_open_about_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        menu = NavigationMenu(browser, browser.current_url)
        menu.open_bm_menu()
        menu.should_be_menu_items()

        menu.go_to_about_page()

    def test_menu_logout_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        menu = NavigationMenu(browser, browser.current_url)
        menu.open_bm_menu()
        menu.should_be_menu_items()

        menu.go_to_logout()

    def test_menu_reset_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        menu = NavigationMenu(browser, browser.current_url)
        menu.open_bm_menu()
        menu.should_be_menu_items()

        menu.go_to_reset_app_state()

    def test_close_menu_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        menu = NavigationMenu(browser, browser.current_url)
        menu.open_bm_menu()
        menu.should_be_menu_items()

        menu.close_bm_menu()


class TestProductSort():
    def test_product_sort_az(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        page.sort_az()

    def test_product_sort_za(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        page.sort_za()

    def test_product_sort_lohi(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        page.sort_lohi()

    def test_product_sort_hilo(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_bm_menu()

        page.sort_hilo()


class TestProductCard():
    def test_add_product_by_name(self, browser):
        page = MainPage(browser, link)
        page.open()

        card = ProductCard(browser, browser.current_url)
        card.add_product_to_cart_by_name("Sauce Labs Backpack")

        price = card.get_product_price_by_name("Sauce Labs Backpack")
        print(f"Цена товаар: {price}")

    def test_go_to_product_page_by_name(self, browser):
        page = MainPage(browser, link)
        page.open()

        card = ProductCard(browser, browser.current_url)
        card.go_to_product_page_by_name("Sauce Labs Backpack")

    def test_go_to_cart_page_by_name_image(self, browser):
        page = MainPage(browser, link)
        page.open()

        card = ProductCard(browser, browser.current_url)
        card.go_to_product_page_by_name_image("Sauce Labs Backpack")


class TestShoppingCart():
    def test_open_shopping_cart(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_shopping_cart()
        page.go_to_shopping_cart()

    def test_should_not_item_in_cart(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_shopping_cart()
        page.go_to_shopping_cart()
        cart = ShoppingCartPage(browser, browser.current_url)
        cart.should_be_shopping_cart()

    def test_add_item_to_cart_and_verify_presence(self, browser):
        page = MainPage(browser, link)
        page.open()

        card = ProductCard(browser, browser.current_url)
        card.add_product_to_cart_by_name("Sauce Labs Backpack")
        card.add_product_to_cart_by_name("Sauce Labs Bike Light")

        page.go_to_shopping_cart()
        cart = ShoppingCartPage(browser, browser.current_url)
        cart.check_product_in_cart_by_name("Sauce Labs Backpack")
        cart.check_product_in_cart_by_name("Sauce Labs Bike Light")


    def test_go_to_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_shopping_cart()
        page.go_to_shopping_cart()
        cart = ShoppingCartPage(browser, browser.current_url)
        cart.go_to_main_page()

    def test_go_to_checkout_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_shopping_cart()
        page.go_to_shopping_cart()
        cart = ShoppingCartPage(browser, browser.current_url)
        cart.go_to_checkout_page()

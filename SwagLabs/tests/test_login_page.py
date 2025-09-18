from SwagLabs.pages.login_page import LoginPage


def test_user_can_add_product_to_basket(browser):
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = LoginPage(browser, link)
    page.open()




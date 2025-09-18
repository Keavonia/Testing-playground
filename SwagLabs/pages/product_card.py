from .locators import ProductCardLocators
from .base_page import BasePage
from selenium.common import NoSuchElementException


class ProductCard(BasePage):
    def get_all_product_cards(self):
        return self.browser.find_elements(*ProductCardLocators.PRODUCT_CARD)

    def find_product_card_by_name(self, target_name):
        cards = self.get_all_product_cards()

        for index, card in enumerate(cards):
            try:
                name_element = card.find_element(*ProductCardLocators.PRODUCT_CARD_NAME)
                if name_element.text == target_name:
                    return card, index
            except NoSuchElementException:
                continue

        return None, None

    def add_product_to_cart_by_name(self, product_name):
        card, index = self.find_product_card_by_name(product_name)

        if card is not None:
            try:
                card.find_element(*ProductCardLocators.CARD_ADD_TO_CART).click()
                print(f"Товар '{product_name}' добавлен в корзину.")
            except Exception as e:
                print(f"Ошибка при добавление товара '{product_name}':'{e}'.")
                return False
        else:
            print(f"Товар '{product_name}' не найден на странице.")
            return False

    def go_to_product_page_by_name(self, product_name):
        card, index = self.find_product_card_by_name(product_name)
        if card is not None:
            try:
                card.find_element(*ProductCardLocators.PRODUCT_CARD_NAME).click()
                print(f"Переход на страницу товара'{product_name}'.")
                return True
            except Exception as e:
                print(f"Ошибка при переходе на страницу товара '{product_name}':'{e}'.")
                return False

        else:
            print(f"Товар '{product_name}' не найден для перехода.")
            return False

    def go_to_product_page_by_name_image(self, product_name):
        card, index = self.find_product_card_by_name(product_name)
        if card is not None:
            try:
                card.find_element(*ProductCardLocators.PRODUCT_CARD_IMAGE).click()
                print(f"Переход на страницу товара'{product_name}'.")
                return True
            except Exception as e:
                print(f"Ошибка при переходе на страницу товара '{product_name}':'{e}'.")
                return False
        else:
            print(f"Товар '{product_name}' не найден для перехода.")
            return False

    def get_product_price_by_name(self, product_name):
        card, index = self.find_product_card_by_name(product_name)
        if card is not None:
            try:
                return card.find_element(*ProductCardLocators.PRODUCT_CARD_PRICE).text
            except Exception as e:
                print(f"Ошибка получении цены товара '{product_name}':'{e}'.")
                return False
        else:
            print(f"Товар '{product_name}' не найден для получения цены.")
            return False

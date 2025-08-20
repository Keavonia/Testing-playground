from .base_page import BasePage
from .locators import BasketPageLocators
import logging

logger = logging.getLogger(__name__)

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        logger.info("Проверка на наличие надписи")
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not present"
        logger.info("Надпись есть")

        logger.info("Проверка на отсутствие товара")
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Basket should be empty, but products are present"
        logger.info("Товаров нет")

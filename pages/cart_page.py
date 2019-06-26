from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import (NoSuchElementException)

class CartPage(BasePage):
    def is_basket_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_FIRST_ITEM)
            return False
        except NoSuchElementException:
            return True

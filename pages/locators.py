from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTERED_ICON = (By.XPATH, '//div[@class="alertinner wicon" and contains(text(), "register")]')

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
    
    
class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner")]')
    
class BasketPageLocators():
    BASKET_FIRST_ITEM = (By.CSS_SELECTOR, "#basket_formset .basket-items")

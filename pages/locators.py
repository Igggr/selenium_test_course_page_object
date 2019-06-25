from selenium.webdriver.common.by import By

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

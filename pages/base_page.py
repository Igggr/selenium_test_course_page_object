from selenium.common.exceptions import (NoSuchElementException)
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except (NoSuchElementException):
            return False
        
        
    def open(self):
        self.browser.get(self.url) 
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
        
    def go_to_basket(self):
        busket = self.browser.find_element(*BasePageLocators.BASKET)
        busket.click()

    def should_be_autorised(self):
        assert self.is_element_present(*BasePageLocators.REGISTERED_ICON)
        

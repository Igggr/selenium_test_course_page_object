from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class ProductPage(BasePage):
    def add_to_busket(self):
        add_to_busket_button = self.browser.find_element(* ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        add_to_busket_button.click()
            
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
            return True
        except NoAlertPresentException:
            print("No second alert presented")
            return False
   
                 
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
   
   
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True
    
        
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

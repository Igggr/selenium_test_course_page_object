from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.url.find("login") != -1, "Login url is not presented"
        # assert  not self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
        
    def register_new_user(self, email, password):
        email_field = self.browser.find_element_by_id("id_registration-email")
        email_field.send_keys(email)
        password_field_1 = self.browser.find_element_by_id("id_registration-password1")
        password_field_2 = self.browser.find_element_by_id("id_registration-password2")
        password_field_1.send_keys(password)
        password_field_2.send_keys(password)
        submit = self.browser.find_element_by_name("registration_submit")
        submit.click()

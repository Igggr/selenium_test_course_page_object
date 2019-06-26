from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.locators import ProductPageLocators
import pytest
import time


@pytest.mark.xfail(reason="in fact guest will see this message")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_not_be_success_message()
    
    
@pytest.mark.xfail(reason="success message will not dissapear")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])  
def test_message_dissapeared_after_adding_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_dissapear(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])    
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()    

   
@pytest.mark.need_review   
@pytest.mark.guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  


@pytest.mark.need_review
@pytest.mark.guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser, link):  
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = CartPage(browser,  url=browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
@pytest.mark.guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_cart(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_busket()
        page.should_be_second_alert() 

@pytest.mark.user
class TestUserAddToCartFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        passwd = str(time.time())
        login_page.register_new_user(email, passwd)
        yield
        # teardown
    
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])        
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message() 
    
    @pytest.mark.need_review                              
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])                                                                                                                
    def test_user_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_busket()
        page.should_be_second_alert()


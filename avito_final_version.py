import time
from selenium import webdriver
browser=webdriver.Firefox()
browser.implicitly_wait(10)

class ItemsPage:
    
    def __init__(self, browser):
        self.browser=browser
    
    def open_and_sign_in (browser):
        browser.get("https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1")
        button=browser.find_element_by_partial_link_text ("Вход и регистрация")
        button.click()
    
    def input_login_and_password ():
        input1=browser.find_element_by_name ("login")
        input1.send_keys("")
        input2=browser.find_element_by_name ("password")
        input2.send_keys ("")
        button=browser.find_element_by_name ("submit")
        button.click()
        time.sleep(5)
    
    def choosing_random_item ():
        button=browser.find_element_by_css_selector (".iva-item-titleStep-2bjuh a:link")
        button.click()
    
    def wait_and_switch_to_new_window ():
        time.sleep(5)
        name = browser.window_handles[1]
        browser.switch_to.window(name)

class Purchase:
    
    def purchase_with_delivery ():
        button=browser.find_element_by_css_selector (".item-view-actions button:first-child")
        button.click()
    
    def check_phone_input_is_empty ():
        input3=browser.find_element_by_css_selector ("[data-marker='sd/order-widget-field/phone']")
        assert input3.get_attribute('value')==''

try:
    ItemsPage.open_and_sign_in(browser)
    ItemsPage.input_login_and_password()
    ItemsPage.choosing_random_item()
    ItemsPage.wait_and_switch_to_new_window()
    Purchase.purchase_with_delivery()
    Purchase.check_phone_input_is_empty()


finally:
    browser.quit()
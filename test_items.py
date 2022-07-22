import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add():
    browser = webdriver.Chrome()
    #browser.get(link)
    #time.sleep(5)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "No basket"


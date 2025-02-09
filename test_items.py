from selenium.webdriver.common.by import By
from selenium import webdriver
browser = webdriver.Chrome()
def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary"), "not add basket"
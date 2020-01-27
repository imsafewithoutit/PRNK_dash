from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import random
import string

#login
try:
    link = "https://testdash.app.pryaniky.com/login"
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get(link)
    browser.maximize_window()

    login = browser.find_element_by_id("LOGINUSERNAME")
    login.send_keys("am@pryaniky.ru")

    password = browser.find_element_by_id("LOGINPASSWORD")
    password.send_keys("td1234")

    button1 = browser.find_element_by_id("LOGINENTERBUTTON")
    button1.click()

#find
    tabWait = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "news")))

    tabClick = browser.find_element_by_id("news")
    tabClick.click()

#post
    placeholder = browser.find_element_by_xpath("//div[text()=\"Текст новости\"]")
    placeholder.click()

    form = browser.find_element_by_xpath("//div[@class=\"notranslate public-DraftEditor-content\"]")
    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    form.send_keys(randstring)

    button2 = browser.find_element_by_xpath("//button[text()=\"Отправить\"]")
    button2.click()

#assert

#end
finally:
    browser.quit()

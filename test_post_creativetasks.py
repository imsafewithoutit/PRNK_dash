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

    tabWait = WebDriverWait(browser, 30).until(
    EC.element_to_be_clickable((By.ID, "creativetasks")))

    tabClick = browser.find_element_by_id("creativetasks")
    tabClick.click()

#post
    placeholder1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/input")
    placeholder1.click()

    textarea1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/input")

    randstring1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    textarea1.send_keys(randstring1)

    placeholder2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/div/div/div/div")
    placeholder2.click()

    textarea2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/div/div/div/div")

    randstring2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    textarea2.send_keys(randstring2)

    button = browser.find_element_by_xpath("//button[text()=\"Отправить\"]")
    button.click()

#assert

#end
finally:
    browser.quit()

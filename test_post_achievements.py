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

    tabWait = WebDriverWait(browser, 40).until(
    EC.element_to_be_clickable((By.ID, "achievements")))

    tabClick = browser.find_element_by_id("achievements")
    tabClick.click()

#post

    placeholder1 = browser.find_element_by_class_name("AchievementsSelector")
    placeholder1.click()

    select = browser.find_element_by_css_selector("#Dialog-root > div > div.Dialog-Body.Dialog-Body_entered > div > div.VerticalScroll.AchievementsSelector-Items > div:nth-child(2) > ul > li:nth-child(1)")
    select.click()

    placeholder2 = browser.find_element_by_xpath("//div[text()=\"Описание достижения\"]")
    placeholder2.click()

    textarea = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div")

    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    textarea.send_keys(randstring)

    button = browser.find_element_by_xpath("//button[text()=\"Отправить\"]")
    button.click()

#assert

#end
finally:
    browser.quit()

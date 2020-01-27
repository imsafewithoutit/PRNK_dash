from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

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

#like

    self.driver.find_element(By.XPATH, "//button[contains(.,\'Нравится\')]").click()
    element = self.driver.find_element(By.XPATH, "//div[5]/div/button/i")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.XPATH, "//button[2]/span").click()

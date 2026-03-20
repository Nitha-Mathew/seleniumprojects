from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_verify_keyboard_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/practice.html")
    frst_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    actions=ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(frst_name,"the testing academy").key_up(Keys.SHIFT).perform()
    time.sleep(10)
    driver.quit()



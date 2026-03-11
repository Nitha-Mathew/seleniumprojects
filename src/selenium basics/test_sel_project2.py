# Locators - Find the Web elements
#Open the URL https://app.vwo.com/#/login
#Find the Email id** and enter the email as admin@admin.com
# Find the Pass inputbox** and enter passwrod as admin.
#Find and Click on the submit button
#Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_*/

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_page():
    chrome_option=Options()
    chrome_option.add_argument("--start-maximized")
    driver=webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com/#/login")
    username=driver.find_element(By.ID,"login-username")
    username.send_keys("admin@admin.com")
    password=driver.find_element(By.ID,"login-password")
    password.send_keys("admin")
    log_but=driver.find_element(By.ID,"js-login-btn")
    log_but.click()
    time.sleep(5)

    msg=driver.find_element(By.ID,"js-notification-box-msg")
    assert msg.text=="Your email, password, IP address or location did not match"


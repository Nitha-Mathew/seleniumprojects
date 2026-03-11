from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_page():
    chrome_option=Options()
    chrome_option.add_argument("--start-maximized")
    driver=webdriver.Chrome(chrome_option)
    driver.get("https://www.idrive360.com/enterprise/login")
    username=driver.find_element(By.ID,"username")
    username.send_keys("augtest_040823@idrive.com")
    time.sleep(2)
    password=driver.find_element(By.ID,"password")
    password.send_keys("123456")
    log_but=driver.find_element(By.ID,"frm-btn")
    log_but.click()
    time.sleep(5)

    msg_txt=driver.find_element(By.CLASS_NAME,"id-btn id-warning-btn-drk id-tkn-btn")
    assert msg_txt.text=="Upgrade Now!"


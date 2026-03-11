from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def test_sel_alerts():
    chrome_option = Options()
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    alert_button=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    alert_button.click()
    WebDriverWait(driver,timeout=5).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    #alert.dismiss()
    #alert.send_keys()
    msg=driver.find_element(By.ID,"result")
    assert msg.text=="You successfully clicked an alert"

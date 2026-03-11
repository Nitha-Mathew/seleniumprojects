from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_project1_katalon_positive():
    chrome_option=Options()
    chrome_option.add_argument("--start-maximized")
    driver=webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    login_btn=driver.find_element(By.ID,"btn-login")
    login_btn.click()
    time.sleep(2)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"

def test_project1_katalon_negative():
    chrome_option=Options()
    chrome_option.add_argument("--start-maximized")
    driver=webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("Nitha")
    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("WrongPassword")
    login_btn=driver.find_element(By.ID,"btn-login")
    login_btn.click()
    invalid_msg=driver.find_element(By.CLASS_NAME,"text-danger")
    print(invalid_msg.text)
    time.sleep(2)
    assert invalid_msg.text=="Login failed! Please ensure the username and password are valid."







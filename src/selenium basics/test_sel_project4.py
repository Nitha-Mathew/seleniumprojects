
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def test_login_page():
    chrome_option = Options()
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com/#/login")
    txt=driver.find_element(By.LINK_TEXT,"Start a free trial")
    txt.click()
    #WebDriverWait(driver,timeout=5).until(EC.url_matches(pattern="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eq_loginpage"))
    WebDriverWait(driver=driver,poll_frequency=1,timeout=3).until(EC.url_to_be("https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"))
    assert driver.current_url== "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_page():
    chrome_option = Options()
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com/#/login")
    all_links=driver.find_elements(By.TAG_NAME,"a")
    for i in range(len(all_links)):
        print(all_links[i].text)

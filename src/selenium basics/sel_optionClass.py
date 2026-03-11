from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_options():
    chrome_option=Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximised")
    chrome_option.add_argument(("--window-size=900,600"))
    #chrome_option.add_argument("--headless")

    driver=webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

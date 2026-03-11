#makemytrip

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_page():
    chrome_option = Options()
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://www.makemytrip.com")
    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class=commonModal__close]")))
    cls_modal=driver.find_element(By.XPATH,"//span[@class=commonModal__close]")
    cls_modal.click()
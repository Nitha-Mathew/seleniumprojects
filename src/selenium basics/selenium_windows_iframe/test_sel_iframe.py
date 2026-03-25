from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_iframe():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()


    link=driver.find_element(By.XPATH,"//div[@aria-label='Close']//*[name()='svg']")
    link.click()

    driver.switch_to.frame("mce_0_ifr")
    nxt_link=driver.find_element(By.XPATH,"//body[@id='tinymce']/p")
    assert "Your content goes here." in nxt_link.text
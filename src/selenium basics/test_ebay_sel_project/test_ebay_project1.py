#print the titles of ebay sites after searching
#verify that 62 items are there for macmini

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
def test_ebay():
    chrome_options=Options()
    chrome_options.add_argument("--start-maximized")
    driver=webdriver.Chrome(chrome_options)
    driver.get("http://ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(5)
    search=driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search.send_keys('macmini')
    srch_but=driver.find_element(By.XPATH,"//span[@class='gh-search-button__label']")
    srch_but.click()
    lst_items=driver.find_elements(By.XPATH,"//div[@class='s-card__title']")
    lst_items_price=driver.find_elements(By.XPATH,"//span[@class='su-styled-text primary bold large-1 s-card__price']")
    lst_items_text=[title.text for title in lst_items]
    lst_items_price_text=[price.text for price in lst_items_price]
    for text,price in zip(lst_items_text,lst_items_price_text):
        print(text,price)



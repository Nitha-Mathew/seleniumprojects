from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_windows():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window=driver.current_window_handle
    print(parent_window)

    link=driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
    link.click()

    window_handles=driver.window_handles
    print(window_handles)

    for handle in window_handles:
        if handle!=parent_window:
            driver.switch_to.window(handle)
            if "New Window" in driver.page_source:
                print("test passed")


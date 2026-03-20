from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionBuilder

def test_verify_keyboard_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/selenium/mouse_interaction.html")
    atag=driver.find_element(By.ID,"click")
    atag.click()
    actions_builder=ActionBuilder(driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()



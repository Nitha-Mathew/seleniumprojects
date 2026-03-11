from selenium import webdriver

def test_first_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    pg_src=driver.page_source
    assert "CURA Healthcare Service" in pg_src
    driver.quit()

def test_first_edge():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    pg_src=driver.page_source
    assert "CURA Healthcare Service" in pg_src
    driver.quit()
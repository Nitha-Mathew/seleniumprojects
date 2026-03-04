from selenium import webdriver

def test_first():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    pg_src=driver.page_source
    assert "CURA Healthcare Service" in pg_src

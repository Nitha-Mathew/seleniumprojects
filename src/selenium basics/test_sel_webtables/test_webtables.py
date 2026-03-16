from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    row_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row=len(row_elements)
    col_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col=len(col_elements)
    for i in range(2,row+1):
        for j in range(1,col+1):
            dynamic_path=driver.find_element(By.XPATH,"//table[contains(id,'customers')]/tbody/tr[i]/td[j]")
            data=dynamic_path.text
            print(data)
            if "Helen Bennett" in data:
                country_path="//table[@id='customers']/tbody/tr[i]/td[j]/following-sibling::td"
                country_text=driver.find_element(By.XPATH,country_path).text
                print(country_text)

    driver.get("https://awesomeqa.com/webtable1.html")
    table=driver.find_element(By.XPATH,"//table[@summary_table='Sample Table']/tbody")
    row_table=table.find_element(By.TAG_NAME,"tr")



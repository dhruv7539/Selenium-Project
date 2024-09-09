from selenium import webdriver

chrome_driver_path="D:\INstalls\Chrome driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.w3schools.com/html/html_forms.asp")

search_bar=driver.find_element_by_id("fname")

search_bar.send_keys("Dhruv")




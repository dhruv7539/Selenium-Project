from selenium import webdriver

chrome_driver_path="D:\INstalls\Chrome driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

# widget=driver.find_element_by_class_name("widget-title")
# print(widget.text)

table=driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
print(table.text)
driver.quit()
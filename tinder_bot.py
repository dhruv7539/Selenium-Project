from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\INstalls\Chrome driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

log_in = driver.find_element_by_xpath('//*[@id="s1221153819"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()
driver.maximize_window()  # For maximizing window
# driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
time.sleep(5)

google = driver.find_element_by_xpath('//*[@id="s1442494255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
google.click()
# print(driver.window_handles)
# print(google.text)
base_page=driver.window_handles[0]

time.sleep(5)
fb_login_page=driver.window_handles[1]
driver.switch_to.window(fb_login_page)


email_input=driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys("dhruvbhanderi7@skype.com")

password_input=driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys("dhruvbh")
password_input.send_keys(Keys.ENTER)
time.sleep(15)

continue_enter=driver.find_element_by_css_selector(".x193iq5w .x1lliihq")
continue_enter.click()

driver.switch_to.window(base_page)


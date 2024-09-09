from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\INstalls\Chrome driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.facebook.com/v2.8/dialog/oauth?app_id=464891386855067&cbt=1675189805899&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df45e273987da38%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff3840ccd7b2c21%26relation%3Dopener&client_id=464891386855067&display=popup&domain=tinder.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Ftinder.com%2F&locale=en_US&logger_id=f176f5aebfbe84c&origin=1&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df71957f3ee05a%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff3840ccd7b2c21%26relation%3Dopener%26frame%3Dfb13af352be0bc&response_type=token%2Csigned_request%2Cgraph_domain&scope=user_birthday%2Cuser_photos%2Cemail%2Cuser_likes&sdk=joey&version=v2.8&ret=login&fbapp_pres=0&tp=unspecified&ext=1675193415&hash=AebNlOlFx9Tttpfp9qc")

email_input=driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys("dhruvbhanderi7@skype.com")

password_input=driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys("dhruvbh")
password_input.send_keys(Keys.ENTER)
time.sleep(15)

continue_enter=driver.find_element_by_css_selector(".x193iq5w .x1lliihq")
continue_enter.click()
# continue_enter.send_keys(Keys.TAB)
# continue_enter.send_keys(Keys.TAB)
# continue_enter.send_keys(Keys.ENTER)
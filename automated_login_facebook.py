from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
elem1=driver.find_element_by_id("email")
elem1.send_keys("YOUR EMAIL ID")
elem1.send_keys(Keys.RETURN)
elem2=driver.find_element_by_id("pass")
elem2.send_keys("YOUR PASSWORD")
elem2.send_keys(Keys.RETURN)

time.sleep(60)
	
elem3=driver.find_element_by_id("logoutMenu")
elem3.click()
elem4=driver.find_element_by_xpath("//span[@class='_54nh']")
elem4.click()

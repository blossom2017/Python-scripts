import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests

def main():
	if not os.path.exists("problems"):
		os.makedirs("problems")
	print("Hello")
	login_url = "https://leetcode.com/accounts/login/"
	chrome_options = webdriver.ChromeOptions()

	driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
	driver.maximize_window()
	driver.get(login_url)
	username = input("Enter username/email")
	password = input("Enter password")
	time.sleep(5)

	#Login
	while True:
		try:
			driver.find_element_by_id("id_login").send_keys(username)
			driver.find_element_by_id("id_password").send_keys(password)
			driver.find_element_by_id("signin_btn").click()
			break
		except:
			time.sleep(1)

	time.sleep(5)

	topic_tag = "array"
	lc_url = "https://leetcode.com/tag/" + topic_tag + "/"
	driver.get(lc_url)
	time.sleep(5)
	# Check the [show problem tags] button
	driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/label").click()
	time.sleep(5)

	soup = BeautifulSoup(driver.find_element_by_xpath("//*").get_attribute("outerHTML"), "html.parser")
	tables = soup.find_all("tbody", {"class": "reactable-data"})
	rows = soup.find_all("tr")
	file_row = ""
	for item in rows:
		data = item.find_all("td")
		if len(data) > 5:
			print(data)
			number = data[1].text
			title = data[2].text
			div = data[2].find("div").find("a")
			problem_link = "https://leetcode.com"+div['href']
			# Check the tags here
			acceptance = data[4].text
			difficulty = data[5].text
			if data[6].get("value"):
				frequency = data[6]['value']
			else: 
				frequency = 'N/A'
			file_row += (number + "," + title + "," + problem_link + "," + acceptance + "," + difficulty + "," + frequency + "\n")

	f = open("./problems/" + topic_tag, "w")
	f.write(file_row)
	f.close()


if __name__ == "__main__":
	main()
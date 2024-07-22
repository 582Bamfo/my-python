# Web Testing with Selenium
# Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()



#https://demo.seleniumeasy.com/
#This is use for testing
#assert is use instead of print it is use gto check

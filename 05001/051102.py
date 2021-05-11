from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://www.127.0.0.1:88/index.php"
driver.get(url)

driver.find_element_by_name("account").send_keys("admin")
driver.find_element_by_name("password").send_key("xingyuyu7788")


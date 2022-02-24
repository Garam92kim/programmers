from time import time
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("1234")
browser.find_element_by_id("pw").send_keys("45346@A")

browser.find_element_by_id("log.login").click()
time.sleep(3)

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

print(browser.page_source)

browser.quit()
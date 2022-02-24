from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button").click() # [0] -> 첫번째
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click() # [0] -> 첫번째
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b")
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[1]/div/input").click()
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys("제주도")
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys(Keys.ENTER)

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button/span").click()


# Lodding 처리 방법
# 최대 10초 대기 대부분 try - finally 로 진행
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "xpath값"))
finally:
    browser.quit()
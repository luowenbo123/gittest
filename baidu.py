#coding=utf-8 
from selenium import webdriver 
driver = webdriver.Chrome(executable_path="C:\\chromedriver") 
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()



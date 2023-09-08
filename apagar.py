#!/usr/bin/env python

import time
import datetime
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

log_file = open("/home/yago/log_routers.log","a")

ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-gpu")

chrome_options.add_argument("--headless")

chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)







#driver = webdriver.Chrome()
driver.get('http://192.168.0.1')

#print(driver.page_source)

pepe = driver.find_element_by_name('fInfo')

driver.switch_to_frame(pepe)

time.sleep(2)

username = driver.find_element_by_name("txtUser")
password = driver.find_element_by_name("txtPassword")
click = driver.find_element_by_id("login_1")

username.send_keys("")
password.send_keys("238500")

#wait = WebDriverWait(driver, 10)


click.click()

#wait = WebDriverWait(driver, 2)
time.sleep(2)
frame1 = driver.find_element_by_name('fInfo')
driver.switch_to_frame(frame1)

time.sleep(2)

wifi = driver.find_element_by_id("wifi_menu_href")



wifi.click()



time.sleep(2)

enable2G = driver.find_element_by_name("enablemode")
apply_button = driver.find_element_by_id("apply")
#disable
if enable2G.is_selected():
	enable2G.click()
	apply_button.click()

#wait = WebDriverWait(driver, 5)

time.sleep(2)

wifi2G = driver.find_element_by_id("wifi_2g_href")
wifi2G.click()

time.sleep(2)

enable2G_2 = driver.find_element_by_name("enablemode")
apply_button = driver.find_element_by_id("apply")

if enable2G_2.is_selected():
	enable2G_2.click()
	apply_button.click()

time.sleep(2)

#time.sleep(2)

log_file.write("\n"+sttime+"___Apagando Wifi 1__todoOk")

driver.quit()

time.sleep(2)


log_file.close()

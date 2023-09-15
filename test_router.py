#!/usr/bin/env python

import time
import datetime
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

#log_file = open("/home/yago/log_routers.log","a")

ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-gpu")

chrome_options.add_argument("--headless")

chrome_options.add_argument("--no-sandbox")

#driver = webdriver.Chrome('C:\\Users\\16888\\Downloads\\chromedriver_win32\\chromedriver.exe',options=chrome_options)
#driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)

driver = webdriver.Chrome(options=chrome_options)







#driver = webdriver.Chrome()
driver.get('http://192.168.3.250')

#print(driver.page_source)

time.sleep(2)

password = driver.find_element("id", "pcPassword")

password.send_keys('123456aA')

#password.submit()

#click = driver.find_element_by_id("loginBtnText")

clik = driver.find_element("id", "loginBtnText")



clik.click()

#wait = WebDriverWait(driver, 2)
time.sleep(2)

print(driver.page_source)



time.sleep(2)

#time.sleep(2)

#log_file.write("\n"+sttime+"___Apagando Wifi 1__todoOk")

driver.quit()

time.sleep(2)


log_file.close()

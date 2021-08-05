import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import datetime
import socket

start_time = datetime.now()
print (f'Start time: {start_time}')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.portaldelagro.cl/category/agroindustria/")

#time.sleep(5)
titulos = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/div/div[1]/div[1]')

print('Título: '+ titulos.text)

driver.quit()

end_time = datetime.now()
print (f'End time: {end_time}')
total_time = end_time - start_time
print (f'Finished in: {total_time}')
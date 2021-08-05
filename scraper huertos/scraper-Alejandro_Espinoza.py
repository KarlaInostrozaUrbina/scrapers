from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
#import time
from datetime import datetime

start_time = datetime.now()
print (f'Start time: {start_time}')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.portaldelagro.cl/category/agroindustria/")

#time.sleep(5)
precioBTC = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/div/div[1]/div[1]')

print('Título: '+ precioBTC.text)

driver.quit()

end_time = datetime.now()
print (f'End time: {end_time}')
total_time = end_time - start_time
print (f'Finished in: {total_time}')
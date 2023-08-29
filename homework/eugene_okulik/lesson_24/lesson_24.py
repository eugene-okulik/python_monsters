from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('start-maximized')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
sleep(3)
# driver.maximize_window()
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys('cat')
search_field.submit()
sleep(3)

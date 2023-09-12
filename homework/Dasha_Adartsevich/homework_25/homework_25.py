from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/popup/modal')
pop_up_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
sleep(3)
checkbox = driver.find_element(By.CSS_SELECTOR, '#id_checkbox_0').click()
send_button = driver.find_element(By.XPATH, '//*[@form="id-checkbox-form"]').click()
displayed_text = driver.find_element(By.CLASS_NAME, 'result-text')
print(displayed_text.text)

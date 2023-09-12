from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/input/simple')
text_input_field = driver.find_element(By.NAME, 'text_string')
text_input_field.send_keys('text')
text_input_field.submit()
entered_text = driver.find_element(By.ID, 'result-text')
print(entered_text.text)

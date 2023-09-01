from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
sleep(3)
driver.get('https://www.qa-practice.com/elements/button/simple')
# driver.find_element(By.ID, 'submit-id-submit').click()
driver.find_element(By.CSS_SELECTOR, '#submit-id-submit').click()
result = driver.find_element(By.CLASS_NAME, 'result-text')
print(result.text)
sleep(1)
driver.refresh()
# driver.find_element(By.CLASS_NAME, 'btn').click()
driver.find_element(By.CSS_SELECTOR, '.btn').click()
# header = driver.find_element(By.TAG_NAME, 'h1')
header = driver.find_element(By.CSS_SELECTOR, 'h1')
print(header.text)
result_box = driver.find_element(By.ID, 'result')
result2 = result_box.find_element(By.TAG_NAME, 'p')
print(result2.text)
driver.find_element(By.LINK_TEXT, 'Looks like a button').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Looks like').click()
driver.find_element(By.CSS_SELECTOR, '[href="#"]').click()
print(driver.find_element(By.CSS_SELECTOR, '#result-text').text)
driver.find_element(By.XPATH, '//*[@onclick="showReq()"]').click()
sleep(3)

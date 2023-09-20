from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/dynamic-properties')
    button = driver.find_element(By.ID, 'enableAfter')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
    button.click()

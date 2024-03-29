from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element(By.ID, 'firstName').send_keys('Jane')
driver.find_element(By.ID, 'lastName').send_keys('Doe')
driver.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('test@test.com')
driver.find_element(By.XPATH, '//*[@for="gender-radio-2"]').click()
driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
driver.find_element(By.ID, 'dateOfBirthInput').click()
select = driver.find_elements(By.TAG_NAME, 'select')
month_dropdown = Select(select[0])
month_dropdown.select_by_value('2')
year_dropdown = Select(select[1])
year_dropdown.select_by_value('1980')
driver.find_element(By.CLASS_NAME, 'react-datepicker__day--014').click()
driver.find_element(By.ID, 'subjectsInput').send_keys('Arts')
driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__menu').click()
driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-2"]').click()
driver.find_element(By.ID, 'currentAddress').send_keys('New York, 20 Jameson street')
driver.set_window_size(400, 700)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element(By.ID, 'state').click()
driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu').click()
driver.find_element(By.ID, 'city').click()
driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu').click()
driver.find_element(By.ID, 'submit').click()
driver.maximize_window()
table = driver.find_element(By.TAG_NAME, 'tbody')
print(table.text)

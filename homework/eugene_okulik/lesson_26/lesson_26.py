from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
sleep(3)
# driver.get('https://www.qa-practice.com/elements/button/simple')
# button = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
# print(button.get_attribute('value'))
# print(button.value_of_css_property('background-color'))
# print(button.tag_name)
# button.click()
# result = driver.find_element(By.CLASS_NAME, 'result-text')
# print(result.text)
# print(result.get_attribute('innerText'))
# driver.get('https://www.qa-practice.com/elements/button/disabled')
# button2 = driver.find_element(By.ID, 'submit-id-submit')
# # button2.click()
# print(button2.is_enabled())
# hidden = driver.find_element(By.NAME, 'csrfmiddlewaretoken')
# print(hidden.is_displayed())
# print(button2.is_displayed())
# select = driver.find_element(By.TAG_NAME, 'select')
# dropdown = Select(select)
# print('-' * 10)
# print(button2.is_enabled())
# dropdown.select_by_value('enabled')
# print(button2.is_enabled())
# cookies = driver.get_cookie('_ga')
# print(cookies)
# driver.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
# products = driver.find_elements(By.CSS_SELECTOR, '.product-item-link')
# for x in products:
#     print(x.text)
#
# print(products[-1].text)
driver.get('https://www.qa-practice.com/elements/new_tab/link')
driver.find_element(By.ID, 'new-page-link').click()
tabs = driver.window_handles
print(tabs)
# for tab in tabs:
#     if tab != driver.current_window_handle:
#         driver.switch_to.window(tab)
#         break
driver.switch_to.window(tabs[1])
print(driver.find_element(By.ID, 'result-text').text)

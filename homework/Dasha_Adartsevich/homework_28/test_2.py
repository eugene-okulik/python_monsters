from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_navigation():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/menu#')
    main_item_2 = driver.find_elements(By.XPATH, '//*[@href="#"]')[1]
    sub_sub_list = driver.find_elements(By.XPATH, '//*[@href="#"]')[4]
    sub_sub_item_2 = driver.find_elements(By.XPATH, '//*[@href="#"]')[6]
    action = ActionChains(driver)
    action.move_to_element(main_item_2)
    action.move_to_element(sub_sub_list)
    action.click(sub_sub_item_2)
    action.perform()

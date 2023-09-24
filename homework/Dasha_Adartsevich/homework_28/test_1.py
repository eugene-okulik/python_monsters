from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_tabs():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/index.html')
    driver.maximize_window()
    current_tab = driver.current_window_handle
    product = driver.find_elements(By.XPATH, '//*[@href="prod.html?idp_=1"]')[1]
    product_name = product.text
    ActionChains(driver).key_down(Keys.COMMAND).click(product).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.XPATH, '//*[@onclick="addToCart(1)"]').click()
    driver.close()
    driver.switch_to.window(current_tab)
    driver.find_element(By.ID, 'cartur').click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="success"]')))
    cart = driver.find_elements(By.TAG_NAME, 'td')[1]
    assert product_name == cart.text

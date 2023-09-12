from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(5)
sleep(3)  # для перетягивания окошка


def login():
    driver.get('https://magento.softwaretestingboard.com/customer/account/login/')
    # msg = driver.find_element(By.XPATH, '(//*[@class="not-logged-in"])[1]')
    # print(msg.text)
    driver.find_element(By.ID, 'email').send_keys('user1@mail.com')
    driver.find_element(By.ID, 'pass').send_keys('sdkjhsdkfjhs')
    driver.find_element(By.ID, 'send2').click()
    error_panel = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    print(error_panel.text)


def chains():
    driver.get('https://magento.softwaretestingboard.com')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    # ActionChains(driver).move_to_element(women).move_to_element(tops).move_to_element(jackets).click(jackets).perform()

    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'


def d_n_d():
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    draggable = driver.find_element(By.ID, 'rect-draggable')
    droppable = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    ActionChains(driver).click_and_hold(draggable).move_to_element(droppable).release(droppable).perform()


def hotkey():
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(3)


def cart():
    driver.get('https://magento.softwaretestingboard.com/josie-yoga-jacket.html')
    driver.find_element(By.ID, 'option-label-size-143-item-166').click()
    driver.find_element(By.ID, 'option-label-color-93-item-49').click()
    driver.find_element(By.ID, 'product-addtocart-button').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'counter-number')))
    print(driver.find_element(By.CLASS_NAME, 'counter-number').is_displayed())

    assert driver.find_element(By.CLASS_NAME, 'counter-number').text == '1'


hotkey()

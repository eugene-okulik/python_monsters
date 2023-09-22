from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()
driver.implicitly_wait(5)
sleep(3)  # для перетягивания окошка


def iframes():
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CLASS_NAME, 'navbar-toggler').click()
    driver.save_screenshot('iframe.png')
    # sleep(3)  # to see the results
    driver.switch_to.default_content()
    print(driver.find_element(By.CLASS_NAME, 'tab').text)
    driver.execute_script('window.scrollTo(0, 400);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)


def wait():
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    driver.execute_script('window.addEventListener("load", function () {alert("It\'s loaded!")});')
    print(driver.find_element(By.XPATH, '//*[@class="not-logged-in"]').text)


def alerts():
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.LINK_TEXT, 'Click').click()
    alert = Alert(driver)
    print(alert.text)
    sleep(2)
    alert.accept()


alerts()

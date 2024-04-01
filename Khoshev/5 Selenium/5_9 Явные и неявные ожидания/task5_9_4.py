# Охота на таинственный Блок

# import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with (webdriver.Chrome() as browser):
    url = 'https://parsinger.ru/selenium/5.9/2/index.html'
    browser.get(url=url)

    locator = ('id', 'qQm9y1rk')

    if box := WebDriverWait(browser, 40).until(EC.presence_of_element_located(locator)):
        box.click()
        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()


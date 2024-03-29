# Мимолётные теги

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/expectations/6/index.html'
    browser.get(url=url)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('id', "btn"))).click()
    time.sleep(3)

    locator = ('class name', 'BMH21YY')
    if WebDriverWait(browser, 40).until(EC.presence_of_element_located(locator)):
        print(browser.find_element(*locator).text)


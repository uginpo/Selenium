# Тайный заголовок

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/expectations/4/index.html'
    browser.get(url=url)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('id', "btn"))).click()
    time.sleep(3)

    if WebDriverWait(browser, 40).until(EC.title_contains('JK8HQ')):
        print(browser.execute_script("return document.title;"))

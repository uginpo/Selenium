# Ожидание title

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/expectations/3/index.html'
    browser.get(url=url)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('id', "btn"))).click()
    time.sleep(3)

    if WebDriverWait(browser, 20).until(EC.title_is('345FDG3245SFD')):
        print(browser.find_element('id', 'result').text)

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('id', "btn"))).click()
    time.sleep(3)
    print(browser.find_element('id', 'result').text)
    
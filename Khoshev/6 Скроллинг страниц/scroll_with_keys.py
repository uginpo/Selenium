import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)
    time.sleep(3)

    tags_input = browser.find_elements(By.TAG_NAME, 'input')

    for element in tags_input:
        element.send_keys(Keys.DOWN)
        time.sleep(1)
        
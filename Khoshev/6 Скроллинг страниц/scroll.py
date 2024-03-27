import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.execute_script("window.scrollBy(0,5000)")
    time.sleep(2)

    height = browser.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    print(height)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

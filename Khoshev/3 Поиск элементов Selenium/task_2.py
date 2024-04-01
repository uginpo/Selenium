import time
from selenium import webdriver


url = 'https://parsinger.ru/selenium/2/2.html'

with webdriver.Chrome() as driver:
    driver.get(url=url)
    link = driver.find_element('link text', '16243162441624')
    link.click()

    time.sleep(10)

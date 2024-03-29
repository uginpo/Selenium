import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
webdriver = webdriver.Chrome(service=service)

url = r'https://yandex.ru'
webdriver.get(url=url)

time.sleep(10)
webdriver.back()
time.sleep(3)

webdriver.forward()
time.sleep(3)

webdriver.refresh()
time.sleep(3)
# Настройка вьюпорта браузера
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with (webdriver.Chrome(service=service) as driver):
    url = 'https://parsinger.ru/window_size/1/'
    driver.get(url=url)
    driver.set_window_size(555, 694)
    print(driver.find_element('id', 'result').text)





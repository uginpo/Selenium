# Настройка вьюпорта браузера
import time

from itertools import product
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with (webdriver.Chrome(service=service) as driver):
    url = 'https://parsinger.ru/window_size/2/index.html'
    driver.get(url=url)

    for width, height in product(window_size_x, window_size_y):

        driver.set_window_size(width, height + 139)
        res = driver.find_element('id', 'result').text
        # time.sleep(1)

        if len(res) != 0:
            print(res)
            print({'width': width, 'height': height})
            break

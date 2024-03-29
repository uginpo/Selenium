import time
import webbrowser

from selenium import webdriver

option_Chrome = webdriver.ChromeOptions()
option_Chrome.add_argument('user-data-dir=/Users/user/Library/Application Support/Google/Chrome/Default')

with webdriver.Chrome(options=option_Chrome) as browser:
    url = 'https://yandex.ru/'

    browser.get(url=url)
    time.sleep(10)


import time
from selenium import webdriver
from seleniumwire import webdriver  # для авторизации

url = 'https://2ip.ru/'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    time.sleep(1)
    print(browser.find_element('id', 'd_clip_button').find_element('tag name', 'span').text)
    time.sleep(1)

# Запускаем через прокси
# Прокси должен быть вида IP:PORT

proxy = '35.185.196.38:3128'
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    print(browser.find_element('id', 'd_clip_button').find_element('tag name', 'span').text)
    time.sleep(5)

options = {'proxy': {
    'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
    'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
}}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get(url)
    print(browser.find_element('id', 'd_clip_button').find_element('tag name', 'span').text)
    browser.switc
    time.sleep(5)

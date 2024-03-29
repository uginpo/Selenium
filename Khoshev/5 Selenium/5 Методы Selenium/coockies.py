from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)

'''
[{'domain': '.ya.ru',
  'expiry': 1685518907,
  'httpOnly': False,
  'name': '_ym_d',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '1653982908'},
  ...
   {'domain': '.ya.ru',
  'expiry': 1656574906,
  'httpOnly': False,
  'name': 'yandex_gid',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '239'}]
'''

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name'])  # или cookie['value'] чтобы получить их значение

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    print(webdriver.get_cookie('_ym_uid')['expiry'])

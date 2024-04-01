# Откройте сокровища интернета
import time
from selenium import webdriver

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]


urls = [(sites[i], f'_blank{i+1}') for i in range(len(sites))]
text_scripts = [f'window.open("{url[0]}", "{url[0]}");' for url in urls]
CHECK_BOX_LOCATOR = ('xpath', '//input[@type="checkbox"]')
COD_LOCATOR = ('xpath', '//span[@id="result"]')

with webdriver.Chrome() as browser:

    for elem in text_scripts:
        browser.execute_script(elem)

    count = 0
    for x in range(1, len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])

        browser.find_element(*CHECK_BOX_LOCATOR).click()
        cod = int(browser.find_element(*COD_LOCATOR).text)
        time.sleep(1)
        count += cod ** 0.5

    print(round(count, 9))

# Охотник за загадочными числами
import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/blank/3/index.html'
    browser.get(url=url)

    BUTTONS_LOCATOR = ('xpath', '//input[@type="button"]')
    buttons = browser.find_elements(*BUTTONS_LOCATOR)

    for button in buttons:
        button.click()

    time.sleep(1)

    count = 0
    for x in range(1, len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        count += int(browser.execute_script("return document.title;"))

    print(count)

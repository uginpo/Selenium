# Коллекционер секретных рун

# import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with (webdriver.Chrome() as browser):
    url = 'https://parsinger.ru/selenium/5.9/5/index.html'
    browser.get(url=url)

    buttons_locator = ('xpath', '//div[@class="box_button"]')
    cross_locator = ('xpath', '//button[@id="close_ad"]')

    code = []
    buttons = browser.find_elements(*buttons_locator)
    for button in buttons:
        button.click()
        browser.find_element(*cross_locator).click()
        if WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(cross_locator)):
            if WebDriverWait(browser, 10).until(lambda _: button.text != ''):
                code.append(button.text)
print('-'.join(code))

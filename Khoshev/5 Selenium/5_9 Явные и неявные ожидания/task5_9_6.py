# Триумф над рекламным Заговором

# import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with (webdriver.Chrome() as browser):
    url = 'https://parsinger.ru/selenium/5.9/4/index.html'
    browser.get(url=url)

    close_locator = ('xpath', '//span[@class="close"]')
    button_locator = ('xpath', '//button')

    cross = browser.find_element(*close_locator)
    cross.click()

    if WebDriverWait(browser, 40).until(EC.invisibility_of_element_located(close_locator)):
        browser.find_element(*button_locator).click()

    message = browser.find_element('xpath', '//p[@id="message"]')
    print(message.text)



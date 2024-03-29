# Мерцающий Чек Бокс Мистерии

# import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with (webdriver.Chrome() as browser):
    url = 'https://parsinger.ru/selenium/5.9/6/index.html'
    browser.get(url=url)

    checkbox_locator = ('xpath', '//input')
    result_locator = ('xpath', '//p[@id="result"]')
    button_locator = ('xpath', '//button')

    element = browser.find_element(*checkbox_locator)

    if WebDriverWait(browser, 10).until(EC.element_to_be_selected(element)):
        browser.find_element(*button_locator).click()
        print(browser.find_element(*result_locator).text)
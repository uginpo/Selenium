# Познание атрибута display

# import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with (webdriver.Chrome() as browser):
    url = 'https://parsinger.ru/selenium/5.9/3/index.html'
    browser.get(url=url)

    locator = ('id', 'qQm9y1rk')

    flag = True

    while flag:
        for elem in ids_to_find:
            locator = ('id', f'{elem}')
            if box := WebDriverWait(browser, 40).until(EC.visibility_of_element_located(locator)):
                box.click()

        try:
            alert = browser.switch_to.alert
            print(alert.text)
            alert.accept()
            flag = False

        except NoAlertPresentException:
            continue



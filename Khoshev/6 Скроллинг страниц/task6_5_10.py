# Секретный код: кибер-расследование
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException

service = Service(ChromeDriverManager().install())

with (webdriver.Chrome(service=service) as driver):
    url = 'https://parsinger.ru/selenium/5.8/5/index.html'
    driver.get(url=url)

    INPUT_TEXT_LOCATOR = ("xpath", '//input[@id="guessInput"]')
    BUTTON_LOCATOR = ("xpath", '//button[@id="checkBtn"]')

    IFRAME_LOCATOR = ("xpath", '//div[@id="main_container"]')
    IFRAME_KEYS_LOCATOR = ('xpath', '//p[@id="numberDisplay"]')
    IFRAME_BUTTON_LOCATOR = ('xpath', '//button')

    for ind in range(9):
        iframes = driver.find_element(*IFRAME_LOCATOR)

        driver.switch_to.frame(iframes.find_elements('tag name', "iframe")[ind])
        frame_button = driver.find_element(*IFRAME_BUTTON_LOCATOR)
        driver.execute_script("arguments[0].click();", frame_button)

        key_iframe = driver.find_element(*IFRAME_KEYS_LOCATOR).text

        driver.switch_to.default_content()
        input_text = driver.find_element(*INPUT_TEXT_LOCATOR)
        input_text.clear()
        input_text.send_keys(key_iframe)
        driver.find_element(*BUTTON_LOCATOR).click()
        time.sleep(1)

        try:
            alert = driver.switch_to.alert
            print(alert.text)
            alert.accept()
            break

        except NoAlertPresentException:
            continue


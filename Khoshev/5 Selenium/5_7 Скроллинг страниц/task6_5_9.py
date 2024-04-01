# Поиск секретных пин-кодов

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with (webdriver.Chrome(service=service) as driver):
    url = 'https://parsinger.ru/selenium/5.8/2/index.html'
    driver.get(url=url)

    INPUT_LOCATOR = ("xpath", '//input[@class="buttons"]')
    PIN_LOCATOR = ("xpath", '//input[@id="input"]')
    CHECK_LOCATOR = ("xpath", '//input[@id="check"]')
    RESULT_LOCATOR = ("xpath", '//p[@id="result"]')

    buttons = driver.find_elements(*INPUT_LOCATOR)

    text_pin = driver.find_element(*PIN_LOCATOR)
    check_button = driver.find_element(*CHECK_LOCATOR)
    result = driver.find_element(*RESULT_LOCATOR).text

    for button in buttons:
        button.click()
        alert = driver.switch_to.alert
        pin = alert.text
        alert.accept()

        text_pin.clear()
        text_pin.send_keys(pin)
        check_button.click()

        result = driver.find_element(*RESULT_LOCATOR).text
        if result.isdigit():
            print(result)
            break

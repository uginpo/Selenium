# Условие задачи: "Поиск секретного кода"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.8/1/index.html'
    driver.get(url=url)

    INPUT_LOCATOR = ("xpath", '//input[@type="button"]')
    RESULT_LOCATOR = ("xpath", '//p[@id="result"]')
    buttons = driver.find_elements(*INPUT_LOCATOR)

    for button in buttons:
        button.click()
        driver.switch_to.alert.accept()

        result = driver.find_element(*RESULT_LOCATOR).text

        if result:
            print(result)
            break

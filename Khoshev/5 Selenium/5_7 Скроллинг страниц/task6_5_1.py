# "Космическая чистка урана"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.7/1/index.html'

    driver.get(url=url)
    buttons = driver.find_elements('xpath', '//button[@class="clickMe"]')

    for button in buttons:
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    # Переключаемся на алерт
    alert = driver.switch_to.alert

    # Получаем текст с алерта
    print(alert_text := alert.text)


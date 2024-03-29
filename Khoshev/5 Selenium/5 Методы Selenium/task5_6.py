# Освобождение скрытых элементов

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/scroll/4/index.html'
    driver.get(url=url)

    result = 0
    buttons = driver.find_elements('xpath', '//button[@class="btn"]')
    for button in buttons:
        # Пример получения фокуса элемента
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        res = driver.find_element('id', 'result').text
        result += int(res)
    print(result)

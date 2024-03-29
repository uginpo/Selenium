import time
from selenium import webdriver

url = 'https://parsinger.ru/selenium/6/6.html'

with (webdriver.Chrome() as driver):
    driver.get(url=url)
    expression = driver.find_element('id', 'text_box')
    print(num := eval(expression.text))

    numbers = driver.find_elements('xpath', '//option')
    for number in numbers:
        if num == int(number.text):
            number.click()

    driver.find_element('xpath', '//input[@class="btn"]').click()

    print(driver.find_element('id', 'result').text)

    time.sleep(10)

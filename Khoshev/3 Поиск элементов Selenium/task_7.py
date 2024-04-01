import time
from selenium import webdriver

url = 'https://parsinger.ru/selenium/7/7.html'

with (webdriver.Chrome() as driver):
    driver.get(url=url)
    numbers = driver.find_elements('xpath', '//option')
    summa = sum([int(number.text) for number in numbers])
    driver.find_element('id', 'input_result').send_keys(summa)

    driver.find_element('xpath', '//input[@class="btn"]').click()

    print(driver.find_element('id', 'result').text)

    time.sleep(10)

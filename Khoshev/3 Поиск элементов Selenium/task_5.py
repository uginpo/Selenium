import time
from selenium import webdriver

url = 'https://parsinger.ru/selenium/4/4.html'

with (webdriver.Chrome() as driver):
    driver.get(url=url)
    boxes = driver.find_elements('xpath', '//input[@type="checkbox"]')
    for box in boxes:
        box.click()
    driver.find_element('xpath', '//input[@class="btn"]').click()

    print(driver.find_element('id', 'result').text)

    time.sleep(10)

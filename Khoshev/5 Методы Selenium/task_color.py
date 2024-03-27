import time
from selenium import webdriver

url = 'https://parsinger.ru/selenium/5.5/4/1.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)

    gray_numbers = browser.find_elements('xpath', '//textarea[@color="gray"]')
    blue_numbers = browser.find_elements('xpath', '//textarea[@color="blue"]')
    buttons = browser.find_elements('xpath', '//div[@id="container"]//button')
    button_all = browser.find_element('id', 'checkAll')

    for gray_number, blue_number, button in zip(gray_numbers, blue_numbers, buttons):
        number = gray_number.text
        gray_number.clear()
        blue_number.send_keys(number)
        button.click()

    button_all.click()
    result = browser.find_element('id', 'congrats').text
    print(result)

    time.sleep(5)

import time
from selenium import webdriver


url = 'https://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as driver:
    driver.get(url=url)
    numbers = driver.find_elements('xpath', "//div[@class='text']/p[2]")

    summa = sum([int(number.text) for number in numbers])
    print(summa)

    time.sleep(3)

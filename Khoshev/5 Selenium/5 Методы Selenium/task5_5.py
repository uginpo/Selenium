# Поиск cookies и самого большого элемента 'expiry'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/methods/5/index.html'
    driver.get(url=url)
    refs = driver.find_elements('xpath', '//div[@class="urls"]/a')
    refs_atr = [ref.get_attribute('href') for ref in refs]

    biggest_time = 0
    result = ''
    for ref in refs_atr:
        driver.get(url=ref)

        cook_expiry = driver.get_cookies()
        if int(cook_expiry[0]['expiry']) > biggest_time:
            biggest_time = int(cook_expiry[0]['expiry'])
            res = driver.find_element('id', 'result')
            result = res.text
    print(result)

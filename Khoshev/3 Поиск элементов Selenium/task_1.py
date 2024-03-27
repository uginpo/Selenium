import time
from selenium import webdriver


url = 'https://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome() as driver:
    driver.get(url=url)
    content_lst = driver.find_elements('xpath', "//input[@class='form']")
    butt = driver.find_element('id', 'btn')
    for content in content_lst:
        content.send_keys('Text')
    butt.click()


    time.sleep(10)


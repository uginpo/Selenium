# Перемещение красного блока и поиск секретного токена
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as driver:
    url = 'https://parsinger.ru/draganddrop/1/index.html'
    driver.get(url=url)

    time.sleep(3)
    element_locator = ('id', 'field1')
    target_locator = ('id', 'field2')

    result_locator = ('id', 'result')

    action = ActionChains(driver)

    element = driver.find_element(*element_locator)
    target = driver.find_element(*target_locator)

    action.drag_and_drop(element, target).perform()
    time.sleep(3)

    print(driver.find_element(*result_locator).text)

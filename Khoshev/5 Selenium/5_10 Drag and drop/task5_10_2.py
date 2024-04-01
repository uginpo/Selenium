# Путешествие квадрата и проверочные точки
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/draganddrop/3/index.html'
    driver.get(url=url)

    time.sleep(3)
    element_locator = ('id', 'block1')
    targets_locator = ('xpath', '//div[@class="controlPoint"]')

    result_locator = ('id', 'message')

    action = ActionChains(driver)

    element = driver.find_element(*element_locator)
    targets = driver.find_elements(*targets_locator)

    action.click_and_hold(element).perform()

    for i in range(len(targets)):
        action.move_by_offset(50, 0).perform()

    action.move_by_offset(-5, 0).release().perform()
    time.sleep(3)

    print(driver.find_element(*result_locator).text)

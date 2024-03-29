# Путешествие квадрата

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/draganddrop/2/index.html'
    driver.get(url=url)
    driver.set_window_size(1000, 1500)

    time.sleep(3)
    element_locator = ('id', 'draggable')
    targets_locator = ('xpath', '//div[@class="box"]')

    result_locator = ('id', 'message')

    action = ActionChains(driver)

    element = driver.find_element(*element_locator)

    targets = driver.find_elements(*targets_locator)

    for target in targets:
        # action.click_and_hold(element).drag_and_drop_by_offset(element, 1150, 0).release().perform()
        action.drag_and_drop(element, target).perform()
    time.sleep(3)

    print(driver.find_element(*result_locator).text)

# Путешествие квадрата

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/draganddrop/2/index.html'
    driver.get(url=url)
    driver.set_window_size(1000, 1500)

    time.sleep(3)
    element_locator = ('xpath', '//div[contains(@class, "draganddrop")]')
    targets_locator = ('xpath', '//div[@class="draganddrop_end"]')

    result_locator = ('id', 'message')

    action = ActionChains(driver)

    elements = driver.find_elements(*element_locator)
    elements = elements[:-1]
    target = driver.find_element(*targets_locator)

    for element in elements:
        action.click_and_hold(element).drag_and_drop_by_offset(element, 1150, 0).release().perform()

    time.sleep(3)

    print(driver.find_element(*result_locator).text)

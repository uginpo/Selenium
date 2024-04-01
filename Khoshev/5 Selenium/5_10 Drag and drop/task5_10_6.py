# Автоматическая сортировка шариков

import time
from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/5.10/4/index.html'
    driver.get(url=url)
    driver.set_window_size(1600, 1800)

    time.sleep(3)
    elements_locator = ('xpath', "//div[contains(@class, 'draggable')]")
    targets_locator = ('xpath', "//div[contains(@class,'droppable')]")

    result_locator = ('xpath', '//p[@class="message"]')

    action = ActionChains(driver)

    elements = driver.find_elements(*elements_locator)

    targets = driver.find_elements(*targets_locator)

    for target in targets:
        for element in elements:
            color_element = Color.from_string(element.get_attribute('class').split()[1].split('_')[0])
            color_target = Color.from_string(target.get_attribute('class').split()[1])

            if color_target == color_element:
                action.drag_and_drop(element, target).perform()

    time.sleep(3)

    print(driver.find_element(*result_locator).text)


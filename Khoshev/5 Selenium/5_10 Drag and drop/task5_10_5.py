# Найдите пару

import time
from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/5.10/3/index.html'
    driver.get(url=url)
    driver.set_window_size(1600, 1800)

    time.sleep(3)
    elements_locator = ('xpath', "//div[contains(@class, 'draggable')]")
    targets_locator = ('xpath', "//div[@class='draganddrop_end']")

    result_locator = ('id', 'message')

    action = ActionChains(driver)

    elements = driver.find_elements(*elements_locator)

    targets = driver.find_elements(*targets_locator)

    for element in elements:
        for target in targets:
            color_element = Color.from_string(element.value_of_css_property('background-color'))
            color_target = Color.from_string(target.value_of_css_property('border-color'))

            if color_target == color_element:
                action.drag_and_drop(element, target).perform()

    time.sleep(3)

    print(driver.find_element(*result_locator).text)


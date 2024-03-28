# Бросок на правильное расстояние

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/5.10/8/index.html'
    driver.get(url=url)
    driver.set_window_size(1600, 1800)

    time.sleep(3)
    elements_locator = ('xpath', "//div[contains(@class, 'draggable')]")
    targets_locator = ('xpath', "//div[contains(@class,'droppable')]")

    result_locator = ('xpath', '//p[@id="message"]')

    action = ActionChains(driver)

    elements = driver.find_elements(*elements_locator)

    targets = driver.find_elements(*targets_locator)

    for target in targets:
        for element in elements:
            range_element = element.get_attribute('id').split('_')[1]
            range_target = target.get_attribute('id').split('_')[1]

            if range_target == range_element:
                x_offset = target.find_element('tag name', 'p').text.split()[1]
                x_offset = x_offset[:-2]
                action.drag_and_drop_by_offset(element, int(x_offset), 0).perform()

    time.sleep(3)

    print(driver.find_element(*result_locator).text)

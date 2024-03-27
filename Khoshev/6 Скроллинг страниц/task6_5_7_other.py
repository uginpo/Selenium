# Чётный Выбор: Бесконечный Чекбоксовый список

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.7/4/index.html'
    driver.get(url=url)

    actions = ActionChains(driver)

    LINE_LOCATOR = ('xpath', '//div[@class="child_container"]')
    NEXT_LINE_LOCATOR = ('xpath', 'following-sibling::div[@class="child_container"]')
    BOX_LOCATOR = ('xpath', 'input[@type="checkbox"]')
    ALERT_LOCATOR = ('xpath', '//button[@class="alert_button"]')

    boxes_line = driver.find_element(*LINE_LOCATOR)
    time.sleep(2)

    flag = True
    while flag:

        check_boxes = [box for box in boxes_line.find_elements(*BOX_LOCATOR) if
                       int(box.get_attribute('value')) % 2 == 0]
        for box in check_boxes:
            box.click()

        try:
            boxes_line = boxes_line.find_element(*NEXT_LINE_LOCATOR)
            actions.scroll_to_element(boxes_line).perform()

        except NoSuchElementException:

            try:
                button = driver.find_element(*ALERT_LOCATOR)
                actions.scroll_to_element(button).perform()
                button.click()
                flag = False
                break

            except NoSuchElementException:
                continue

    alert = driver.switch_to.alert
    print(alert.text)

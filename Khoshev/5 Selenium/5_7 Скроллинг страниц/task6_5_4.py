# Infinite scroll
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/infiniti_scroll_1/'
    driver.get(url=url)

    time.sleep(10)

    count = 0
    checkbox_list = []
    flag = True
    while flag:
        check_boxes = [x for x in driver.find_elements('xpath', '//input')]
        numbers = [x for x in driver.find_elements('xpath', '//span')]

        for check_box, number in zip(check_boxes, numbers):
            if check_box not in checkbox_list:
                try:
                    check_box.send_keys(Keys.TAB)
                except ElementNotInteractableException:
                    continue

                driver.execute_script("return arguments[0].scrollIntoView(true);", check_box)
                check_box.click()
                time.sleep(3)
                checkbox_list.append(check_box)
                count += int(number.text)
                if number.get_attribute('class') == "last-of-list":
                    flag = False
                    break

    print(count)


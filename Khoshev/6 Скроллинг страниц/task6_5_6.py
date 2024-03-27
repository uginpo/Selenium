# Операция "Пятерка": Одновременный Глубокий Скроллинг

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException

service = Service(ChromeDriverManager().install())

count = 0
with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/infiniti_scroll_3/'
    driver.get(url=url)
    actions = ActionChains(driver)
    windows = driver.find_elements('xpath', '//div[contains(@class, "scroll-container")]')
    time.sleep(10)

    for window in windows:
        class_wind = window.get_attribute('class')
        SPAN_LOCATOR = f'//div[@class="{class_wind}"]/span'

        numbers_list = []
        flag = True

        while flag:

            numbers = [x for x in window.find_elements('xpath', SPAN_LOCATOR)]

            for number in numbers:
                if number not in numbers_list:
                    try:
                        print(number.text)
                        actions.move_to_element(number).scroll_by_amount(0, 50).pause(1).perform()
                        count += int(number.text)
                        numbers_list.append(number)

                    except ElementNotInteractableException:
                        continue

                    if number.get_attribute('class') == "last-of-list":
                        flag = False
                        break

    print(count)

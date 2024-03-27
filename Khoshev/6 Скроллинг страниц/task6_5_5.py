# Десант в глубину: Поиск сокровищ среди скрытых элементов

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException


service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/infiniti_scroll_2/'
    driver.get(url=url)
    actions = ActionChains(driver)
    window = driver.find_element('id', 'scroll-container')

    time.sleep(10)

    count = 0
    numbers_list = []
    flag = True

    while flag:
        P_LOCATOR = ('tag name', 'p')
        numbers = [x for x in driver.find_elements(*P_LOCATOR)]

        for number in numbers:
            if number not in numbers_list:
                try:
                    actions.move_to_element(number).scroll_by_amount(0, 500).pause(3).perform()
                    count += int(number.text)
                    numbers_list.append(number)

                except ElementNotInteractableException:
                    continue

                if number.get_attribute('class') == "last-of-list":
                    flag = False
                    break
    print(count)

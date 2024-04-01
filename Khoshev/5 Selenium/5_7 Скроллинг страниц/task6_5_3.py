# Поиск чисел

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/scroll/2/index.html'
    driver.get(url=url)
    actions = ActionChains(driver)

    check_boxes = driver.find_elements('xpath', '//input[@type="checkbox"]')
    numbers = driver.find_elements('xpath', '//span')

    count = 0
    for check_box, number in zip(check_boxes, numbers):
        check_box.click()
        count += 0 if len(number.text) == 0 else int(number.text)

    print(count)

    # actions.click_and_hold(button).pause(hold_time).release(button).perform()

    # alert = driver.switch_to.alert
    # print(alert.text)

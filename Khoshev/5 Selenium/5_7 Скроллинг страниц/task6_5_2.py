# Операция 'Зелёный Лотос'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())


with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.7/5/index.html'
    driver.get(url=url)
    actions = ActionChains(driver)

    buttons = driver.find_elements('xpath', '//button[@class="timer_button"]')

    for button in buttons:
        hold_time = float(button.get_attribute('value'))
        actions.click_and_hold(button).pause(hold_time).release(button).perform()

    alert = driver.switch_to.alert
    print(alert.text)

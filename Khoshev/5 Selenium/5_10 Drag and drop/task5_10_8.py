# Движение слайдеров и тайный Код

import time
from selenium import webdriver
from selenium.webdriver import Keys

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/5.10/6/index.html'
    driver.get(url=url)
    driver.set_window_size(1600, 1800)

    time.sleep(3)
    sliders_locator = ('xpath', "//input[@class='volume-slider']")
    current_values_locator = ('xpath', "//span[@class='current-value']")
    target_values_locator = ('xpath', "//span[@class='target-value']")
    result_locator = ('xpath', '//p[@id="message"]')

    current_values = driver.find_elements(*current_values_locator)
    target_values = driver.find_elements(*target_values_locator)
    sliders = driver.find_elements(*sliders_locator)

    for slider, current_value, target_value in zip(sliders, current_values, target_values):
        # Получить текущее значение слайдера
        current_value = int(current_value.text)
        target_value = int(target_value.text)
        difference = current_value - target_value
        if difference > 0:
            for _ in range(difference):
                slider.send_keys(Keys.ARROW_LEFT)
        else:
            for _ in range(-difference):
                slider.send_keys(Keys.ARROW_RIGHT)

    time.sleep(3)

    print(driver.find_element(*result_locator).text)


# Увеличиваем значение
# slider.send_keys(Keys.ARROW_RIGHT)


# Уменьшаем значение
# slider.send_keys(Keys.ARROW_LEFT)

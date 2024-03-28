# Движение слайдеров и тайный Код

import time
from selenium import webdriver
from selenium.webdriver import Keys

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/5.10/6/index.html'
    driver.get(url=url)
    driver.set_window_size(1600, 1800)

    time.sleep(3)
    sliders_locator = ('xpath', "//div[@class='slider-container']")
    result_locator = ('xpath', '//p[@id="message"]')

    sliders = driver.find_elements(*sliders_locator)

    for slider in sliders:
        # Получить текущее значение слайдера
        current_value = slider.find_element('xpath', '/span[@class="current-value"]').text
        print(current_value)
        pass

    time.sleep(3)

    print(driver.find_element(*result_locator).text)


# Увеличиваем значение
# slider.send_keys(Keys.ARROW_RIGHT)


# Уменьшаем значение
# slider.send_keys(Keys.ARROW_LEFT)

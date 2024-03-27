import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)

    # Находим элементы
    draganddrop = driver.find_element(By.CLASS_NAME, "draganddrop")
    draganddrop_end = driver.find_element(By.CLASS_NAME, "draganddrop_end")

    # Выполняем перетаскивание
    ActionChains(driver).drag_and_drop(draganddrop, draganddrop_end).perform()
    time.sleep(5)

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.5/5/1.html'
    driver.get(url=url)
    contents = driver.find_elements('xpath', '//div[contains(@style, "background-color")]')

    for content in contents:
        span_color = content.find_element('tag name', 'span').text
        select_lst = content.find_element('tag name', 'select')
        select_colors = select_lst.find_elements('tag name', 'option')

        for select_color in select_colors:
            if select_color.get_attribute("value") == span_color:
                select_color.click()

        div_lst = content.find_element('tag name', 'div')
        div_colors = div_lst.find_elements('tag name', 'button')

        for div_color in div_colors:
            if div_color.get_attribute("data-hex") == span_color:
                div_color.click()

        check_box_button = content.find_element('xpath', 'input[@type="checkbox"]')
        check_box_button.click()

        input_text = content.find_element('xpath', 'input[@type="text"]')
        input_text.send_keys(span_color)

        check_page_button = content.find_element('xpath', 'button[contains(text(), "Проверить")]')
        check_page_button.click()

    check_final_button = driver.find_element('xpath', '//button[contains(text(), "Проверить все элементы")]')
    check_final_button.click()

    time.sleep(3)
    # Переключаемся на алерт
    alert = driver.switch_to.alert

    # Получаем текст с алерта
    alert_text = alert.text
    print(alert_text)

    time.sleep(5)

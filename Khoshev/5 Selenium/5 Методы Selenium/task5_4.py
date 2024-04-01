from selenium import webdriver

url = 'https://parsinger.ru/selenium/5.5/2/1.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    fields = browser.find_elements('xpath', '//input[@data-enabled="true"]')
    for field in fields:
        field.clear()
    browser.find_element('id', 'checkButton').click()
    # Переключаемся на алерт
    alert = browser.switch_to.alert

    # Получаем текст с алерта
    print(alert_text := alert.text)

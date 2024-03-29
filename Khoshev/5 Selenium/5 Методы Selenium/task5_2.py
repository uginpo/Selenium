from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=chrome')

url = 'https://parsinger.ru/selenium/5.5/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    fields = browser.find_elements('xpath', '//input[@class="text-field"]')
    for field in fields:
        field.clear()
    browser.find_element('id', 'checkButton').click()

    # Переключаемся на алерт
    alert = browser.switch_to.alert

    # Получаем текст с алерта
    print(alert_text := alert.text)

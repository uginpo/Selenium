# Check-boxes

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    url = 'https://parsinger.ru/selenium/5.5/3/1.html'
    driver.get(url=url)

    result = 0
    checkboxes = driver.find_elements('xpath', '//input[@type="checkbox"]')
    res_all = driver.find_elements('tag name', 'textarea')
    for element, res in zip(checkboxes, res_all):

        if element.is_selected():
            result += int(res.text)

    print(result)

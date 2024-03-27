from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = "https://vk.com"
driver.get(url=url)

first_title = driver.title
print(first_title)

new_url = "https://ya.ru"
driver.get(url=new_url)

second_title = driver.title
print(second_title)

driver.back()
assert driver.title == first_title, "Can't go back"

driver.refresh()
print(curr_url := driver.current_url)

driver.forward()
assert driver.current_url != curr_url, 'Ups, something wrong'

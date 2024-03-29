import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ru.wikipedia.org/w/index.php?returnto=Заглавная+страница&title=Служебная:Вход&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in')
driver.find_element('id', 'wpLoginAttempt').click()

time.sleep(3)
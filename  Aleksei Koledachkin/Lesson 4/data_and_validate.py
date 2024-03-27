import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org')

url = driver.current_url

title = driver.title
assert title == "Wikipedia"
print(driver.page_source)

time.sleep(1)
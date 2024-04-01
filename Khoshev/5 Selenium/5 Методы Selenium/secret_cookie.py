from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:

    url = "https://parsinger.ru/methods/3/index.html"
    driver.get(url=url)
    cookies = driver.get_cookies()
    result = sum([int(x['value']) for x in cookies])
    print(result)


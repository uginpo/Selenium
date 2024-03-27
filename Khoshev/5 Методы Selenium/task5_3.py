from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=chrome')

url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    cookies = browser.get_cookies()
    summa = 0
    for cookie in cookies:
        if int(cookie['name'].split('_')[2]) %2 ==0:
            summa += int(cookie['value'])

    print(summa)


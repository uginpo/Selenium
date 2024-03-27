from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=chrome')

url = 'https://parsinger.ru/methods/1/index.html'
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get(url=url)
    res = browser.find_element('id', 'result')
    while True:
        browser.refresh()
        res = browser.find_element('id', 'result')
        if res.text != "refresh page":
            print(res.text)
            break

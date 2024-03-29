import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())

with webdriver.Chrome(options=chrome_options, service=service) as driver:
    url = 'https://demoqa.com/upload-download'

    driver.get(url=url)

    time.sleep(3)
    upload_file = driver.find_element('xpath', '//input[@type="file"]')  # ключевой момент
    upload_file.send_keys(f'{os.getcwd()}/downloads/ironman.jpg')
    time.sleep(5)

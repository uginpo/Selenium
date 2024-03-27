from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://testautomationpractice.blogspot.com'
driver.get(url=url)

print(driver.find_element("class name", "wikipedia-icon"))
print(driver.find_element("id", "Wikipedia1_wikipedia-search-input"))
print(driver.find_element("class name", "wikipedia-search-input"))
print(driver.find_elements("tag name", "h2"))

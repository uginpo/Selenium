from selenium import webdriver

url = 'https://parsinger.ru/selenium/5.5/3/1.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    check_boxes = browser.find_elements('xpath', '//div[@class="parent"]/input[@type="checkbox"]')
    contents = browser.find_elements('xpath', '//div[@class="parent"]/textarea')

    result = sum([int(content.text) for check_box, content in zip(check_boxes, contents) if check_box.is_selected()])
    print(result)

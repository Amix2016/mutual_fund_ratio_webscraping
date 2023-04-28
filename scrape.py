import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s = Service("C:/Users/Transfo 01/OneDrive/Desktop/chromedriver.exe")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get('https://www.etmoney.com/mutual-funds/filter/mutual-fund-risk-ratios')

old_height = driver.execute_script('return document.body.scrollHeight')

while True:

    driver.find_element(by=By.XPATH, value='//*[@id="load_more_nav"]/span').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('ratios.html','w',encoding='utf-8') as f:
    f.write(html)





#html = driver.page_source

#with open('ratios.html','w', encoding='utf-8') as f:
#    f.write(html)
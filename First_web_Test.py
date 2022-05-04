"""
prerequisites  = https://www.youtube.com/
0. open URL
1 fill "Python from zero to hero" in search field
2 click the search button
3 verify that element == Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE] by
XPATH = '//*[@id="container"]/h1/yt-formatted-string'

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)


elem = "Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]"

url = ["https://www.google.com/"]

driver.get(url[0])

search_field = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

element = driver.find_element(By.XPATH, search_field)

element.send_keys(elem)

button = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]'

element_button = driver.find_element(By.XPATH, button)

time.sleep(1)

element_button.click()

res_url = '//*[@id="rso"]/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/h3/a/h3'

res = driver.find_element(By.XPATH, res_url)

res.click()

time.sleep(1)

if driver.find_element(By.XPATH, '//*[@id="container"]/h1/yt-formatted-string'):
    print('1')
else:
    assert print('Some text')


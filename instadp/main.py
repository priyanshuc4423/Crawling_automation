from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
CHROMECAST = "C:\DEVELOPMENT\chromedriver.exe"
IG_USERNAME = input('which user dp you want ?')

driver = webdriver.Chrome(CHROMECAST)
driver.get('https://www.instagram.com')
time.sleep(2)
login_username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
login_username.send_keys('arrogant_is_my_name')

login_password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
login_password.send_keys('9866560247')


login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login_button.click()
time.sleep(4)
not_now = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
not_now.click()
time.sleep(3)
not_now_returns = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now_returns.click()
time.sleep(2)
search_box = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search_box.send_keys(F'{IG_USERNAME}')

time.sleep(2)
select_username = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div/div/div')
select_username.click()
time.sleep(2)

username_dp = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/div/div/div/button/img').get_attribute('src')
response = requests.get(url=username_dp,headers = {'User-Agent': 'Mozilla/5.0'}).content

time.sleep(2)
with open(F'images/{IG_USERNAME}.png',mode='wb') as file:
    file.write(response)

driver.close()
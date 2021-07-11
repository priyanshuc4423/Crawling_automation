from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
Chromecast = 'C:\DEVELOPMENT\chromedriver.exe'


USERNAME = input("please give your facebook username")
PASSWORD = input("please give Facebook password")

conn = webdriver.Chrome(Chromecast)

conn.get('https://tinder.com/')
time.sleep(2)
login = conn.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(1)

try:
    facebook_login = conn.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()
except NoSuchElementException:
    more_option = conn.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/button')
    more_option.click()
    facebook_login = conn.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()
time.sleep(2)
base = conn.window_handles[0]
fb_login_page = conn.window_handles[1]

conn.switch_to.window(fb_login_page)

email = conn.find_element_by_name('email')
email.send_keys(f'{USERNAME}')

password = conn.find_element_by_name('pass')
password.send_keys(f'{PASSWORD}')

fb_login = conn.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
fb_login.click()
time.sleep(5)
conn.switch_to.window(base)
location_allow = conn.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(2)
disabled_notification = conn.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
disabled_notification.click()

for x in range(100):
    time.sleep(3)
    try:

        like = conn.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like.click()
    except NoSuchElementException:
        no_superlike = conn.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
        no_superlike.click()





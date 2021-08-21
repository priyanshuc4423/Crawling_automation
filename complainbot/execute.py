from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
CHROMECAST = 'C:\DEVELOPMENT\chromedriver.exe'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMECAST)
        self.down = 0
        self.up =0

    def tweet_at_provider(self):
        time.sleep(2)
        self.driver = webdriver.Chrome(CHROMECAST)
        self.driver.get('https://twitter.com/')
        time.sleep(2)
        self.login = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        self.login.click()
        time.sleep(1)

        self.user_id = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        self.user_id.send_keys(input('write your email id'))

        self.password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        self.password.send_keys(input('write your password'))

        self.access = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        self.access.click()
        time.sleep(2)
        self.tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        self.tweet.send_keys(f'HOW DARE @ACTFibernet provide me with {self.up} when those people promised with 80mbps #cancelactfibernet')
        time.sleep(1)
        self.body = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]')
        self.body.click()
        time.sleep(1)
        self.tellthem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        self.tellthem.click()
        time.sleep(2)
        self.driver.close()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        self.go = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go.click()
        time.sleep(45)
        self.up = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        self.down = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        self.driver.close()


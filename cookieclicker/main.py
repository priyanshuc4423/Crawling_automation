from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import timer
import threading
import time
DRIVER_PATH = "C:\DEVELOPMENT\chromedriver.exe"








connection = webdriver.Chrome(DRIVER_PATH)
connection.get("https://orteil.dashnet.org/cookieclicker/")
def clickitems():

    for x in range(17,-1,-1):
        cookieclicker.click()
        try:
            x = connection.find_element_by_id(f"product{x}")
            x.click()
        except:
            pass


timeout = time.time() +5
end_time = time.time() +5*60

cookieclicker = connection.find_element_by_id("bigCookie")
condition = True
while(condition):

    cookieclicker.click()


    if time.time() > timeout:
        clickitems()
        timeout +=5
    if time.time() > end_time:
        condition = False







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


DRIVER_PATH = "C:\DEVELOPMENT\chromedriver.exe"

conn = webdriver.Chrome(DRIVER_PATH)

conn.get("https://www.linkedin.com/home")

signin = conn.find_element_by_xpath("/html/body/nav/div/a[2]")
signin.click()
time.sleep(2)
username = conn.find_element_by_name("session_key")
username.send_keys("dontchallangeme13@gmail.com")

password = conn.find_element_by_name("session_password")
password.send_keys("Monthan@123")

login = conn.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()
# time.sleep(5)

# jobs = conn.find_element_by_xpath('//*[@id="ember31"]')
# jobs.click()

time.sleep(5)
whatjob = conn.find_element_by_xpath('//*[@id="ember25"]/input')
whatjob.send_keys("Python Developer")
whatjob.send_keys(Keys.ENTER)
time.sleep(5)
button = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/section/div/nav/div/div[1]/div/div[2]/ul/li[3]/button')
button.click()
time.sleep(5)
remote = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/section/div/div/div/div[1]/div/div[2]/ul/li[7]/div')
remote.click()
time.sleep(5)
easyapply = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/section/div/div/div/div[1]/div/div[2]/ul/li[8]/div')
easyapply.click()
time.sleep(5)
# dateposted = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/section/div/div/div/div[1]/div/div[2]/ul/li[5]/div')
# dateposted.click()
# # date24 = conn.find_element_by_xpath('//*[@id="ember1234"]')
# date24 = conn.find_element_by_xpath('//*[@id="artdeco-hoverable-artdeco-gen-57"]/div[1]/div/form/fieldset/div[1]/ul/li[4]')
# date24.click()
# results = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div')
# results.click()
file_element = []
file_element = conn.find_elements_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li')
print(len(file_element))

for x in range(1,len(file_element)):
    time.sleep(3)
    element_clicker = conn.find_element_by_xpath(f'/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[{x}]/div')
    element_clicker.click()
    time.sleep(2)
    apply = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div')
    apply.click()
    try:
        # results = conn.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div')
        # results.click()
        submit = conn.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button')
        submit.click()
        close = conn.find_element_by_xpath('/html/body/div[3]/div/div/button')
        close.click()
    except NoSuchElementException:
        close = conn.find_element_by_xpath('/html/body/div[3]/div/div/button')
        close.click()
        time.sleep(2)
        discard = conn.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/button[2]')
        discard.click()





# number = conn.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2505018937,9,phoneNumber~nationalNumber)"]')
# number.send_keys('12345678')
# submit = conn.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button')
# submit.click()
# close = conn.find_element_by_xpath('//*[@id="ember1169"]')
# close.click()


# location = conn.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember296"]')
# location.send_keys("India")


# search = conn.find_element_by_xpath('//*[@id="ember299"]/div[2]/input[2]')
# search.click()

conn.close()
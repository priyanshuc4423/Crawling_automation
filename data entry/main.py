from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
header = {
      'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0','Accept-Language':"en-US",
}
CHROMECAST = 'C:\DEVELOPMENT\chromedriver.exe'
response = requests.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D',headers = header)

all_price = []
all_address = []
soup = BeautifulSoup(response.content,'lxml')
all_price = soup.find_all(class_='list-card-price')
all_address = soup.find_all(class_ = 'list-card-addr')
all_imageurl = soup.select(selector='article div a')

driver = webdriver.Chrome(CHROMECAST)
driver.get('https://forms.gle/Q2P5g5CCpDvNyVAr8')
for x in range(len(all_price)):
      try:
            new_imageurl = all_imageurl[x]['href'].replace('https://www.zillow.com',"")
      except:
            pass
      time.sleep(4)
      Address = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
      Address.send_keys(f"{all_address[x].text}")
      pricepermonth = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
      pricepermonth.send_keys(f"{all_price[x].text}")
      link = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
      link.send_keys(f"https://www.zillow.com{new_imageurl}")
      submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
      submit.click()
      time.sleep(2)
      backtomainpage = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
      backtomainpage.click()
# print(soup)


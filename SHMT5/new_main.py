import bs4
import requests
from selenium import webdriver


CHROME = "C:\DEVELOPMENT\chromedriver.exe"
for i in range(1,3):
    try:
        f = open("list.csv",encoding='utf-8')
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['name', 'Photo', 'about', 'degree','phone','email','address','specialization','yearofexperience','language','rating','clinicname','timings','onlinebooking','consultonline','linktoprofile']]
    reponse = requests.get(f'https://www.practo.com/Thiruvananthapuram/hospitals/ayurveda-hospitals?page={i}')
    soup = bs4.BeautifulSoup(reponse.text,'html.parser')
    names = soup.select('#container > div > div > div.pure-g.o-page-container.c-listing > div.pure-u-18-24.c-listing__left > div > div > div > div > div.pure-g.c-card__body.u-spacer--bottom-less > div.pure-u-18-24 > div > div.o-media__body.u-cushion--right > div > a ')
    name = [ f"https://www.practo.com{na['href']}" for na in names]
    for link in name:
        conn = webdriver.Chrome(CHROME)
        conn.get(link)
        time = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/p[2]/span')
        print(time.text)
        conn.close()
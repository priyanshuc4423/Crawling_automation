import requests
import csv
import bs4
from selenium import webdriver

CHROME = "C:\DEVELOPMENT\chromedriver.exe"
def csv_data():
    try:
        with open(f"practo.csv", 'a', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)
    except:
        with open(f"practo.csv", 'w', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)



for i in range(1,12):
    name_list = []
    try:
        f = open("practo.csv",encoding='utf-8')
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['type','name', 'Photo', 'about','contactname','phone','email','address','city','state','county','Discipline','Amenities','language','rating','votes','timings','Mode of Payment','onlinebooking','Year Established','Linkedin','linktoprofile']]
    reponse = requests.get(f'https://www.practo.com/Nashik/hospitals/ayurveda-hospitals?page={i}')
    soup = bs4.BeautifulSoup(reponse.text,'html.parser')
    city = 'Nashik'
    state = 'Maharashtra'
    names = soup.select('#container > div > div > div.pure-g.o-page-container.c-listing > div.pure-u-18-24.c-listing__left > div > div > div > div > div.pure-g.c-card__body.u-spacer--bottom-less > div.pure-u-18-24 > div > div.o-media__body.u-cushion--right > div > a ')
    name = [ f"https://www.practo.com{na['href']}" for na in names]
    names = soup.select('div > div.pure-g.c-card__body.u-spacer--bottom-less > div.pure-u-18-24 > div > div.o-media__body.u-cushion--right > div > a > h2')
    name_list = [nam.text for nam in names]
    i = 0
    print(name_list)
    for link in name:
        reponse = requests.get(link)
        soup = bs4.BeautifulSoup(reponse.text,'html.parser')
        try:
            image = soup.select('div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-4-24 > img')
            new_image = image[0]['src']
        except:
            try:
                image = soup.select('//*[@id="container"]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]/img')
                new_image = image[0]['src']
            except:
                new_image = 'null'

        conn = webdriver.Chrome(CHROME)
        conn.get(link)
        Amenities = 'null'
        YearEstablished = 'null'
        try:
            click = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[3]/div[1]/div/button')
            click.click()
        except:
            pass

        try:
            new_name = soup.select('# container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > div:nth-child(1) > h1')
            new_new_name = new_name[0].text
        except:
            try:
                 new_name = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > h1 > span')
                 new_new_name = new_name[0].text
            except:
                 new_new_name = 'null'

        if new_new_name == "null":
            new_new_name = name_list[i]

        try:
            new_rating = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/span[1]')
            new_new_rating = new_rating.text
        except:
            try:
                new_rating = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/span[1]')
                new_new_rating = new_rating.text
            except:
                new_new_rating ='null'
        try:
            votes = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/span')
            votes = votes.text
        except:
            votes = 'null'

        try:
            new_address = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/p')
            new_new_address = new_address.text
        except:
            try:
                new_address =soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > h2')
                new_new_address = new_address[0].text
            except:
                new_address = 'null'
                new_new_address = 'null'

        try:
            services = conn.find_element_by_css_selector('#react-tabs-462943 > div > div:nth-child(1) > div.pure-g.u-spacer--top > div.pure-u-1-2 > div > div:nth-child(1) > a > span')
            #service = [ser.text for ser in services]
            services = services[0].text
        except:
            services = 'null'
        try:
            about = conn.find_element_by_css_selector('#react-tabs-462943 > div > div:nth-child(1) > div:nth-child(2) > div > p')
            new_about = about[0].text
        except:
            try:
                about = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/p')
                new_about = about.text
            except:
                about = 'null'
                new_about = about
        type = 'Ayurveda'
        lang = 'eng,hindi'
        country = 'India'
        specialization = 'MBBS'

        try:
            phone = conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/div/div/div[2]')
            phone = phone.text
        except:
            phone = "null"

        try:
            timming =  conn.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]')
            timming = timming.text
        except:
            timming = 'null'

        onlinebooking = link
        consultonline = link
        linktoprofile = link
        conn.close()
        i+=1
        csv_datas.append([type,new_new_name,new_image,new_about,'null',phone,'null',new_new_address,city,state,country,'null',Amenities,lang,new_new_rating,votes,timming,'null',link,'null','null',linktoprofile])
    csv_data()

import requests
import csv
import bs4


def csv_data():
    try:
        with open(f"list.csv", 'a', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)
    except:
        with open(f"list.csv", 'w', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)



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
        reponse = requests.get(link)
        soup = bs4.BeautifulSoup(reponse.text,'html.parser')
        try:
            new_name = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > div:nth-child(1) > h1')
            new_new_name = new_name[0].text
        except:
            try:
                new_name = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > h1 > span')
                new_new_name = new_name[0].text
            except:
                new_new_name = 'null'

        try:
            new_rating = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > div:nth-child(2) > div > div > div > span.common__star-rating__value')
            new_new_rating = new_rating[0].text
        except:
            try:
                new_rating = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > div.pure-u-12-24.c-profile__details > div > div > div > div > span.common__star-rating__value')
                new_new_rating = new_rating[0].text
            except:
                new_new_rating ='null'
        try:
            new_address = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > div.pure-u-12-24.c-profile__details > h2.c-profile__details')
            new_new_address = new_address[0].text
        except:
            try:
                new_address = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-20-24 > h2')
                new_new_address = new_address[0].text
            except:
                new_address = 'null'
        try:
            image = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-4-24 > img')
            new_image = image[0]['src']
        except:
            try:
                image = soup.select('#container > div.o-page-container > div > div.pure-g.u-spacer--top > div.pure-u-18-24.u-cushion--large-bottom > div:nth-child(1) > div > div.pure-u-4-24 > img')
                new_image = image[0]['src']
            except:
                image = 'null'
        try:
            services = soup.select('#react-tabs-462943 > div > div:nth-child(1) > div.pure-g.u-spacer--top > div.pure-u-1-2 > div > div:nth-child(1) > a > span')
            #service = [ser.text for ser in services]
            services = services[0].text
        except:
            services = 'null'
        try:
            about = soup.select('#react-tabs-462943 > div > div:nth-child(1) > div:nth-child(2) > div > p')
            new_about = about[0].text
        except:
            try:
                about = soup.select('#react-tabs-455481 > div > div:nth-child(1) > div:nth-child(2) > div.pure-u-2-3 > p')
                new_about = about[0].text
            except:
                about = 'null'
                new_about = about
        specialist = 'Ayurveda'
        lang = 'eng,hindi'
        number = 'null'
        specialization = 'MBBS'

        try:
            timming = soup.select('#react-tabs-455481 > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div > div > div > div > p.timings__time > span')
            timming = timming[0].text
        except:
            timming = 'null'

        onlinebooking = link
        consultonline = link
        linktoprofile = link

        csv_datas.append([ new_new_name, new_image, new_new_address, specialization, number, 'null', new_new_address, specialist, 'null',
         lang, new_new_rating, new_new_name, timming, onlinebooking, consultonline, linktoprofile])
    csv_data()

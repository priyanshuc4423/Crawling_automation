import requests
import bs4
import csv

def csv_data():
    try:
        with open(f"list.csv", 'a', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)
    except:
        with open(f"list.csv", 'w', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)


for i in range(1,6):
    try:
        f = open("list.csv",encoding='utf-8')
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['name', 'Photo', 'about', 'degree','phone','email','address','specialization','yearofexperience','language','rating','clinicname','timings','onlinebooking','consultonline','linktoprofile']]
    response = requests.get(f'https://en.bookimed.com/doctors/country=germany/page={i}/')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    names = soup.select('div.doctor-new-card__doctor > div.doctor-new-card__general > a')
    name = [ nam.text for nam in names]
    link = [nam['href'] for nam in names]
    expertises = soup.select('div.doctor-new-card__doctor > div.doctor-new-card__clinic > div.doctor-new-card__doctor-direction > span')
    expert = [ ex.text for ex in expertises]
    addresses = soup.select(' div.doctor-new-card__desc > div.doctor-new-card__description > div.doctor-new-card__clinic-address')
    address = [ add.text for add in addresses]
    images = soup.select(' div.doctor-new-card__poster > img')
    image = [img['content'] for img in images]
    descs = soup.select('div.doctor-new-card__desc > div.doctor-new-card__description > div.doctor-new-card__description-text > span')
    desc = [de.text for de in descs]
    degree = 'MBBS'
    phone = 'null'
    email = 'null'
    experience = 'null'
    lang = 'german,english'
    raing = 'null'
    clinicname = 'null'
    timmings = 'null'
    onlinebooking = 'null'
    consult = 'null'

    csv_datas.append(
        [name, image, desc, degree, phone, email, address,expert, experience, lang, raing,
         clinicname, timmings, onlinebooking, consult, link])
    csv_data()
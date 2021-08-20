import requests
import bs4
import csv



def csv_data():
    try:
        with open(f"list.csv", 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)
    except:
        with open(f"list.csv", 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)

name = []
address = []
for i in range(1,10):
    try:
        f = open("list.csv")
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['name', 'Photo', 'about', 'degree','phone','email','address','specialization','yearofexperience','language','rating','clinicname','timings','onlinebooking','consultonline','linktoprofile']]
    response = requests.get(url=f'https://australiandoctorsdirectory.com.au/doctors?page={i}&limit=1000&distance=2')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    links = []
    links = soup.select('div.listing > div.listing-header > a')
    link = [ f"https://australiandoctorsdirectory.com.au/{li['href']}" for li in links]
    for li in link:
        response = requests.get(li)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        try:
            new_name = soup.select('div.profile-limited-description > h1')[0].text
        except:
            new_name = 'null'
        try:
            new_phone = soup.select('div.profile-limited-contact')[0].text
        except:
            new_phone = 'null'
        photo = 'null'
        try:
            new_about = soup.select('#container > div.grid > div > div.profile-limited-description > p:nth-child(4)')[0].text
        except:
            new_about = 'null'
        degree = 'Medical Doctor'

        email = 'null'
        try:
            new_special = soup.select('#container > div.grid > div > div.profile-limited-description > p:nth-child(3)')[0].text
        except:
            new_special = ''
        try:
            new_address = soup.select('#container > div.grid > div > div.profile-limited-description > p:nth-child(2)')[0].text
        except:
            new_address = 'null'
        address.append(new_special)
        experience = 'null'
        lang = 'english'
        clinicname = 'null'
        timmings = 'null'
        onlinebooking = 'null'
        consult = 'null'
        raing ='null'
        linktoprof = f'{li}'
        csv_datas.append([new_name,photo,new_about,degree,new_phone,email,new_address,new_special,experience,lang,raing,clinicname,timmings,onlinebooking,consult,linktoprof])

    csv_data()

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


for i in range(1,52):
    try:
        f = open("list.csv",encoding='utf-8')
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['name', 'Photo', 'about', 'degree','phone','email','address','specialization','yearofexperience','language','rating','clinicname','timings','onlinebooking','consultonline','linktoprofile']]
    response = requests.get(f'https://www.vaidam.com/doctors/germany?page={i}')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    links = soup.select(' div.col-sm-8.col-md-9.col-xs-12 > div.view.view-search-solr.view-id-search_solr.view-display-id-page.view-dom-id-2902640fc9d7049c793e168f267d6001 > div.view-content > div > ul > li > div > div > div.list-card-info > div.section-2.clearfix > div > div > div > h2 > a')
    link = [li['href'] for li in links]
    for li in link:
        response = requests.get(li)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        images = soup.select('#newmain > div.containerreplace > div > div.col-md-3.col-xs-12.fix-point.sidebar-left > div.wrap-inner.clearfix > div.clearfix.avatar > img')
        image = images[0]['src']
        names = soup.select('#newmain > div.containerreplace > div > div.col-md-9.col-xs-12.wrap-affix > div:nth-child(1) > div.col-md-6.col-xs-12.nopad > h1')
        try:
            name = names[0].text
        except:
            name = "null"
        specialities = soup.select('#newmain > div.containerreplace > div > div.col-md-9.col-xs-12.wrap-affix > div:nth-child(1) > div.col-md-6.col-xs-12.nopad > h4')
        try:
            expert = specialities[0].text
        except:
            expert = "null"
        location = soup.select('#newmain > div.containerreplace > div > div.col-md-9.col-xs-12.wrap-affix > div:nth-child(1) > div.col-md-6.col-xs-12.nopad > span > p > span')
        try:
            address = location[0].text
        except:
            address = 'null'
        degree = 'MBBS'
        phone = 'null'
        email = 'null'
        experience = 'null'
        raing = 'null'
        clinicname = 'null'
        timmings = 'null'
        onlinebooking = 'null'
        consult = 'null'
        new_link = li
        description = soup.select('#about-doctor > div > div.rich-editor.margin10-bottom.clearfix.lessDesc15479 > ul > li:nth-child(1)')
        try:
            desc = description[0].text
        except:
            desc = 'NULL'
        lang = 'Germany,english'
        try:
            csv_datas.append(
                [name, image, desc, degree, phone, email, address, expert, experience, lang, raing,
                 clinicname, timmings, onlinebooking, consult, new_link])
        except IndexError:
            pass
    csv_data()

import requests
import bs4
import csv
total_link = []




def csv_data():
    try:
        with open(f"placidway.csv", 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)
    except:
        with open(f"placidway.csv", 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_datas)


for i in range(1,46):
    response = requests.get(url = f'https://www.placidway.com/search-medical-doctors/All/Thailand/{i}')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    links = soup.select('div.listing-item-inner > a')
    link = [linked['href'] for linked in links]
    header = soup.select(' div.listing-item-inner > a > h3')
    head = [ heads.text for heads in header]
    locations = soup.select('div.clearfix > h4:nth-child(2)')
    loaction = [locat.text for locat in locations]
    specalities = soup.select("div.clearfix > h4:nth-child(1)")
    specality = [special.text for special in specalities]
    total_link.append(link)

for links in total_link:
    for link in links:
        try:
            f = open("placidway.csv")
            csv_datas = []
            f.close()
        except IOError:
            csv_datas = [['name', 'address', 'image', 'contact field']]
        response = requests.get(url=f"https://www.placidway.com{link}")
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        title = soup.select('div.listing-titlebar-title > h1')
        link = f"https://www.placidway.com{link}"
        try:
            paragraph = soup.select('div.listing-titlebar-title > p.listing-address')
        except:
            paragraph = ""
        try:
            image = soup.find(class_ ='listing-titlebar-title').select('img')
        except:
            image = ''
        try:
            new_para = paragraph[0].text.replace("\n","")
        except:
            new_para = paragraph[0].text

        csv_datas.append([title[0].text,new_para,f"https://www.placidway.com{image[0]['src']}",link])

    csv_data()

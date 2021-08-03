import requests
import bs4


for i in range(1,2):
    try:
        f = open("placidway.csv")
        csv_datas = []
        f.close()
    except IOError:
        csv_datas = [['name', 'address', 'image', 'contact field']]
    response = requests.get(url = f'https://www.bangkokhospital.com/en/doctor?page={i}')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    title = soup.select('div.doctor-detail > div.doctor-image > div')
    print(title)


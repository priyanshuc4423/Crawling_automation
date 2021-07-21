import requests
from bs4 import BeautifulSoup
import csv


class Links():
    def __init__(self):
        self.response = requests.get('https://docplus.online/')
        self.soup = BeautifulSoup(self.response.text,'html.parser')
        self.links = []
    def get_data(self,diseases):
        for disease in diseases:
            url = f'https://docplus.online/doctors?diseases={disease}'
            self.links.append(url)
            self.response = requests.get(url)
            self.soup = BeautifulSoup(self.response.text,'html.parser')
            self.footerlinks = self.soup.find_all('a')
            # print(self.footerlinks)
            for footerlink in self.footerlinks:
                try:
                    hre = footerlink.attrs['href']
                    if hre.startswith("/"):
                        new_link = f'https://docplus.online{hre}'
                        if new_link not in self.links:
                            self.links.append(new_link)
                except:
                    pass



    def give_data(self):
        with open('links.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(self.links)



    def diseases(self):
        diseases = []

        self.response = requests.get('https://server.docplus.online/doctors/get/specialties')
        self.data = self.response.json()['data']
        for item in self.data:
            new_diseases = item['name']
            diseases.append(new_diseases)
        self.get_data(diseases)




a = Links()
a.diseases()
a.give_data()
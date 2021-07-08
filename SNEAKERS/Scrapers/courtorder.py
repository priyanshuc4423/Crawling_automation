import requests
import csv
from bs4 import BeautifulSoup

class Courtorder:
    def __init__(self,url):
        self.csv_datas = [['name','product_id','price','brand','age','images','color','shoes sizes']]

        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
        self.attrs = {}
    def colour(self,handlerid):

        shoe_url = f'https://courtorder.co.za/collections/sneakers/products/{handlerid}.js'
        self.res = requests.get(headers = self.header,url=shoe_url)

        self.color = self.res.json()['description']
        soup = BeautifulSoup(self.color,'html.parser')
        self.key_elemets = soup.select('div > strong')
        self.key_element = [element.text for element in self.key_elemets]
        self.value_elements = soup.select("div > span")
        self.value_element = [element.text for element in self.value_elements]
        self.attrs = dict(zip(self.key_element,self.value_element))
        return self.attrs






    def get_data(self):
        self.response = requests.get(headers=self.header,url=self.url)
        print(self.response.status_code)
        self.data = self.response.json()
        # print(self.data)


    def csv_data(self):
        # self.datalists = name
        with open("courtorder.csv",'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.csv_datas)

    def datas(self):
        for item in self.data['products']:
            self.name = item['title']
            self.product_id = item['variants'][0]['product_id']
            self.brand = item['vendor']
            self.pricerange = item['variants'][0]['price']
            self.images = [image['src'] for image in item['images']]
            self.shoe = item['variants'][0]['option1']
            self.handle = item['handle']
            self.new_dict = self.colour(self.handle)
            try:
                self.color = self.new_dict['COLOUR:\xa0']
            except:
                self.color = ""
            try:
                self.age = self.new_dict['GENDER:']
            except:
                self.age = ""

            self.csv_datas.append([self.name,self.product_id,self.pricerange,self.brand,self.age,self.images,self.color,self.shoe])
        self.csv_data()




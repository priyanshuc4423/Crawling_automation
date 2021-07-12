import requests
import csv
from bs4 import BeautifulSoup
import logging
import datetime

class Courtorder:
    def __init__(self,url):
        self.list_colour= []
        self.number = []
        try:
            f = open("./data/courtorder.csv")
            self.csv_datas = []
            f.close()
        except IOError:
            self.csv_datas = [['name','product_id','price','brand','age','images','color','shoes sizes']]


        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
        self.attrs = {}
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            level=logging.INFO,
                            filename="./logs/courtorder.log",
                            filemode="a"
                            )
        logging.info('Admin logged in')

    def colour(self,handlerid):

        shoe_url = f'https://courtorder.co.za/collections/sneakers/products/{handlerid}.js'
        self.res = requests.get(headers = self.header,url=shoe_url)

        color = self.res.json()['description']
        soup = BeautifulSoup(color, 'html.parser')

        key_elemets = soup.select('div > strong')

        key_element = [element.text for element in key_elemets]

        value_elements = soup.select("div > span")
        new_value_elements = soup.select('div')

        new_value_elements = [element.text for element in new_value_elements]

        return new_value_elements






    def get_data(self):
        self.response = requests.get(headers=self.header,url=self.url)
        print(self.response.status_code)
        self.data = self.response.json()
        # print(self.data)


    def csv_data(self):
        # self.datalists = name
        with open("./data/courtorder.csv",'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.csv_datas)

        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Admin logged out')



    def datas(self):
        for item in self.data['data']['items']:
            self.name = item['title']
            print(self.name)
            self.age = 'none'
            self.color = 'none'
            self.product_id = item['id']
            self.brand = item['vendor']
            self.pricerange = item['variants'][0]['price']
            self.images = [image['url'] for image in item['images']]
            try:
                self.shoe = item['options'][0]['values']
            except:
                self.shoe = ""

            self.handle = item['urlName']
            self.new_dict = self.colour(self.handle)
            for element in self.new_dict:
                if "COLOUR" in element:
                    if "PRODUCT CODE" in element or 'RELEASE DATE' in element or 'GENDER' in element:
                        pass

                    elif "COLOUR: 12/01/2019" in element:
                        self.color = 'none'
                    else:
                        self.color = element.replace("COLOUR:", "").strip()








                elif "GENDER" in element:
                    if "WOMEN" in element:
                        self.age = "WOMEN"
                    elif "MEN" in element:
                        self.age = 'MEN'
                    else:
                        pass



            self.csv_datas.append([self.name,self.product_id,self.pricerange,self.brand,self.age,self.images,self.color,self.shoe])
        self.csv_data()




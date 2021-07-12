import requests
import csv
import logging
import datetime
class Superbalist:
    def __init__(self,url):
        try:
            f = open("./data/superbalist.csv")
            self.csv_datas = []
            f.close()
        except IOError:
            self.csv_datas = [['name', 'product_id', 'price', 'brand', 'age', 'images', 'color', 'shoes sizes']]



        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            level=logging.INFO,
                            filename="./logs/superbalits.log",
                            filemode="a"
                                )
        logging.info('Admin logged in')

    def replace_image(self,images):
        self.images_lists = images
        self.images_lists = [image.replace('/{size}filters:quality({quality}):format({extension})',"") for image in self.images_lists]
        return self.images_lists

    def get_data(self):
        self.content = True
        self.number = 1


        while self.content :
            self.response = requests.get(headers=self.header,url=self.url+f"&page={self.number}")
            print(self.response.status_code)
            self.data = self.response.json()
            print(self.number)
            if self.data['search']['data'] != []:
                self.number +=1
                self.datas()
            else:
                self.csv_data()
                self.content = False


    def shoesize(self,par):
        id = par
        self.sizes_list = []
        self.info = self.additional_info(id)
        self.shoes = self.data['page_impression']['metadata']['variations']
        # self.length = len(self.shoes)
        # i = 0
        try:
            for shoe in self.shoes.values():
                self.sizes_list.append(shoe['fields']['Size'])
        except:
            self.sizes_list = 'not available'

        return self.sizes_list
        # return self.sizes_list

    def additional_info(self,id):
        self.id = id
        self.add_url = f'https://superbalist.com/api/public/products/{self.id}'
        self.res = requests.get(headers=self.header,url=self.add_url)
        self.data = self.res.json()
        return self.data

        # return self.size

    def genders(self,id):
        id = id
        self.info = self.additional_info(id)
        try:
            self.gender = self.info['og_data']['product:category']
            self.dataset = self.gender
        except:
            self.gender = "not available"
        return self.gender

    def colour(self,id):
        id = id
        self.info = self.additional_info(id)
        try:
            self.col = self.info['product']["data_nice"]['Colour']
        except:
            self.col = "not available"
        return self.col

    def csv_data(self):
        try:
            with open(f"./data/superbalist.csv", 'a',newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.csv_datas)
        except:

            with open(f"./data/superbalist.csv",'w',newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.csv_datas)

        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Admin logged out')


    def datas(self):
        for item in self.data['search']['data']:
            self.name = item['short_name']
            print(self.name)
            self.product_id = item['id']
            self.age = self.genders(self.product_id)
            self.shoe = self.shoesize(self.product_id)

            self.pricerange = item['price_range']['min']['price']
            self.brand = item['designer_name']
            self.images = [item['asset']['base_ssl_url'],item['asset']['base_url']]
            self.images = self.replace_image(self.images)
            self.color = self.colour(self.product_id)

            self.csv_datas.append([self.name,self.product_id,self.pricerange,self.brand,self.age,self.images,self.color,self.shoe])






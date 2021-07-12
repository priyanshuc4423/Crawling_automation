import requests
import csv
import logging
import datetime

class Sportscene:
    def __init__(self,url):
        try:
            f = open("./data/sportscene.csv")
            self.csv_datas = []
            f.close()
        except IOError:
            self.csv_datas = [['name', 'product_id', 'price', 'brand', 'age', 'images', 'color', 'shoes sizes']]

        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            level=logging.INFO,
                            filename="./logs/sportscene.log",
                            filemode="a"
                            )
        logging.info('Admin logged in')


    def shoesizes(self,productid):
        self.shoe_sizes = []
        try:
            shoe_url = f'https://www.sportscene.co.za/product/generateProductJSON.jsp?productId={productid}'
            self.res = requests.get(headers = self.header,url=shoe_url)
            self.sizes = self.res.json()['sizes']
            self.shoe_sizes = [size['name'] for size in self.sizes]
        except:
            self.shoe_sizes = []

        return self.shoe_sizes

    def get_data(self):
        self.response = requests.get(headers=self.header,url=self.url)
        print(self.response.status_code)
        self.data = self.response.json()


    def csv_data(self,name):
        try:
            with open(f"./data/sportscene.csv",'a',newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.csv_datas)
        except:
            with open(f"./data/sportscene.csv",'w',newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.csv_datas)

        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Admin logged out')




    def datas(self):
        for item in self.data['data']['products']:
            self.name = item['name']
            print(self.name)
            self.namelist = self.name.split(" ")
            if "Women's" in self.namelist:
                self.age = 'women'
                self.dataname = 'women'
            elif 'Junior' in self.namelist:
                self.age = 'kid'
            else:
                self.age = 'men'
                self.dataname = 'men'
            self.product_id = item['productId']
            self.shoe = self.shoesizes(productid=item['productId'])
            self.pricerange = item['latestPriceRange']
            self.brand = item['brand']
            self.images = [item['defaultImages'],item['swapImage']]
            self.color = item['colors'][0]['name']
            self.csv_datas.append([self.name,self.product_id,self.pricerange,self.brand,self.age,self.images,self.color,self.shoe])
        self.csv_data(self.dataname)



import requests
import csv

class Sportscene:
    def __init__(self,url):
        self.csv_datas = [['name','product_id','price','brand','age','images','color','shoes sizes']]

        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
    def shoesizes(self,productid):
        self.shoe_sizes = []
        shoe_url = f'https://www.sportscene.co.za/product/generateProductJSON.jsp?productId={productid}'
        self.res = requests.get(headers = self.header,url=shoe_url)
        self.sizes = self.res.json()['sizes']
        self.shoe_sizes = [size['name'] for size in self.sizes]
        return self.shoe_sizes

    def get_data(self):
        self.response = requests.get(headers=self.header,url=self.url)
        print(self.response.status_code)
        self.data = self.response.json()


    def csv_data(self,name):
        self.datalists = name
        with open(f"sportscene_{self.datalists}.csv",'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.csv_datas)

    def datas(self):
        for item in self.data['data']['products']:
            self.name = item['name']
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



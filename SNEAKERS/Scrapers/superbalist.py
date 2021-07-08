import requests
import csv


class Superbalist:
    def __init__(self,url):
        self.csv_datas = [['name','product_id','price','brand','age','images','color','shoes sizes']]

        self.header =  {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.url = url
    def replace_image(self,images):
        self.images_lists = images
        self.images_lists = [image.replace('/{size}filters:quality({quality}):format({extension})',"") for image in self.images_lists]
        return self.images_lists

    def get_data(self):
        self.response = requests.get(headers=self.header,url=self.url)
        print(self.response.status_code)
        self.data = self.response.json()

    def shoesize(self,par):
        id = par
        self.sizes_list = []
        self.info = self.additional_info(id)
        self.shoes = self.data['page_impression']['metadata']['variations']
        # self.length = len(self.shoes)
        # i = 0
        for shoe in self.shoes.values():
             self.sizes_list.append(shoe['fields']['Size'])

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
        self.gender = self.info['og_data']['product:category']
        self.dataset = self.gender
        return self.gender

    def colour(self,id):
        id = id
        self.info = self.additional_info(id)
        self.col = self.info['product']["data_nice"]['Colour']
        return self.col

    def csv_data(self):

        with open(f"superbalist_{self.dataset}.csv",'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.csv_datas)

    def datas(self):
        for item in self.data['search']['data']:
            self.name = item['short_name']
            self.product_id = item['id']
            self.age = self.genders(self.product_id)
            self.shoe = self.shoesize(self.product_id)

            self.pricerange = item['price_range']['min']['price']
            self.brand = item['designer_name']
            self.images = [item['asset']['base_ssl_url'],item['asset']['base_url']]
            self.images = self.replace_image(self.images)
            self.color = self.colour(self.product_id)

            self.csv_datas.append([self.name,self.pricerange,self.brand,self.age,self.images,self.color,self.shoe])
        self.csv_data()





import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

shoe_url = f'https://courtorder.co.za/collections/sneakers/products/nike-air-max-95-greedy-2020.js'

res = requests.get(headers=header, url=shoe_url)

color = res.json()['description']
soup = BeautifulSoup(color, 'html.parser')

key_elemets = soup.select('div > strong')

key_element = [element.text for element in key_elemets]

value_elements = soup.select("div > span")
new_value_elements = soup.select('div')



new_value_elements = [element.text for element in new_value_elements]

for element in new_value_elements:
    if "COLOUR" in element:
        if "PRODUCT CODE" in element or 'RELEASE DATE' in element or 'GENDER' in element:
            pass
        else:
            # pass
            print(element.replace("COLOUR:","").strip())
    elif "GENDER" in element:
        if "MEN" in element:
            age = "MEN"

        elif "WOMEN" in element:
            age = 'WOMEN'
        else:
            pass




# attrs = dict(zip(key_element, value_element))
# print(attrs)
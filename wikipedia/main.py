import requests
import bs4
import csv

response = requests.get(url='https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = bs4.BeautifulSoup(response.text,'html.parser')

content = soup.select('#mw-content-text > div.mw-parser-output > table > tbody')

rows = content[0].find_all('tr')
data = []

csv_data = [['country','region','population','total percentage']]
for row in rows:
    try:
        data = row.select('td')
        country = data[0].find('a').text
        region = data[1].find('a').text
        population = data[2].text
        total_percentage = data[3].text


        csv_data.append([country,region,population,total_percentage])

    except:
        pass


with open("world_population.csv","w") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)


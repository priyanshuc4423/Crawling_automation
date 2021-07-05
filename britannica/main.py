import requests
import bs4
import csv

website = requests.get(url = 'https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = bs4.BeautifulSoup(website.text,'html.parser')

unorder_list = soup.select('.topic-list')[0].find_all('li')
philosphers_list =  [lists.find("a").attrs['href']  for lists in unorder_list]

csv_data = []


for philospher in philosphers_list[:5]:
    try:
        website = requests.get(url = f'{philospher}')

        soup = bs4.BeautifulSoup(website.text,'html.parser')

        name = soup.select_one('title').text
        topics = soup.select_one('.topic-identifier').text

        intro = soup.select_one('.topic-paragraph').text

        try:
            picture = soup.select_one('.fact-box-picture img ').attrs['src']
        except:
            picture = None

        try:

            date_of_birth = soup.find(attrs={'data-label':'born'}).get_text(separator ='|').split('|')[1]
            date_of_death = soup.find(attrs={'data-label':'died'}).get_text(separator='|').split('|')[1]
        except:
            date_of_death=None
            date_of_birth= None

        try:
            works = soup.find(attrs={'data-label':'notable works'}).get_text(separator='|').split('|')
            worked = [work.strip() for work in works[1:]]
        except:
            worked = None
        try:
            studies = soup.find(attrs={'data-label':'subjects of study'}).select_one('ul').select('li')
            study = [stud.text for stud in studies]
        except:
            study = None

        csv_data.append[[name,study,worked,date_of_death,date_of_birth,topics,intro]]
    except:
        csv_data = None

with open("philosphers.csv",'w') as file:
    write = csv.writer(file)
    write.writerows(csv_data)







import requests
import bs4

total_link = []
for i in range(1,46):
    response = requests.get(url = f'https://www.placidway.com/search-medical-doctors/All/Thailand/{i}')
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    links = soup.select('div.listing-item-inner > a')
    link = [f"https://www.placidway.com{linked['href']}" for linked in links]
    header = soup.select(' div.listing-item-inner > a > h3')
    head = [ heads.text for heads in header]
    locations = soup.select('div.clearfix > h4:nth-child(2)')
    loaction = [locat.text for locat in locations]
    specalities = soup.select("div.clearfix > h4:nth-child(1)")
    specality = [special.text for special in specalities]
    total_link.append(link)

for link in total_link[:1]:
    response = requests.get(url=f"{link}")
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    title = soup.select('div.listing-titlebar-title > h1')
    print(title)



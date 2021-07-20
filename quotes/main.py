import requests
from bs4 import BeautifulSoup


page = 1;
next_button = True

while next_button:
    website = requests.get(url = f'https://quotes.toscrape.com/page/{str(page)}/')
    soup = BeautifulSoup(website.text,'html.parser')
    quotes = soup.findAll(class_ = 'quote')
    for quote in quotes:
        quote_text = quote.find(class_ = 'text')
        quote_author = quote.find(class_ = 'author')
        quote_tags =  quote.select('.tag')
        quote_tag = [ x.text  for x in quote_tags]
        print(f'{quote_text.text}')
        print(f'{quote_author.text}')
        print(f"{quote_tag}")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    next_button = soup.select_one(".next > a")

    print(f"scraped page :-{page}")
    page += 1






# dict= {}
# for quote in quotes:
#     quote_text = quote.find(class_ = 'text')
#     quote_author = quote.find(class_ = 'author')
#     dict[f"{quote_author.text}"] = f'{quote_text.text}'
#
#
# print(dict)




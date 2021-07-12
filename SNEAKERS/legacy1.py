from scrapers import superbalist,courtorder
from scrapers.sportscene import Sportscene
from scrapers.courtorder import Courtorder
from scrapers.superbalist import Superbalist
import config
scene_URLS = ['https://www.sportscene.co.za/search/ajaxResultsList.jsp?N=280g&Nrpp=527&page=1&baseState=280g&cat=Sneakers&c=all','https://www.sportscene.co.za/search/ajaxResultsList.jsp?N=284v&Nrpp=498&page=1&baseState=284v&cat=Sneakers&c=all']
balist_URLS = ['https://superbalist.com/api/public/catalogue?department=men&category=shoes&subcategory=sneakers','https://superbalist.com/api/public/catalogue?department=women&category=shoes&subcategory=sneakers']
courtorder_url = 'https://courtorder.co.za/collections/sneakers/products.json'



def sportscene(scene_URL):
    url = scene_URL
    try:
        for i in url:
            scene = Sportscene(i)
            scene.get_data()
            scene.datas()
    except:
        scene = Sportscene(url)
        scene.get_data()
        scene.datas()

def sportbalist(balist_url):
    url = balist_url
    try:
        for i in url:
            scene = Superbalist(i)
            scene.get_data()
            scene.datas()
    except:
        scene = Superbalist(url)
        scene.get_data()
        scene.datas()


def court(court_url):
    url = court_url
    s = Courtorder(url)
    s.get_data()
    s.datas()



def genderfilter():
    if config.men == 'y':
      sportscene(scene_URL=scene_URLS[0])
      sportbalist(balist_URLS[0])
    elif config.women == 'women':
        sportscene(scene_URL=scene_URLS[1])
        sportbalist(balist_URLS[1])
    else:
        sportscene(scene_URLS)
        sportbalist(balist_URLS)
        court(courtorder_url)
def companyprefernece():
    if config.courtorder == "y":
        court(courtorder_url)
    elif config.balist == 'y':
        sportbalist(balist_URLS)
    elif config.scene == "y":
        sportscene(scene_URLS)
    else:
        sportscene(scene_URLS)
        sportbalist(balist_URLS)
        court(courtorder_url)


def websitefilter():

    if config.gender_filter == 'y' and config.company_preference == 'y':
        if config.courtorder == "y":
            if config.men == "y":
                pass
            elif config.women == 'y':
               pass
            else:
                court(courtorder_url)

        elif config.scene == 'y':

            if config.men == "y":
                sportscene(scene_URL=scene_URLS[0])
            elif config.women == 'y':
                sportscene(scene_URL=scene_URLS[1])
            else:
                sportscene(scene_URLS)
        elif config.balist == 'y':
            if config.men == "y":
                sportbalist(balist_URLS[0])
            elif config.women == 'y':
                sportbalist(balist_URLS[1])
            else:
                sportbalist(balist_URLS)
        else:
            sportbalist(balist_URLS)
            sportscene(scene_URLS)
            court(courtorder_url)
    elif config.gender_filter == 'y':
        genderfilter()
    elif config.company_preference == 'y':
        companyprefernece()
    else:
        sportbalist(balist_URLS)
        sportscene(scene_URLS)
        court(courtorder_url)



websitefilter()
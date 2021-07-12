import argparse
from scrapers.sportscene import Sportscene
from scrapers.courtorder import Courtorder
from scrapers.superbalist import Superbalist
from config import scene_URLS,balist_URLS,courtorder_url

def runcode():
    parser = argparse.ArgumentParser(description="which code do you want to run")
    parser.add_argument('code',metavar='code',type=str,help = "add the website name you want to scrape data from")
    args = parser.parse_args()
    code = args.code
    return code


def run(comlin_code):
    comlin = comlin_code


    if comlin == "sportscene":
        urls = scene_URLS
        for url in urls:
            scene = Sportscene(url)
            scene.get_data()
            scene.datas()
    elif comlin == 'superbalist':
        urls = balist_URLS
        for url in urls:
            scene = Superbalist(url)
            scene.get_data()
            # scene.datas()
    elif comlin == 'courtorder':
        url = courtorder_url
        s = Courtorder(url)
        s.get_data()
        s.datas()


value = runcode()
execscript = run(value)

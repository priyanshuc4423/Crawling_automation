import requests
import bs4
import time
import pandas as pd
from pandas.io.json import json_normalize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = 'C:\DEVELOPMENT\chromedriver.exe'

class jobs():
    def __init__(self,remote,location,easyapply,past24hrs):
        self.remote = remote
        self.location = location
        self.easyapply = easyapply
        self.past24hrs = past24hrs
    def getjobs(self):
        parameter = {
            'f_WRA' : f'{self.remote}',
            'f_AL': f'{self.easyapply}',
            'location':f'{self.location}',
            'keywords':'web scraping'

        }

        if self.past24hrs.lower() == 'true':
            GET = f'https://www.linkedin.com/jobs/search/?f_AL={self.easyapply}&f_TPR=r86400&f_WRA={self.remote}&keywords=web%20scraping&location={self.location}'
        else:
            GET = f'https://www.linkedin.com/jobs/search/?f_AL={self.easyapply}&f_WRA={self.remote}&keywords=web%20scraping&location={self.location}'
        connection = webdriver.Chrome(chrome)
        connection.get(url= GET)

        time.sleep(3)
        res = connection.execute_script('return document.documentElement.outerHTML')
        connection.quit()

        self.soup = bs4.BeautifulSoup(res,'html.parser')



        self.job_lists = self.soup.select_one('#main-content > section.two-pane-serp-page__results-list > ul')
        self.jobs_links = [job.find('a') for job in self.job_lists]
        self.links = [ link.attrs['href'] for link in self.jobs_links if link != -1]

        return self.links







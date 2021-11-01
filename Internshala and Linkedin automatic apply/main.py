from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import LINKEDIN


def linkedin(permission_linkedin):
    if permission_linkedin.lower() =='y' :
        remote = input("are you looking for remote job ?")
        easyapply = input('do you want easy apply as well')
        location = input('location ?')
        past24hrs = input('do you want the job posted from past 24hours ?')

        jobs_from_linkedin = LINKEDIN.jobs(remote =remote,easyapply= easyapply,location=location,past24hrs=past24hrs)

        value = jobs_from_linkedin.getjobs()
        print(value)


def internshala(permission_intern):
    if permission_intern == 'y':
        accepted_jobs = ['Scraping', 'Scrapping', 'automation', 'Automation', 'scraping', 'scrapping']
        CHROME = "C:\DEVELOPMENT\chromedriver.exe"
        apply = []
        conn = webdriver.Chrome(CHROME)
        for i in range(37):
            conn.get(
                f'https://internshala.com/internships/work-from-home-computer%20science-jobs/part_time-true/page-{i + 1}')
            job = []
            block = []
            try:
                close = conn.find_element_by_xpath('/html/body/div[1]/div[19]/div/div[1]/i')
                close.click()
            except:
                pass

            time.sleep(2)
            # /html/body/div[1]/div[20]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a
            total = conn.find_elements_by_class_name('internship_meta')
            time.sleep(2)
            job = conn.find_elements_by_css_selector('.heading_4_5  a')

            for i in job:
                a = i.text.split(" ")
                if a != "":
                    try:
                        if a[1] in accepted_jobs:
                            block.append(i.get_attribute('href'))
                            block.append(i.text)
                            apply.append(block)

                    except:
                        pass

        print(apply)
        conn.close()


permission = input('do you want jobs from linkedin as well ? please answer in y or n')
intern = input('do you want jobs from internshala as well ? please answer in y or n')
linkedin(permission)
internshala(intern)




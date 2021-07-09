import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
URL ="https://www.amazon.in/Gajraj-Knitted-Beanie-Women-Purple/dp/B07SNQHKJK/ref=cs_sr_dp_2?dchild=1&keywords=bean+cap&qid=1620273283&sr=8-2"
MY_EMAIL = "jameswang8667@gmail.com"
MY_PASSWORD = "Jambajuice@713"
http_header={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
    "X-Real-Ip":"183.83.39.179",
    "Cookie":"PHPSESSID=kgvi6jt99jk86n63osummq2fq7; _ga=GA1.2.1992581518.1620273355; _gid=GA1.2.152681127.1620273355",
    "Accept-Encoding":"gzip, deflate"

}

response = requests.get(url="https://www.amazon.in/Gajraj-Knitted-Beanie-Women-Purple/dp/B07SNQHKJK/ref=cs_sr_dp_2?dchild=1&keywords=bean+cap&qid=1620273283&sr=8-2",headers = http_header)


PAGE = response.text

soup = BeautifulSoup(PAGE,"lxml")
price =soup.find(name="span",id= "priceblock_ourprice")
real_price = price.getText().split()





if float(real_price[1]) < 300.00:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="priyanshuc4423@gmail.com",msg=f"Subject:PRICE DROPPED ON YOUR ITEM\n\nprice dropped please go to \n {URL}\n to buy now")
    connection.close()

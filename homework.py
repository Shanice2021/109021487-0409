import requests
from bs4 import BeautifulSoup


def urlsss(urls):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    r=requests.get(urls,headers=headers,verify=False)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml') #lxml = html.parser
    soup = soup.find('tbody')
    Ysoup = soup.find_all('p')
    Ysoup = str(Ysoup)
    Ysoup=Ysoup.replace('<p>',"")
    Ysoup=Ysoup.replace('</p>',"")
    Ysoup=list(Ysoup.split(','))
    for i in Ysoup:
        print(i)

urlsss('https://csie.asia.edu.tw/project/semester-100')
urlsss('https://csie.asia.edu.tw/project/semester-101')
urlsss('https://csie.asia.edu.tw/project/semester-102')
urlsss('https://csie.asia.edu.tw/project/semester-103')
urlsss('https://csie.asia.edu.tw/project/semester-104')
urlsss('https://csie.asia.edu.tw/project/semester-105')
urlsss('https://csie.asia.edu.tw/project/semester-1061')
urlsss('https://csie.asia.edu.tw/project/semester-107')
urlsss('https://csie.asia.edu.tw/project/108學年')

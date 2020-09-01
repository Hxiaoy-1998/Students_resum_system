import requests
import re
from bs4 import BeautifulSoup
import time
from lxml import etree








def getweather():
    url = 'http://tianqi.moji.com/'
    headers = {
        'Referer': 'http://tianqi.moji.com/',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
    }
    page_text = requests.get(url=url, headers=headers)

    html=BeautifulSoup(page_text.text, 'lxml')

    html=str(html)

    weather =re.findall(r'<div class="forecast clearfix">.*?<div class="hours">',html,re.S)

    weather = str(weather)

    weather = re.findall(r'<ul class="days clearfix">.*?</ul>',weather,re.S)

    weather = str(weather).split('</ul>')[0]

    weather = re.findall(r'<a.*?</strong>',weather,re.S)

    weather = str(weather).replace('\\n','')

    weather = str(weather).replace('\\r','')

    weather = str(weather).replace('\\','')

    weather = str(weather).replace('</li><li>','')

    weatherqian = str(weather).split('<img')[0]

    weatherhou = str(weather).split('<img')[1]

    weathers = weatherqian+'<img style="width: 40px;height: 35px"'+weatherhou

    weathers = str(weathers).replace("['",'')

    weathers = str(weathers).replace("']",'')

    return weathers



def getnews():
    url = 'https://mkt.51job.com/careerpost/default_res.php'
    headers = {
        'Referer': 'http://tianqi.moji.com/',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
    }
    page_text = requests.get(url=url, headers=headers)

    page_text.encoding = 'GBK'

    pagenews = BeautifulSoup(page_text.text, 'lxml')

    pagenews = str(pagenews)

    pagenews1 = re.findall(r'<div class="ctxt clearfix">.*?<div class="cmsg">',pagenews,re.S)

    pagenews1 = str(pagenews1).replace('\\n','')

    pagenews1 = str(pagenews1).split('<div class="bcon">')[0]

    pagenews1 = str(pagenews1).replace('<div class="ctxt clearfix">','<div class="ctxt clearfix" style="font-size: 17px; font-family: Gabriola">')

    pagenews1 = pagenews1+'</div>'

    pagenews2 = re.findall('<div class="bcon"><div class="btit at">.*?<div class="cmsg">',pagenews,re.S)

    pagenews2 = str(pagenews2).split('<div class="cmsg">')[0]

    pagenews2 = str(pagenews2).replace('\\n','')

    pagenews2 = pagenews2+'<div class="cmsg">'

    pagenews2 = str(pagenews2).replace('<div class="bcon"><div class="btit at">',' <div class="bcon"><div class="btit at" style="font-size: 17px; font-family: Gabriola">')

    pagenews3 = re.findall(r'<div class="container">.*?<div class="footer">',pagenews,re.S)

    pagenews3 = str(pagenews3).split('<div class="ebox clearfix">')[1]

    pagenews3 = str(pagenews3).split('<div class="e">')

    pagenews3 = str(pagenews3).replace('\\n','')

    pagenews3 = str(pagenews3).replace('\\', '')

    pagenews3 = str(pagenews3).split('<div class="htit">')[1]

    pagenews3 = '<div class="htit">'+pagenews3

    pagenews3 = str(pagenews3).replace("', '",'')

    pagenews3 = str(pagenews3).split('<ul class="dcon">')[1]

    pagenews3 = '<ul class="dcon">'+pagenews3

    pagenews3 = str(pagenews3).replace('</div>','')

    pagenews1 = str(pagenews1).replace("['",'')

    pagenews2 = str(pagenews2).replace("['",'')

    return pagenews1,pagenews2,pagenews3



def getphoto():
    url = 'https://mkt.51job.com/careerpost/default_res.php'
    headers = {
        'Referer': 'http://tianqi.moji.com/',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
    }
    page_text = requests.get(url=url, headers=headers)

    page_text.encoding = 'GBK'

    pagenews = BeautifulSoup(page_text.text, 'lxml')

    pagenews = str(pagenews)

    pagenews = re.findall(r'<div class="container">.*?<div class="dbox">',pagenews,re.S)

    pagenews = str(pagenews).replace("']",'')

    pagenews = str(pagenews).replace('\\n','')

    pagenews = str(pagenews).replace("['",'')

    pagenews = str(pagenews).split('<div class="acon">')[1]

    pagenews1 = str(pagenews).split('<div class="btxt">')[0]

    pagenews2 = str(pagenews).split('<div class="btxt">')[1]

    pagenews2 = str(pagenews2).split('</span>')[1]

    firstpagenew = pagenews1+pagenews2

    firstpagenew0 = str(firstpagenew).split('<div class="btit at">')[0]

    firstpagenew1 = str(firstpagenew).split('<div class="btit at">')[1]

    firstpagenews = firstpagenew0+'<div class="btit at">'+firstpagenew1+'</div>'+'</a>'

    firstpagenews = str(firstpagenews).replace('</div></div></div>','</div></div>')

    secendpagenew = re.findall(r'<a.*?</a>',pagenews,re.S)[1]

    secendpagenew0 = str(secendpagenew).split(r'<div class="btxt">')[0]

    secendpagenew1 = str(secendpagenew).split(r'<div class="btxt">')[1]

    secendpagenew1 = str(secendpagenew1).split(r'</span>')[1]

    secendpagenew = secendpagenew0+'<div class="btxt">'+secendpagenew1

    threepagenew = str(pagenews).split(r'<div class="cmsg">')[1]


    # pagenews = str(pagenews).split('<div class="btit at">')[2]

    # pagenews = '<div class="btit at">'+pagenews+'</div>'

    # secendpagenew =



    return firstpagenews,secendpagenew,threepagenew







if __name__ == '__main__':
    getphoto()

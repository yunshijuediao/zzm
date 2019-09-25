import requests
import re
from bs4 import BeautifulSoup
for m in range(0,10):
    u = 'https://movie.douban.com/top250?start='+str(0+m*25)+'&filter='
    print(u)
    res = requests.get(u)
    html = res.text
    bs = BeautifulSoup(html,'html.parser')
    number = bs.find_all('em')
    name = bs.find_all('span',class_= 'title')
    rating = bs.find_all('span',class_= 'rating_num')
    inqure = bs.find_all('span',class_='inq')
    sub = bs.find_all('div',class_ = "hd") 
    finalname=[]
    j = 1
    for i in range(len(name)):
        finalname.append(name[i].text)
        if name[i].text[0] == '\xa0':
            finalname.pop()
            x = name[i].text.replace('\xa0', '')
            x = x.replace('/\xa0', '/')
            
            finalname[-1] += x
    with open('C:\\Users\\22530\\Desktop\\a.doc','a',encoding = 'utf-8') as f:
        for i in range(len(number)):
            f.write(repr([number[i].text,finalname[i],rating[i].text,inqure[i].text,sub[i].find('a').get('href')]))




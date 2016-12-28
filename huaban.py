__author__ = 'Administrator'
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve
from multiprocessing import pool
import json
import re
import time

def getPicName(num):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    try:
        page=requests.get("http://huaban.com/pins/{0}/".format(num),headers=headers)
        soup=BeautifulSoup(page.text,'lxml')
        pic_name=re.findall(r'app\["page"\].*}}};?',str(soup))[0]
        true_pic_name=re.findall(r'"key":"(.*)"?, "type',pic_name)[0].split('",')[0]
        true_pic_url='http://img.hb.aicdn.com/'+true_pic_name
        return true_pic_url

    except Exception:
        with open('invalid_url_list.txt','a+') as fo:
            fo.write('http://huaban.com/pins/'+str(num)+'\n')
            print('http://huaban.com/pins/'+str(num)+' is invalid url')



#for num in range(900000000,900000010):
def download(num):
    try:
        link=getPicName(num)
        pic_name=link.split('/')[-1]
        urlretrieve(link,r'd:\pic1\{}.jpg'.format(pic_name))
        print(pic_name+' is downloaded')
    except Exception:
        pass


# print(time.ctime())
# download_pool=pool()
# pool.map(download,list(range(900000000,900000010)))
# print(time.ctime())

def main():
    for i in range(900000000,900020000):
        download(i)


print(time.ctime())
main()
print(time.ctime())
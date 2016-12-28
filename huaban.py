__author__ = 'pipasugar'
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import time

'''
    花瓣网图片抓取思路
    1，多次浏览发现花瓣网的每个图片都有一个URL链接，http://huaban.com/pins/1234567 类似这种，只有后面的数字是变化的
    2，进入到图片链接，审查元素，可以发现，图片的真实地址  类似  http://img.hb.aicdn.com/4783f52b95ba7a24f20b85ce21bd312c244c55d7490618-6A7Fpe，
       后面的一段无序字符串的不同的。
    3，只要能确定后一段无序字符串，就可以确定一个图片的真实地址。
    4，访问图片的URL链接，可以再返回的源码中找到该无序字符串。
    5，将该无序字符串和http://img.hb.aicdn.com/组合成一个完整的链接，就可以下载图片了。    
 
'''
#定义函数，作用：根据图片URL后面的数字（http://huaban.com/pins/1234567），得到该图片的真实地址。
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



#定义函数，作用：根据图片URL后面的数字，下载图片，保存到本地
def download(num):
    try:
        link=getPicName(num)
        pic_name=link.split('/')[-1]
        urlretrieve(link,r'd:\pic1\{}.jpg'.format(pic_name))
        print(pic_name+' is downloaded')
    except Exception:
        pass
    
    
#定义函数，作用：指定URL后面的数字范围，下载这些URL对应的图片。
def main():
    for i in range(900000000,900020000):
        download(i)


print(time.ctime())
main()
print(time.ctime())

####################################运行结果######################
'''
43ed6f6d7244533a98f584a107510d30b67c2a3538952-guv9Kd is downloaded
c64fc1425debdfd3ca4a37cd96cc1f63bccf90149d29-E1nlPV is downloaded
a2ed28d1893c61903823a69748bd9e49e68f97a161fb5-wz0vg4 is downloaded
b059cdb701172d0bffbc2d0833fcd054e731ab1a1363a-QGQb1h is downloaded
'''

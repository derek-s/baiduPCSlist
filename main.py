# -*- coding:UTF-8 -*-
#---- main.py ----
#百度网盘链接应用抓取页面内大量链接
#2016-12-10

from bs4 import BeautifulSoup
import urllib2
import os
import string
import io

linkfile = open('link.txt',"aw+")
#sucode = urllib2.urlopen("").read()
#soup = BeautifulSoup(sucode,'html.parser')

soup = BeautifulSoup(open('233.html'),'html.parser')
#print soup.prettify()

for link in soup.find_all("a",attrs={"class":"list-micon icon-download2"}):
    linkfile.write(link.get('href'))
    linkfile.write('\n')
    

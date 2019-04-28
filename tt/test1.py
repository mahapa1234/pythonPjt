#encoding: utf-8

# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('https://www.baidu.com')
# print browser.current_url

import requests

# data = {
#     'name':'germey',
#     'age':22
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print r.text
# print r.json()
# print r.content
#


from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
print bsObj.findAll(text="the prince")
print bsObj.body.attrs



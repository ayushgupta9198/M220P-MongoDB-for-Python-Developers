from bs4 import BeautifulSoup
from urllib.request import urlopen
url='http://makeseleniumeasy.com/2018/08/25/how-to-change-default-download-directory-for-chrome-browser-in-selenium-webdriver/'
response=urlopen(url)
print(response)
soup=BeautifulSoup(response,'html.parser')
print(soup.text)
# ===============================method 2================
# from bs4 import BeautifulSoup
# # from urllib.request import urlopen
# import requests
# url='http://makeseleniumeasy.com/2018/08/25/how-to-change-default-download-directory-for-chrome-browser-in-selenium-webdriver/'
# response=requests.get(url)
# print(response)
# soup=BeautifulSoup(response.text,'html.parser')
# print(soup.text)
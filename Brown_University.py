from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import re

url = "https://www.brown.edu/undergraduate_concentrations"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1,"html.parser")

branch=soup.find_all("a",{"class":"component_title_link"})
branch
branch=branch[:-1]
branch[81].text
url1="https://www.brown.edu"+branch[0].get('href')

driver.get(url1)
html1 = driver.page_source
soup = BeautifulSoup(html1,"html.parser")

email=soup.find_all("a",{"class":"link_list_link","itemprop":"url"})
email[2].get('href').split(':')[1]
email=email[2:]
email[0]
name=soup.find_all("span",{"class":"link_list_link_label","itemprop":"name"})
name[2].text



for i in range(0,len(branch)):
    department=branch[i].text
    department=department.replace('-','').replace('/',' ')
    url1="https://www.brown.edu"+branch[i].get('href')
    driver.get(url1)
    time.sleep(2)
    html1 = driver.page_source
    soup = BeautifulSoup(html1,"html.parser")
    email=soup.find_all("a",{"class":"link_list_link","itemprop":"url"})
    name=soup.find_all("span",{"class":"link_list_link_label","itemprop":"name"})
    email=email[2:]
    name=name[2:]
    name1=[]
    email1=[]
    for j in range(0,len(email)):            
        name1.append(name[j].text)
        email1.append(email[j].get('href').split(':')[1])
    if(len(email1)>0):    
        data=pd.DataFrame(list(zip(name1,email1,)),columns=['Name','Email'])
        book = load_workbook(r'G:\study\internshipp\CSIR_CDRI\Brown_University.xlsx')
        writer = pd.ExcelWriter(r'G:\study\internshipp\CSIR_CDRI\Brown_University.xlsx', engine='openpyxl') 
        writer.book = book
        data.to_excel(writer, sheet_name = department)        
        writer.save()
        print(i)
        












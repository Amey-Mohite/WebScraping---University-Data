from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import re

url = "https://www.brown.edu/academics/medical/about/departments/faculty-directory"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1,"html.parser")

z=soup.find('div',attrs={'class':"view-content"}).find_all("div")
z[0].a.text
url1="https://www.brown.edu"+z[0].a.get('href')
driver.get(url1)
html1 = driver.page_source
soup = BeautifulSoup(html1,"html.parser")

tr=soup.find_all("tr")

name=tr[0].td.a.text
designation=str(tr[0].td).split('<br/>')[1]
email=tr[0].td.find_all('a')[1].text


for i in range(0,len(z)):
    department=z[i].a.text
    url1="https://www.brown.edu"+z[i].a.get('href')
    driver.get(url1)
    time.sleep(2)
    html1 = driver.page_source
    soup = BeautifulSoup(html1,"html.parser")
    tr=soup.find_all("tr")
    #name=tr[i].td.a.text
    #designation=str(tr[i].td).split('<br/>')[1]
    #email=tr[i].td.find_all('a')[1].text
    name1=[]
    email1=[]
    designation1=[]
    for j in range(0,len(tr)):            
        name1.append(tr[j].td.a.text)
        email1.append(tr[j].td.find_all('a')[1].text)
        designation1.append(str(tr[j].td).split('<br/>')[1])
    if(len(email1)>0):    
        data=pd.DataFrame(list(zip(name1,email1,designation1)),columns=['Name','Email','Designation'])
        book = load_workbook(r'G:\study\internshipp\CSIR_CDRI\Brown_University.xlsx')
        writer = pd.ExcelWriter(r'G:\study\internshipp\CSIR_CDRI\Brown_University.xlsx', engine='openpyxl') 
        writer.book = book
        data.to_excel(writer, sheet_name = department)        
        writer.save()
        print(i)
    




















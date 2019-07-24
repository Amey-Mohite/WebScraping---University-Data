from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from openpyxl import load_workbook
url = "https://kwc.edu/academics/academic-programs/majors/exercise-science/meet-the-faculty/"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1)

department_sheet='Exercise Science'

name=soup.find('div',attrs={'class':"turf e-content entry-content"}).findAll('p')

str(name[0]).split('<br/>')

name[0].text.split('>')[1]
name[1].text.split('>')[1]
name[2].text.split('>')[1]
name1=[]
pos=[]
email=[] 
phone=[]
office=[]


name1.append(name2[0])
pos.append(name2[1].replace('</strong>','')+name2[2])
email.append(name2[3].split('>')[1].split('<')[0])
phone.append(name2[4].replace(' ',''))
office.append(name2[5].split('<')[0])

for i in range(1,len(name)):
    name2=str(name[7]).split('<p>')[1].split('</noscript>')[1].replace('\xa0',' ').replace('amp;','').split('<br/>')
    name1.append(name2[0])
    pos.append(name2[1].replace('</strong>',''))
    email.append(name2[2].split('>')[1].split('<')[0])
    phone.append(name2[3].replace(' ',''))
    office.append(name2[4].split('<')[0])    

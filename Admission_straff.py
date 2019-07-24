from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

url = "https://www.lindsey.edu/academics/majors-and-programs/Education-Master-Human-Service/Faculty.cfm"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1)

main=soup.find_all('div',attrs={'class':"panel-body text-center"})
name=soup.find_all('h3',attrs={'class':"max-height-60 min-height-60 media-heading text-orange"})
designation=soup.find_all('p',attrs={'class':"max-height-60 min-height-60"})
office_type=soup.find_all('div',attrs={'class':"office-type"})
office_type[0]
email=soup.div.find_all('h5')
email=email[1:]
email=email[:-3]
phone=[]
name1=[]
designation1=[]
office_type1=[]
email1=[]
for i in range(0,len(main)):
    z1=str(main[i]).split('<p></p>')
    phone.append(z1[0][-12:])

office_type[0].span.text    
name[0].text
designation[0].text
str(email[0]).split('>')[1][:-1][16:]
for i in range(0,len(name)):
    office_type1.append(office_type[i].span.text)    
    name1.append(name[i].text)
    designation1.append(designation[i].text)
    email1.append(str(email[i]).split('>')[1][:-1][16:])


import numpy as np
z=pd.DataFrame(list(zip(name1,designation1,email1,phone,office_type1)),columns=['Name','Designation','Email','Phone Numbe','Office Type'])

    
writer = pd.ExcelWriter('G:\study\internshipp\CSIR_CDRI\Georgetown College.xlsx', engine='xlsxwriter')
z.to_excel(writer, sheet_name='Admission_department')
z.to_excel(r'G:\study\internshipp\CSIR_CDRI\Georgetown College.xlsx',sheet_name='Admission_department')

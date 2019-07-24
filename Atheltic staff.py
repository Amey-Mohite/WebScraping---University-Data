from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from openpyxl import load_workbook
url = "http://www.lindseyathletics.com/staff.php"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1)


Administration=soup.find_all('td',attrs={'class':"staffTypeTitle",'id':"group-administration"})
Administration

staffName=soup.find_all('td',attrs={'class':"staffName"})
staffName

staffPosition=soup.find_all('td',attrs={'class':"staffPosition"})
staffPosition

staffEmail=soup.find_all('td',attrs={'class':"staffEmail"})
staffEmail[0]
str(staffEmail[0]).split('>')[1][:-1][16:]
staffPhone=soup.find_all('td',attrs={'class':"staffPhone"})
staffPhone

l=[5,4,1,2,4,4,5,2,1,1,1,1,10,1,1,1,5,4,4,2,2,3,3,1,3,3]
admin=[]
name=[]
pos=[]
email=[]
phone=[]


for i in range(0,len(l)):
     for j in range(0,l[i]):
        admin.append(Administration[i].text)
        name.append(staffName[j].text)
        pos.append(staffPosition[j].text)
        email.append(str(staffEmail[j]).split('>')[1][:-1][16:])
        phone.append(staffPhone[j].text)    
z=pd.DataFrame(list(zip(admin,name,pos,email,phone)),columns=['Department or Sport','Name','Position','Email','Phone Number'])
book = load_workbook(r'G:\study\internshipp\CSIR_CDRI\Georgetown College.xlsx')
writer = pd.ExcelWriter(r'G:\study\internshipp\CSIR_CDRI\Georgetown College.xlsx', engine='openpyxl') 
writer.book = book
z.to_excel(writer, sheet_name ="Athletic")        
writer.save()
    


















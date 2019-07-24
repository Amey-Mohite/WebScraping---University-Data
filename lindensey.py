from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import re
url = "https://www.lindsey.edu/academics/majors-and-programs/Music/Faculty.cfm"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1)

#branch name:
branch=soup.find_all('h1')[0].text  

deignation=soup.find_all('h2')
#deignation[7].text
name=soup.find_all('h3')
#name[0].text

email=soup.find('div',attrs={'class':"indentTop indentLeft"}).find_all('a',attrs={'href': re.compile("mailto:")})
#del email[-1]
z=soup.find('div',attrs={'class':"indentTop indentLeft"}).find_all('p')
z1=str(z).split('</p>')
del z1[3]
del z1[2:7]
del z1[3]
del z1[4:10]
del z1[11]
del z1[5:9]
del z1[11]
z1.insert(1,'')
z1[0].replace('<p>','').replace('<br/>\n','').replace('[','').replace('                       ','')
for i in range(0,len(z1)):
    z1[i]=z1[i].replace('<p>','').replace('<br/>\n','').replace('<br/>','').replace('[','').replace('                       ','').replace(',','').replace('                   	','').replace('                    ','').replace('				','').replace('	','').strip()

z=soup.find_all('div',attrs={'class':"tab-pane fade in active"})
re.sub(' +', ' ',str(z[0].text)).replace('\n','').replace('\t','').strip()
z1=[]
for i in range(0,len(z)):
    z1.append(re.sub(' +', ' ',str(z[i].text)).replace('\n','').replace('\t','').strip())
z1.append("")
z1.append("")
z1.insert(0,'')
z1.insert(3,'')
#need to again split and delete some entries from z1

p=[]

s=soup.find('div',attrs={'class':"indentTop indentLeft"}).text
for index,value in enumerate(s):
    if s[index:index+(len("Phone"))] == "Phone":
        p.append(index)

#s[p[0]+6:p[0]+19].strip()

p1=[]
q=soup.find('div',attrs={'class':"indentTop indentLeft"})
q=str(q)
for index,value in enumerate(q):
    if q[index:index+(len("</h3>"))] == "</h3>":
        p1.append(index)
        
#q[p1[0]+6]

#m = q[p1[0]+6:].index('<br/>')

#l = q[p1[0]+6:m+p1[0]+6]
#l=l.strip().replace('amp;','')
#l

#for i in range(0,len(p1)):
 #   m = q[p1[i]+6:].index('<br/>')
  #  l = q[p1[0]+6:m+p1[0]+6]
   # l=l.strip().replace('amp;','')
        
phone=[]
name1=[]
designation=[]
email1=[]
education=[]
office=[]
#z[0]
for i in range(0,len(p)):
    name1.append(name[i].text)
    email1.append(email[i].text)
    designation.append(deignation[i].text)
    education.append(z1[i])
    phone.append(s[p[i]+6:p[i]+19].strip())
    m = q[p1[i]+6:].index('<br/>')
    l = q[p1[i]+6:m+p1[i]+6]
    l=l.strip().replace('amp;','')
    office.append(l)
data=pd.DataFrame(list(zip(name1,office,designation,email1,phone,education)),columns=['Name','Office','Designation','Email','Phone','Education'])
data

data=pd.DataFrame(list(zip(name1,office,designation,email1,phone)),columns=['Name','Office','Designation','Email','Phone'])
data

for i in range(0,len(p)):
    name1.append(name[i].text)
    email1.append(email[i].text)
    designation.append(deignation[i].text)
   # education.append(z1[i])
    phone.append(s[p[i]+6:p[i]+19].strip())
    #m = q[p1[i]+6:].index('<br/>')
    #l = q[p1[i]+6:m+p1[i]+6]
    #l=l.strip().replace('amp;','')
    #office.append(l)

data=pd.DataFrame(list(zip(name1,designation,email1,phone)),columns=['Name','Designation','Email','Phone'])
data


book = load_workbook(r'G:\study\internshipp\CSIR_CDRI\lindensey.xlsx')
writer = pd.ExcelWriter(r'G:\study\internshipp\CSIR_CDRI\lindensey.xlsx', engine='openpyxl') 
writer.book = book
data.to_excel(writer, sheet_name =branch)        
writer.save()  
    
    
    
    
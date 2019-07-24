from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "http://www.indiavotes.com/pc/info?eid=16&state=0"
driver = webdriver.PhantomJS(r"G:\study\software\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)

# This will get the initial html - before javascript
html1 = driver.page_source
soup = BeautifulSoup(html1)
a_tag=soup.find_all('a')
c=soup.find_all('td',attrs={'class': 'tal sorting_1'})
c=c[:-13]
c
#z=str(c[1].find_all('a')[0])
#z
#z=z[9:55]

#z.replace("'",'')



#for i in c:
 #   z=''
 #   z=str(i.find_all('a')[0])
  #  z=z[9:55]
   # z=z.replace('"','')
   # print(z)



#z=str(c[1].find_all('a')[0])
#z
#z=z[9:55]
#z
#driver.get(z)
#html1 = driver.page_source
#soup = BeautifulSoup(html1)
#tal=soup.find_all('td',attrs={'class': 'tal '})
#tar=soup.find_all('td',attrs={'class': 'tar '})
#number=soup.find_all('td',attrs={'class': 'numberTable'})    
#n=str(number[1])
#n
#n=n[24:26]
#n
#if n[1]=='<':
#    n=n.replace('<','')
#n
#n=int(n)
#n
#if n<=3:

    
name=soup.find_all('td',attrs={'class': 'tal '})[0]
#name=str(name)
#name
#name=name.split('>')[1].split('<')[0]
#name

#party=soup.find_all('td',attrs={'class': 'tal '})[1]
#party=str(party)
#party
#party=party.split('<')[2].split('>')[1]
#party

#no_votes=soup.find_all('td',attrs={'class': 'tar '})[0]
#no_votes=str(no_votes)
##no_votes
#no_votes=no_votes.split('>')[1].split('<')[0]
#no_votes

#per_votes=soup.find_all('td',attrs={'class': 'tar '})[1]
#per_votes=str(per_votes)
#per_votes
#per_votes=per_votes.split('>')[1].split('<')[0]
#per_votes


name=[]
party=[]
no_votes=[]
per_votes=[]    


c1=c[516:]
c1[0]
for i in c1:
    z=''
    z=str(i.find_all('a')[0])
    z=z[9:55]
    z=z.replace('"','')
    print(z)
    driver.get(z)
    time.sleep(2)
    html1 = driver.page_source
    soup = BeautifulSoup(html1)
    #number=soup.find_all('td',attrs={'class': 'numberTable'})    
    #n=str(number[0])
    #n
    #n=n[24:26]
    #n
    #if n[1]=='<':
     #   n=n.replace('<','')
    #n
    #n=int(n)
    #n
    n=0
    while(n<3):
        nam=''
        nam=soup.find_all('td',attrs={'class': 'tal '})[n*2]
        nam=str(nam)
        nam
        nam=nam.split('>')[1].split('<')[0]
        nam
        name.append(nam)
        
        part=''
        part=soup.find_all('td',attrs={'class': 'tal '})[n*2+1]
        part=str(part)
        part
        part=part.split('<')[2].split('>')[1]
        part
        party.append(part)

        no_vote=''
        no_vote=soup.find_all('td',attrs={'class': 'tar '})[n*2]
        no_vote=str(no_vote)
        no_vote
        no_vote=no_vote.split('>')[1].split('<')[0]
        no_vote
        no_votes.append(no_vote)

        per_vote=''
        per_vote=soup.find_all('td',attrs={'class': 'tar '})[n*2+1]
        per_vote=str(per_vote)
        per_vote
        per_vote=per_vote.split('>')[1].split('<')[0]
        per_vote
        per_votes.append(per_vote)
        n=n+1  


import pandas as pd
import numpy as np
z=pd.DataFrame(list(zip(name,no_votes,per_votes,party)),columns=['Name','No.of votes','Percentage of votes','Party'])
z.to_csv("G:\study\web_scarping\csv_2014.csv")
z.to_excel("G:\study\web_scarping\excel_2014.xlsx")

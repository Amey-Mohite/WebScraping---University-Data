import numpy as np 
import pandas as pd

data_2009=pd.read_csv(r"G:\study\web_scarping\csv_2009.csv")
data_2014=pd.read_csv(r"G:\study\web_scarping\csv_2014.csv")
data=pd.read_csv(r"G:\study\web_scarping\IndiaVotes_PC__All_States_2009.csv")
data1=pd.read_csv(r"G:\study\web_scarping\IndiaVotes_PC__All_States_2014.csv")
data_final_place=[]
data_final_rank=[]
data_final_name=[]
data_final_vote=[]
data_final_percentage=[]
data_final_party=[]

place=data1['PC Name']
j=0
for i in range(516,543):
    data_final_place.append(place[i])
    data_final_rank.append(1)
    data_final_name.append(data_2014['Name'][j])
    data_final_vote.append(data_2014['No.of votes'][j])
    data_final_percentage.append(data_2014['Percentage of votes'][j])
    data_final_party.append(data_2014['Party'][j])
    
    j=j+1   
    data_final_place.append('')
    data_final_rank.append(2)
    data_final_name.append(data_2014['Name'][j])
    data_final_vote.append(data_2014['No.of votes'][j])
    data_final_percentage.append(data_2014['Percentage of votes'][j])
    data_final_party.append(data_2014['Party'][j])
    
    j=j+1
    data_final_place.append('')
    data_final_rank.append(3)
    data_final_name.append(data_2014['Name'][j])
    data_final_vote.append(data_2014['No.of votes'][j])
    data_final_percentage.append(data_2014['Percentage of votes'][j])
    data_final_party.append(data_2014['Party'][j])
   
    j=j+1
    data_final_place.append('')
    data_final_rank.append('')
    data_final_name.append('')
    data_final_vote.append('')
    data_final_percentage.append('')
    data_final_party.append('') 
    
z=pd.DataFrame(list(zip(data_final_place,data_final_rank,data_final_name,data_final_vote,data_final_percentage,data_final_party)),columns=['Place','Rank','Name','No.of votes','Percentage of votes','Party'])
z.to_csv(r"G:\study\web_scarping\final_2014.csv")
z.to_excel(r"G:\study\web_scarping\final_2014.xlsx")
    
import pandas as pd 
xls = pd.ExcelFile(r'G:\study\internshipp\CSIR_CDRI\Georgetown College.xlsx')
z=xls.sheet_names


df1 = pd.read_excel(xls,z[0])

name=[]
designation=[]
email=[]
phone=[]
office_type=[]
name.insert(0,"")
designation.insert(0,"")
email.insert(0,"")
phone.insert(0,"")
office_type.insert(0,"")   

name.insert(1,"")
designation.insert(1,"Admission Department")
email.insert(1,"")
phone.insert(1,"")
office_type.insert(1,"")   
     
name.insert(2,"")
designation.insert(2,"")
email.insert(2,"")
phone.insert(2,"")
office_type.insert(2,"")   


for i in range(0,len(df1)):
    name.append(df1['Name'][i])
    designation.append(df1['Designation'][i])
    email.append(df1['Email'][i])
    phone.append(df1['Phone Numbe'][i])
    office_type.append(df1['Office Type'][i])

z=pd.DataFrame(list(zip(name,designation,email,phone,office_type)),columns=['Name','Designation','Email','Phone Numbe','Office Type'])
z.to_excel(r'G:\study\internshipp\CSIR_CDRI\Georgetown College1.xlsx',sheet_name='Admission_department')

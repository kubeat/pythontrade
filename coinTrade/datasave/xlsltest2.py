import pandas as pd
import xlsxwriter
import sys

#df = pd.read_excel('new_excel.xlsx')
#print(df.head())
df = pd.read_excel('new_excel.xlsx')
print(df.head())

workbook = xlsxwriter.Workbook('new_people.xlsx')     #新建excel表
worksheet = workbook.add_worksheet('sheet1')       #新建sheet（sheet的名称为"sheet1"）


for index,item in df.iterrows():
    date=item['Number']
    count=item['testA']
    date=date.replace(' 00:00:00','')
    worksheet.write(0,index,date)
    worksheet.write(1,index,count)

workbook.close()

print(dir(sys))
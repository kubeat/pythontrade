import xlsxwriter  # 导入模块
import pandas as pd

workbook = xlsxwriter.Workbook('new_excel.xlsx')  # 新建excel表
worksheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
headings = ['Number', 'testA', 'testB']
# 设置表头
data = [
    ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]  # 自己造的数据

worksheet.write_row('A1', headings)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])  # 将数据插入到表格中

workbook.close()
df = pd.read_excel('new_excel.xlsx')
df = df.set_index('testA')
print(df.head())

df_m = df.resample('Number').sum()

print(df_m.head())


if __name__ == '__main__':
    pass
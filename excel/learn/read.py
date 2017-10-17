# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd as xlrd

data = xlrd.open_workbook('read_data.xlsx') # 打开xls文件
count = data.sheets().__len__()
print('当前表中有%d个sheet'%(count))
for current_sheet_page in range(count):
    table = data.sheets()[current_sheet_page] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    print("当前表名%s，共有%d行数据"%(data.sheet_names()[current_sheet_page], nrows))
    for i in range(nrows): # 循环逐行打印
        if i == 0: # 跳过第一行
            continue
        print(table.row_values(i)[:13]) # 取前十三列

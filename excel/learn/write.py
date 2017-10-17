import xlwt as xlwt

wbk = xlwt.Workbook()

sheet = wbk.add_sheet('Table 1')

# sheet.write_merge(0,0,0,1,'long merge')
for i in range(10):
    for j in range(4):
        sheet.write(i, j, 1)  # 第0行第一列写入内容

wbk.save('write_data.xls')
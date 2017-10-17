import xlrd
from xlutils.copy import copy

merge_str=['hebing','h2','h3','fd','adf']


workbook = xlrd.open_workbook('testIn.xls')

workbooknew = copy(workbook)

ws = workbooknew.get_sheet(0)

count=len(merge_str)
print('count=', count)
for i in range(count):
    index=2*i
    ws.write_merge(0,0,index,index+1,merge_str[i])
    print('完成第%d次合并:content=%s'%(i, merge_str[i]))

workbooknew.save('testIn.xls')
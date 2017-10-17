import xlrd
from xlutils.copy import copy

workbook = xlrd.open_workbook('read_data.xlsx')

workbooknew = copy(workbook)

ws = workbooknew.get_sheet(0)

ws.write(3, 0, 'changed!')

workbooknew.save('read_data_copy.xls')
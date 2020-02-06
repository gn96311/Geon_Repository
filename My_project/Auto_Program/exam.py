import openpyxl
import sys

wb = openpyxl.load_workbook('아마존 리스팅.xlsx')

sheet1 = wb['Sheet1']

for rows in range(2):
    cost_url = sheet1.cell(row=3+rows, column=2).value
    return_price = cost_check(str(cost_url))
    print(return_price)
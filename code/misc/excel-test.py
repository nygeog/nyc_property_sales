import pandas as pd

inFile = '/Users/danielmsheehan/GIS/projects/property_sales/data/input/annual_sales/2012_manhattan_2016-05-12-04-37-39-365275.xls'

#df = pd.io.excel.read_excel(inFile, 'Manhattan', skiprows=4)
df = pd.io.excel.read_excel(inFile, 'Manhattan', skiprows=4, converters={'APARTMENT NUMBER': str})

print df.head(10)

#Apartment Number


# import xlrd
# import csv
# from os import sys

# def csv_from_excel(excel_file):
#     workbook = xlrd.open_workbook(excel_file)
#     all_worksheets = workbook.sheet_names()
#     for worksheet_name in all_worksheets:
#         worksheet = workbook.sheet_by_name(worksheet_name)
#         your_csv_file = open(''.join([worksheet_name,'.csv']), 'wb')
#         print your_csv_file
#         wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

#         for rownum in xrange(worksheet.nrows):
#             wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
#         your_csv_file.close()

# # if __name__ == "__main__":
# #     csv_from_excel(sys.argv[1])
# csv_from_excel(inFile)
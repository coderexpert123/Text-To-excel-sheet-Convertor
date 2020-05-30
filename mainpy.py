import xlsxwriter
workbook=xlsxwriter.Workbook("hello.xlsx")
workshhet=workbook.add_worksheet()
workshhet.write('A1',"Hello")
workbook.close()
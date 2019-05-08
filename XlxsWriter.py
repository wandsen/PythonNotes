import pandas

dataFrame = pandas.DataFrame({'Data': [10, 20, 30]})
writer = pandas.ExcelWriter('write_to_excel.xlsx', engine = 'xlsxwriter')
dataFrame.to_excel(writer, sheet_name = "Sheet1")
writer.save()

# dataFrame2 = pandas.DataFrame({'NotData': ["hello"]})
# writer2 = pandas.ExcelWriter('write_to_excel.xlsx', engine = 'xlsxwriter')
# dataFrame2.to_excel(writer2, sheet_name = "Sheet2")
# writer2.save()

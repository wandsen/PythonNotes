import Question_1_Dictionary as Q1
import pandas

birthdayData = Q1.getBirthdays()
print(birthdayData)

birthdayDataList = []

for key, value in birthdayData.items():
    birthdayDataList.append([key, value])

print(birthdayDataList)

dataFrame = pandas.DataFrame(birthdayDataList, columns = ['Name', 'Birthday'])
writer = pandas.ExcelWriter('output.xlsx', engine = 'xlsxwriter')

print(dataFrame)
dataFrame.to_excel(writer, sheet_name = "Birthday", index=False)
writer.save()
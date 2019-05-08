import pandas

#Access to csv files
excel_file = "data.csv"
excel_data = pandas.read_csv(excel_file)
print(excel_data)

#Access rows using method (integer location)
print(excel_data.iloc[0:2])

#Access by column (case sensitve0)
excel_data_by_column = pandas.DataFrame(excel_data, columns = ['NAME', 'TITLE'])
print(excel_data_by_column)

#Using excel functions on data
sum1 = excel_data['WAGES'].sum()
print("The sum of wages is: " , sum1)

min1 = excel_data['WAGES'].min()
print("The min of wages is: " , min1)

max1 = excel_data['WAGES'].max()
print("The max of wages is: " , max1)
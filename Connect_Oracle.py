import cx_Oracle
import pandas

'''
1. import database module
first check in python folder using pip list, if doesnt exist pip install cx_oracle

2. create a connection using module
3. conect to the record set (connect to the cursor)
4. execute sql statement
5. fetch the output
6. close the cursor and then close the database
'''

username = "Trainee1"
password = "!QAZSE4"
database = "localhost"
osid = "xe"

try:
    connection = cx_Oracle.connect(username + '/' + password + '@' + database + '/' + osid)
    
    #Pointing to record set
    cursor = connection.cursor()

    #Execute DML
    cursor.execute('SELECT * FROM EMPLOYEE')

    #This makes use of substitution where :NAME is substituted with name = input_value
    input_value = input("ENter the name for employee to retrieve\n")
    cursor.execute('SELECT * FROM EMPLOYEE WHERE NAME=:NAME', name = input_value)

    #Retrieve
    row = cursor.fetchone()
    print(row) 

    #Retrieve all records
    allrows = cursor.fetchall()
    print (allrows)

    #Retrievve all records to print in rows 
    for i in allrows:
        print(i)
    
    #Introduce format to print records
    for column1, column2, column3, column4, column5, in allrows:
        print(column1, "\t", column2, "\t", column3, "\t", column4, "\t", column5)

    #Opening a csv file and exporting data into csv, the results are in a dataframe format
    results = pandas.read_sql_query('SELECT * FROM Employee', connection)
    print(results)
    results.to_csv("data.csv", index = False)
    results.to_json("data.json") 

except cx_Oracle.Error as e:
    print('The error is ',  e)

cursor.close()
connection.close()
    
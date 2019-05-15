from myzodb import MyZODB, transaction

db = MyZODB('./Data.fs')
dbroot = db.dbroot

dbroot['a_number'] = 3
dbroot['a_string'] = 'Gift'
dbroot['a_list'] = [1, 2, 3, 4, 5, 12]
dbroot['a_dictionary'] = {1918: 'Red Socks', 1919: "Blue Socks"}
dbroot['Deeply nested'] = {1918 : [('Redsox', 4) , ('cubs', 2)], 1919:[('Reds', 5), ('White sox', 3)]}

transaction.commit()
db.close()
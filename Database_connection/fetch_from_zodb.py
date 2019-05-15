from myzodb import MyZODB
db = MyZODB('./Data.fs')
dbroot = db.dbroot

for key in dbroot.keys():
    print(key + ":" , dbroot[key])
db.close()
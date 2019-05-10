import matplotlib.pyplot as plt
import Question_1_Dictionary as Q1
import pygal as pg

birthdayData = Q1.getBirthdays()
print(birthdayData)

monthData = {}

#Format the data the extract the count of each month
def printBarChart():
    for person in birthdayData:
        dataMonth = birthdayData.get(person).split('/')[1]
        if(monthData.get(dataMonth) == None):
            print('Month does not exist, add month')
            monthData[dataMonth] = 1
        else:
            monthData[dataMonth] +=1

    print(monthData)

    month = []
    count = []
    for key, value in monthData.items():
        print(key)
        month.append(key)
        count.append(value)

    plt.bar(month, count)
    plt.show()





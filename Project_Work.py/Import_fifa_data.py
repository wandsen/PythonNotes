import pandas
import seaborn as sns
from matplotlib import pyplot as plt


#Access to csv files
excel_file = "CompleteDataset.csv"
excel_data = pandas.read_csv(excel_file, index_col = 0)
print(excel_data)

fifaDf = pandas.DataFrame(excel_data, columns = ['Name', 'Age','Nationality', 'Potential'])
print(fifaDf)

def returnStat(column, stat):

    if stat == "min":
        #Findng the minimum age of a player
        print("The minimum age of a fifa player is ", fifaDf[column].min())

    elif stat == "max":
        #Findng the maxium age of a player
        print("The maximum age of a fifa player is ", fifaDf[column].max())

    elif stat == "mean":
        #Findng the average age of a player
        print("The average age of a fifa player is ", fifaDf[column].mean())
    else:
        print("No such stat")

#Counting the number of players in each country
def numPlayerInCountry():
    countryDf = fifaDf.groupby('Nationality')["Name"]
    print(countryDf.count())

#Group by age and find average potential
def avgPotentialByAge():
    ageDf = fifaDf.groupby("Age")
    print(ageDf["Potential"].mean())

# Plotting age vs potential
def barplotAgeVsPotential():
    sns.barplot(x = "Age", y = "Potential" , data = fifaDf)
    plt.show()

def countplotPotential():
    sns.countplot(x = "Potential", data = fifaDf)
    plt.show()

def distPlotPotential():
    sns.distplot(fifaDf["Potential"])
    plt.show()

# def numPlayerInCountry()
# def avgPotentialByAge()
# def barplotAgeVsPotential()
# def countplotPotential()
# def distPlotPotential()
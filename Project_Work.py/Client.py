import Question_1_Dictionary as Q1
import Question_2_Export_Excel as Q2
import Question_3_Histogram as Q3
import Import_fifa_data as Q4


userInput = input("Which Question would you like to choose?\n1) Question 1- Ask birthday\n2) Question 2- export excel\n3) Question 3- bar chart\n4) Choose Fifa project\n")

if (userInput == "1"):
    Q1.askBirthday()
elif (userInput == "2"):
    Q2.exportBirthdayData()
elif (userInput == "3"):
    Q3.printBarChart()
elif(userInput == "4"):
    userInput2 = input("Which part of question 4?\n1) Return min age\n2) Return max age\n3) Return mean age\n4) Number of players in each country\n5) Group by age and potential\n6) Barplot age vs potential\n7) Countplot potential\n8) DistPlot Potential")
    if(userInput2 == "1"):
        Q4.returnStat("Age", "min")
    elif(userInput2 == "2"):
        Q4.returnStat("Age", "max")
    elif(userInput2 == "3"):
        Q4.returnStat("Age", "mean")
    elif(userInput2 == "4"):
        Q4.numPlayerInCountry()
    elif(userInput2 == "5"):
        Q4.avgPotentialByAge()
    elif(userInput2 == "6"):
        Q4.barplotAgeVsPotential()
    elif(userInput2 == "7"):
        Q4.countplotPotential()
    elif(userInput2 == "8"):
        Q4.distPlotPotential()
    else:
        print("No such option")
else:
    print("No such option")

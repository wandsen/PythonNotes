import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'Year': [2012, 2013, 2014, 2015, 2016],
        'Reports':[4 , 24, 31, 2, 3],
        'Coverage': [25, 94, 57, 62, 70]}

df = pd.DataFrame(data, index = ['Chochice', 'Pima', 'SantaCruz', 'Maricopa', 'Yuma'])
print(df)

#Dropping the string variable so applymap() can run, in this case dropping the name column
df = df.drop('name', axis = 1)
print(df)

#Return the square root of every cell in the dataframe
print(df.applymap(np.sqrt))

#Plotting the graph using plt.plot(x, y)
plt.plot(data['name'], data['Reports'])
plt.xlabel('name')
plt.ylabel("Reports")
plt.show()


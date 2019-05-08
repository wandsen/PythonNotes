import pandas

#Dict to Dataframe
olympic_dict = {'London':{2012:205}, 'Beijing': {2008:204}}
data_frame_dic = pandas.DataFrame(olympic_dict)
print(data_frame_dic)

print('*' * 45)

#List to Dataframe
olympic_list = {'HostCity':['London', 'Beijing', 'Athens'],
                'Year':[2012, 2008, 2004],
                'No. of countries': [205, 204, 201]}
data_frame_list = pandas.DataFrame(olympic_list)
print(data_frame_list)
print('*' * 45)

#List to dictionary to dataframe
import numpy
n_array = numpy.array([2012, 2008, 2004, 2006])
dict_narray = {'Year': n_array}
dfnarray = pandas.DataFrame(dict_narray)
print(dfnarray)

print('*' * 45)

#Dataframe from a Dataframe (possible to make dataframes of dataframes)
print(pandas.DataFrame(data_frame_list))

#Stat- extracting value out of dataframe
data = {'Test1': [95, 92, 56, 63, 32],
        'Test2': [75, 53, 77, 53, 92]}
df = pandas.DataFrame(data, index = ['Jack', 'Lewis', 'Patrick', 'Kristian', 'Owen'])
print(df)
print(df.max())
print(df.min())
print(df.std())
print(df.std()[0])

#Data operation - mapping
def movie_grade(rating):
    if rating == 5:
        return 'A'
    elif rating == 4:
        return 'B'
    elif rating == 3:
        return 'C'
    elif rating == 2:
        return 'D'
    else:
        return 'E'

d1 = {'movie':[5,4,3,2,1], 'movie':[4,5,2,3,4]}
df_movieRating = pandas.DataFrame(d1, index = ['Tom', 'Alpha', 'Bravo', 'Charlie', 'Delta'])
print(df_movieRating)
print(df_movieRating.applymap(movie_grade))

print('*' * 45)
#Group data by firstname
df1 = pandas.DataFrame({'first': ['George', 'Bill','Ronald', 'George'],
                        'last': ['Bush', 'Clinton', 'Regan', 'Washington']})
print(df1)

print('*' * 45)
group = df1.groupby('first')
print(group.count())

print('*' * 45)
#Get group with name
group_data = group.get_group('George')
print(group_data)

print('*' * 45)
print(df1.sort_values('first'))



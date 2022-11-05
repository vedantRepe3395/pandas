import pandas as pd
"""
# read data
data = pd.read_excel(r'Attribute DataSet.xlsx')
data = pd.read_excel(r'Attribute DataSet.xlsx', sheet_name='one')
# sheet_name is used for select sheet from excel file.
"""

"""
in pandas the first record of data take as a heading to a  clm
so if we want to change that header we use header  and name clm 
a number 1,2,3,4...
data = pd.read_excel(r'Attribute DataSet.xlsx', header=None)
print(data)
"""

"""
if you want to name a clm then name tag is used with list as a reference for clm name 

data = pd.read_excel(r'Attribute DataSet.xlsx', sheet_name='one', names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                                                         'j', 'k', 'l', 'm', 'n'])
print(data.head(2))  # returns n number of records from top.
print('a')
print(data.tail(2))  # returns n number of records from bottom.
"""
"""data = pd.read_csv(r'haberman.csv', header=None,
                   names=['Age', 'year of operation', 'Number of positive', 'Survival status'])
print(data)

"""

"""
data = pd.read_csv(r'haberman1.csv', sep='@', header=None,                                        
                   names=['Age', 'year of operation', 'Number of positive', 'Survival status'])
# if csv file with any other notation like @ instead of ,
# we can use sep parameter to change that. 

print(data.head(1))
"""
"""
# read csv file from github or any other platform

data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Smarket.csv')
print(data.tail(2))
"""
"""
data = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
print(data[0])
print(type(data))  # return list
"""
"""
data = pd.read_json('https://api.github.com/repos/pandas-dev/pandas/issues')
print(data
"""
"""
# convert data from one form to another like json to csv
data.to_csv('vedant.csv')

data.to_excel('vedant.xlsx')
"""


"""
data = pd.read_csv(r'haberman.csv', header=None)
data.to_csv('vedant.csv',sep='%',inde=False) 
# index used for number fo rows  

"""


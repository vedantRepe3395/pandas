import pandas as pd

df = pd.read_csv('AgentPerformance.csv')

"""# find clm name
print(df.columns)
"""

"""
# select 1 column
print(df['Date'])
"""

"""
# select multiple columns
print(df[['Agent', 'Date']]) 
"""

"""
# provide info of mean, standard deviation,min, max, 25%, 50%, 75% 
# of clm which containing numerical values like int flot 
print(df.describe())
"""

"""
print(df[df.dtypes[df.dtypes == 'object'].index])
# provide clm with data which containing data of data type = object.
"""
"""
print(df[df.dtypes[df.dtypes == 'object'].index].describe())

"""


"""
print(df["Agent Name"].isnull())
# returns true if value == null 
"""
"""
print(df[df['Total Feedback'] == max(df['Total Feedback'])][['Agent Name','Total Feedback']])
"""

print(df[df['Total Feedback'] == 7][['Agent Name', 'Total Feedback']])


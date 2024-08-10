import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# to read external data the titanic dataset is saved as a csv file
data = pd.read_csv('Titanic-Dataset.csv')

# to view the first five rows in the dataset
# if you want to view a certain amout input it in the parenthesis
data.head()

# display all the columns in the dataset
data.columns

# to view the last files in the data
data.tail()

# to get the number of rows and colums in the dataset
data.shape
# (rows,columns)

# to check for null values in the dataset
data.isnull()

# to get its aggregate
data.isnull().sum()

# to get info about the data
data.info()

# to get statistics
data.describe()
# Note: it would only perform stats for data that is number like,it'll skip stuffs like name,gender e.t.c

# for example a dataset has a sex columns with male and females,in order to get the total number of males and females seperately
data.sex.value_counts()

# to check for unique values in a column
data.sex.unique()

# to fill in the null values
data = data['Gender'].fillna(data['Gender'].mode()[0])
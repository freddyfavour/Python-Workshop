import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.linear_model import LogisticRegression

# to import the data
data = pd.read_csv('whateverfile.csv')

# to see the first five rows
data.head()

# to check the last rows
data.tail()

# to get info about the data
data.info()

# to confirm for null values
data.isnull().sum()

# to get a statistical summary of the data
data.describe()

# to get a summary of non-numeric data
data.describe(include='object')

# to get unique values within the dataset
data.nunique() # to get the sum of possibilities
data.unique() # to get unique values

# to get the counts of values
data.Gender.value_counts()

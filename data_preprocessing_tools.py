# Data Preprocessing Tools

# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
#ind v
x = dataset.iloc[:, :-1].values
#dep v
y = dataset.iloc[:, -1].values

print(x)
print(y)
# Taking care of missing data


# Encoding categorical data
# Encoding the Independent Variable

# Encoding the Dependent Variable

# Splitting the dataset into the Training set and Test set



# Feature Scaling

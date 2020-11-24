import sys
import pandas as pd
import matplotlib
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix

# Load the data

airline = pd.read_csv("airline.csv")

# Print the names of the columns in games
# print(airline.columns)
# print(airline.shape)

# Make a histogram of all the prices in the cost column
# plt.hist(airline["Cost"])
# plt.show()

# Remove any rows with missing values

airline = airline.dropna(axis=0)
# print(airline.shape)


# def numberofstops(x):
#     if(x == "non-stop"):
#         return 0
#     else:
#         return x.split(' ')[0]

# Create a function that isolates the number of stops from the Layover columns

def RepresentsInt(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return 0


stopnumber = []

arr = airline.Layover.to_numpy()
for i in range(len(arr)):
    stopnumber.append(RepresentsInt(arr[i].split(' ')[0]))

# print(stopnumber)

# Add the contents of stopnumber into the Data Frame
airline.insert(4, column="stopnumber", value=stopnumber)

# for i in range(10):
#     print('Layover is equal to = {},'.format(airline.Layover[i]),
#         'Stop Number is equal to = {}'.format(airline.stopnumber[i]))

# Isolate the time span of the flight and simplify it to just minutes of flight time

h = airline['Time span'].str.extract('(\d+)h', expand=False).astype(float) * 60
m = airline['Time span'].str.extract('(\d+)m', expand=False).astype(float)

airline['flighttimeminutes'] = h.add(m, fill_value=0).astype(int).astype(str)

# print(airline.shape)

airline['monthofflight'] = pd.DatetimeIndex(airline['Flight Date'], dayfirst=True).month
# print(airline.monthofflight)

# plt.hist(airline["monthofflight"])
# plt.show()

corrmat = airline.corr()
fig = plt.figure(figsize=(12, 6))

sns.heatmap(corrmat, vmax=0.8, square=True)
plt.show()

# scatter plot matrix
# scatter_matrix(airline)
# plt.show()

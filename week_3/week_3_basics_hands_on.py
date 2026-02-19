# Week 3 : Numpy and Pandas for Data Manipulation

import numpy as np
import pandas as pd

# initializing an array
a = np.array([2,3,1,4,4,2,5,6])
print(a)

# access elements
print(a[1], " ", a[2])

# elements are modifiable

# operations
b = np.array([2,4,1])
c = np.array([3,5,6])

print(b+c)

# broadcasting
d = np.array([[1,3,4], [6,2,1]])
print(d + b)

# Series
series_1 = pd.Series([3,1,3,5,5,2,2,5,7,2])
print(series_1)
print(type(series_1))

data = {
    "branch" : ['CSE', 'CSE', 'ECE', 'MT', 'ECE', 'MT', 'MT', 'CSE'],
    "CG" : [8.5, 7.7, 8.1, 7.9, 6.9, 7.1, 8.6, 8.9] 
}

df = pd.DataFrame(data)

print(df.groupby("branch")["CG"].mean())

print(df.groupby("branch")["CG"].agg(["mean", "max", "min"]))

print(df.groupby(["branch", "CG"]).count())


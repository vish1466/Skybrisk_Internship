import numpy as np
import pandas as pd

nums = int(input("Number of samples to collect : "))
days = [x for x in range(1, nums + 1)]


temperatures = []
cities = []
for i in range(nums):
    temp = float(input(f"Provide Temperature Value {i + 1} : "))
    cit  = str(input(f"Provide city {i+1} : "))
    temperatures.append(temp)
    cities.append(cit)


df = pd.DataFrame({
    "days" : days,
    "temperature" : temperatures,
    "city" : cities
})

print("Dataset Collected :  \n", df)

# first clean up missing values (if any)
df = df.dropna()

print("Cleaned dataset :  \n", df)

# next calculate average temperature of each city 

avg_temp = df.groupby("city")["temperature"].mean()

print("Average Temperature by city : \n", avg_temp)



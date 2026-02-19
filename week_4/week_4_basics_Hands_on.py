# Week 4 : Data Visualization with Matplotlib and Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "day": [1, 2, 3, 4, 5, 6, 7],
    "temperature": [32, 34, 33, 31, 35, 36, 34],
    "humidity": [60, 58, 62, 65, 55, 50, 57]
}

df = pd.DataFrame(data)

# simple line plot
plt.figure()
plt.plot(df["day"], df["temperature"], marker="o")
plt.title("Temperature Over Days")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.savefig("temperature_line_plot.png")
plt.show()

# histogram
plt.figure()
plt.hist(df["temperature"], bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("temperature_histogram.png")
plt.show()

data_sec = {
    "day": [1,2,3,4,5,6,7, 1,2,3,4,5,6,7],
    "city": ["Delhi"]*7 + ["Mumbai"]*7,
    "temperature": [32,34,33,31,35,36,34, 28,29,30,31,32,33,34],
    "humidity": [60,58,62,65,55,50,57, 75,78,80,82,79,77,76],
    "wind_speed": [10,12,8,9,11,14,13, 15,18,17,16,19,20,18]
}

# multiple line plots in the same figure
df_sec = pd.DataFrame(data_sec)
plt.figure()
sns.lineplot(data=df_sec, x="day", y="temperature", hue="city", marker="o")
plt.title("Temperature Comparison Between Cities")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

# heatmap
plt.figure()
corr = df_sec[["temperature", "humidity", "wind_speed"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Weather Feature Correlation")
plt.show()


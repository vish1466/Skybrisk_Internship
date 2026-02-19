# Week 4 : Client Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n = 100

data = {
    "StudyHours": np.random.normal(5, 1.5, n),
    "SleepHours": np.random.normal(7, 1, n),
    "Attendance": np.random.uniform(60, 100, n)
}

df = pd.DataFrame(data)

df["ExamScore"] = (
    df["StudyHours"] * 8
    + df["SleepHours"] * 2
    + df["Attendance"] * 0.3
    + np.random.normal(0, 5, n)
)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Student Performance Dashboard", fontsize=16)

# Scatter plot: Study Hours vs Exam Score
axes[0, 0].scatter(df["StudyHours"], df["ExamScore"])
axes[0, 0].set_title("Study Hours vs Exam Score")
axes[0, 0].set_xlabel("Study Hours")
axes[0, 0].set_ylabel("Exam Score")

# Scatter plot: Sleep Hours vs Exam Score
axes[0, 1].scatter(df["SleepHours"], df["ExamScore"])
axes[0, 1].set_title("Sleep Hours vs Exam Score")
axes[0, 1].set_xlabel("Sleep Hours")
axes[0, 1].set_ylabel("Exam Score")

# Histogram: Exam Score Distribution
axes[1, 0].hist(df["ExamScore"], bins=10)
axes[1, 0].set_title("Exam Score Distribution")
axes[1, 0].set_xlabel("Exam Score")
axes[1, 0].set_ylabel("Frequency")

# Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, ax=axes[1, 1], cmap="coolwarm")
axes[1, 1].set_title("Feature Correlation")

plt.tight_layout()
plt.show()

# additional column for a pairplot
df["Performance"] = pd.cut(
    df["ExamScore"],
    bins=[0, 60, 80, 100, 200],
    labels=["Low", "Average", "Good", "Excellent"]
)

sns.pairplot(
    df,
    vars=["StudyHours", "SleepHours", "Attendance", "ExamScore"],
    hue="Performance",
    diag_kind="hist"
)

plt.suptitle("Student Performance Pairplot Dashboard", y=1.02)
plt.show()
import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# First 5 records
print("First 5 Records:")
print(df.head())

# Last 5 records
print("\nLast 5 Records:")
print(df.tail())

# Total rows and columns
print("\nShape of dataset:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes) 
# Total students
total_students = len(df)
print("Total Students:", total_students)

# Passed students
passed = df[df['FinalResult'] == 1].shape[0]
print("Students Passed:", passed)

# Failed students
failed = df[df['FinalResult'] == 0].shape[0]
print("Students Failed:", failed)
print("Average Study Hours:", df['StudyHours'].mean())

print("Average Attendance:", df['Attendance'].mean())

print("Maximum Previous Score:", df['PreviousScore'].max())

print("Minimum Sleep Hours:", df['SleepHours'].min())
result_counts = df['FinalResult'].value_counts()

print(result_counts)

# Percentage
percentage = df['FinalResult'].value_counts(normalize=True) * 100
print("\nPercentage Distribution:")
print(percentage)

import matplotlib.pyplot as plt

plt.hist(df['StudyHours'], bins=10)

plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()
import seaborn as sns

sns.scatterplot(x="StudyHours", y="PreviousScore", hue="FinalResult", data=df)

plt.title("Study Hours vs Previous Score")
plt.show()
sns.boxplot(y=df['Attendance'])

plt.title("Attendance Boxplot")
plt.show()
sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)

plt.title("Assignments Completed vs Final Result")
plt.show()
sns.boxplot(x="FinalResult", y="SleepHours", data=df)

plt.title("Sleep Hours vs Final Result")
plt.show()
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
print("\nDataset Shape (Rows, Columns):", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)
# Total students
print("Total Students:", len(df))

# Passed students
passed = (df["FinalResult"] == 1).sum()
print("Students Passed:", passed)

# Failed students
failed = (df["FinalResult"] == 0).sum()
print("Students Failed:", failed)
print("Average Study Hours:", df["StudyHours"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Maximum Previous Score:", df["PreviousScore"].max())
print("Minimum Sleep Hours:", df["SleepHours"].min())
result_counts = df["FinalResult"].value_counts()

print("Distribution of FinalResult:")
print(result_counts)

# Percentage
percentage = df["FinalResult"].value_counts(normalize=True) * 100
print("\nPercentage Distribution:")
print(percentage)
import matplotlib.pyplot as plt

plt.hist(df["StudyHours"], bins=10)
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()
plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")
plt.show()
import seaborn as sns

sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)
plt.title("Assignments Completed vs Final Result")
plt.show()
sns.boxplot(x="FinalResult", y="SleepHours", data=df)
plt.title("Sleep Hours vs Final Result")
plt.show()
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Features and target
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)

print("Actual Values:")
print(y_test.values)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy * 100, "%")
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.show()
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)
depth1 = DecisionTreeClassifier(max_depth=1)
depth3 = DecisionTreeClassifier(max_depth=3)
depthNone = DecisionTreeClassifier(max_depth=None)

depth1.fit(X_train, y_train)
depth3.fit(X_train, y_train)
depthNone.fit(X_train, y_train)

print("Accuracy depth=1:", depth1.score(X_test, y_test))
print("Accuracy depth=3:", depth3.score(X_test, y_test))
print("Accuracy depth=None:", depthNone.score(X_test, y_test))

student = [[6,85,66,7,7]]

prediction = model.predict(student)

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")
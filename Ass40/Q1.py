# -------------------------------
# 1. Import Required Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import plot_tree

# -------------------------------
# 2. Load Dataset
# -------------------------------
data = pd.read_csv("student_performance_ml.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# -------------------------------
# 3. Data Visualization
# -------------------------------
data.hist(figsize=(10,8))
plt.show()

# -------------------------------
# 4. Prepare Features and Target
# -------------------------------
X = data.drop("FinalResult", axis=1)
y = data["FinalResult"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# -------------------------------
# 5. Train Decision Tree Model
# -------------------------------
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# -------------------------------
# 6. Prediction
# -------------------------------
y_pred = model.predict(X_test)

print("\nPredicted vs Actual:")
comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
print(comparison.head())

# -------------------------------
# 7. Accuracy Calculation
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy * 100, "%")

# -------------------------------
# 8. Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

print("\nConfusion Matrix:")
print(cm)

print("""
True Positive (TP): Correctly predicted Pass
True Negative (TN): Correctly predicted Fail
False Positive (FP): Predicted Pass but actually Fail
False Negative (FN): Predicted Fail but actually Pass
""")

# -------------------------------
# 9. Training vs Testing Accuracy
# -------------------------------
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, y_pred)

print("Training Accuracy:", train_acc * 100)
print("Testing Accuracy:", test_acc * 100)

if train_acc > test_acc:
    print("Model may be Overfitting")
elif train_acc < test_acc:
    print("Model may be Underfitting")
else:
    print("Model is balanced")

# -------------------------------
# 10. Train with Different Depths
# -------------------------------
for depth in [1, 3, None]:
    model_depth = DecisionTreeClassifier(max_depth=depth)
    model_depth.fit(X_train, y_train)
    pred = model_depth.predict(X_test)
    acc = accuracy_score(y_test, pred)

    print("Max Depth:", depth, "Accuracy:", acc)

# -------------------------------
# 11. Predict for New Student
# -------------------------------
student = [[6, 85, 66, 7, 7]]

result = model.predict(student)

print("\nPrediction for new student:")
if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

# -------------------------------
# 12. Feature Importance
# -------------------------------
importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)

print("\nMost important feature:", X.columns[np.argmax(importance)])
print("Least important feature:", X.columns[np.argmin(importance)])

# -------------------------------
# 13. Remove SleepHours Feature
# -------------------------------
X2 = data.drop(["FinalResult", "SleepHours"], axis=1)

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X2, y, test_size=0.2, random_state=42)

model2 = DecisionTreeClassifier()
model2.fit(X_train2, y_train2)

pred2 = model2.predict(X_test2)

acc2 = accuracy_score(y_test2, pred2)

print("\nAccuracy without SleepHours:", acc2)

# -------------------------------
# 14. Train using only StudyHours & Attendance
# -------------------------------
X_small = data[["StudyHours", "Attendance"]]

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X_small, y, test_size=0.2, random_state=42)

model3 = DecisionTreeClassifier()
model3.fit(X_train3, y_train3)

pred3 = model3.predict(X_test3)

acc3 = accuracy_score(y_test3, pred3)

print("\nAccuracy using only StudyHours and Attendance:", acc3)

# -------------------------------
# 15. Predict Results for 5 New Students
# -------------------------------
new_students = pd.DataFrame({
    "StudyHours":[5,7,2,8,4],
    "Attendance":[80,90,60,95,70],
    "PreviousScore":[65,75,40,88,55],
    "AssignmentsCompleted":[6,8,3,9,5],
    "SleepHours":[7,6,8,7,6]
})

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions

print("\nPredictions for New Students:")
print(new_students)

# -------------------------------
# 16. Manual Accuracy Calculation
# -------------------------------
correct = np.sum(y_test == y_pred)
manual_accuracy = correct / len(y_test)

print("\nManual Accuracy:", manual_accuracy)

# -------------------------------
# 17. Misclassified Students
# -------------------------------
misclassified = X_test[y_test != y_pred]

print("\nMisclassified Students:")
print(misclassified)

print("Number of Misclassified:", len(misclassified))

# -------------------------------
# 18. Train Model with Different Random States
# -------------------------------
for rs in [0,10,42]:
    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
        X, y, test_size=0.2, random_state=rs)

    model_r = DecisionTreeClassifier()
    model_r.fit(X_train_r, y_train_r)

    pred_r = model_r.predict(X_test_r)

    acc_r = accuracy_score(y_test_r, pred_r)

    print("Random State:", rs, "Accuracy:", acc_r)

# -------------------------------
# 19. Decision Tree Visualization
# -------------------------------
plt.figure(figsize=(15,8))
plot_tree(model, feature_names=X.columns, class_names=["Fail","Pass"], filled=True)
plt.show()

# -------------------------------
# 20. Create New Feature PerformanceIndex
# -------------------------------
data["PerformanceIndex"] = (data["StudyHours"] * 2) + data["Attendance"]

X_new = data.drop("FinalResult", axis=1)

X_train4, X_test4, y_train4, y_test4 = train_test_split(
    X_new, y, test_size=0.2, random_state=42)

model4 = DecisionTreeClassifier()
model4.fit(X_train4, y_train4)

pred4 = model4.predict(X_test4)

acc4 = accuracy_score(y_test4, pred4)

print("\nAccuracy with PerformanceIndex:", acc4)

# -------------------------------
# 21. Overfitting Explanation
# -------------------------------
model_final = DecisionTreeClassifier(max_depth=None)
model_final.fit(X_train, y_train)

train_final = accuracy_score(y_train, model_final.predict(X_train))
test_final = accuracy_score(y_test, model_final.predict(X_test))

print("\nTraining Accuracy:", train_final)
print("Testing Accuracy:", test_final)

print("""
If training accuracy = 100% but testing accuracy is lower,
the model has memorized training data and cannot generalize
well on unseen data. This is called OVERFITTING.
""")
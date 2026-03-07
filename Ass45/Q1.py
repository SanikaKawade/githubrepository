from sklearn.datasets import load_wine
import pandas as pd

# Load dataset
wine = load_wine()

# Create dataframe
data = pd.DataFrame(wine.data, columns=wine.feature_names)

# Add target column
data['target'] = wine.target

print(data.head())
# Check missing values
print(data.isnull().sum())

# Features and labels
X = data.drop('target', axis=1)
y = data['target']

print(X.head())
print(y.head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Split data
X_train, X_test, y_train, y_test = train_test_split( X_scaled, y, test_size=0.3, random_state=42)

# Train model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)
from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
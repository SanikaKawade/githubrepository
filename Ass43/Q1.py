import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -------------------------------
# Step 1 : Get Data
# -------------------------------

data = pd.read_csv("PlayPredictor.csv")

print("Dataset:\n")
print(data)

# -------------------------------
# Step 2 : Clean, Prepare Data
# -------------------------------

le = LabelEncoder()

data['Whether'] = le.fit_transform(data['Whether'])
data['Temperature'] = le.fit_transform(data['Temperature'])
data['Play'] = le.fit_transform(data['Play'])

print("\nEncoded Dataset:\n")
print(data)

# Features and Target
X = data[['Whether','Temperature']]
Y = data['Play']

# -------------------------------
# Step 3 : Train Model (KNN)
# -------------------------------

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,Y)

print("\nModel Training Completed")

# -------------------------------
# Step 4 : Test Data
# -------------------------------

# Example input
# Sunny = 2 , Overcast = 0 , Rainy = 1
# Hot = 1 , Mild = 2 , Cool = 0

test = [[2,1]]   # Sunny, Hot

result = model.predict(test)

if result == 1:
    print("\nPrediction : Play = YES")
else:
    print("\nPrediction : Play = NO")

# -------------------------------
# Step 5 : Calculate Accuracy
# -------------------------------

def CheckAccuracy(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(Y_test,pred)

    return acc

accuracy = CheckAccuracy(X,Y)

print("\nAccuracy of Algorithm =",accuracy*100,"%")
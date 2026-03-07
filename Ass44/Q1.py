import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------------
# Step 1 : Get Data
# -----------------------------------

data = pd.read_csv("Advertising.csv")

print("Dataset:\n")
print(data)

# -----------------------------------
# Step 2 : Clean, Prepare Data
# -----------------------------------

X = data[['TV','radio','newspaper']]   # Features
Y = data['sales']                      # Target

# -----------------------------------
# Step 3 : Train Data
# -----------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5)

model = LinearRegression()

model.fit(X_train,Y_train)

print("\nModel Training Completed")

# -----------------------------------
# Step 4 : Test Data
# -----------------------------------

predictions = model.predict(X_test)

print("\nPredicted Sales:\n")
print(predictions)

# -----------------------------------
# Step 5 : Display Expected vs Predicted
# -----------------------------------

result = pd.DataFrame({
    "Actual Sales":Y_test,
    "Predicted Sales":predictions
})

print("\nComparison of Actual and Predicted Sales\n")
print(result)
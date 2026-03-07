# Dataset
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

n = len(X)

# Mean of X and Y
mean_x = sum(X) / n
mean_y = sum(Y) / n

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# Calculate intercept (c)
c = mean_y - m * mean_x

print("Slope (m) =", round(m,2))
print("Intercept (c) =", round(c,2))

print("Regression Equation: Y =", round(m,2),"X +", round(c,2))

# Prediction
x_new = 6
y_pred = m * x_new + c

print("Predicted Y for X = 6 :", round(y_pred,2))
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)

num = sum((X[i]-mean_x)*(Y[i]-mean_y) for i in range(len(X)))
den = sum((X[i]-mean_x)**2 for i in range(len(X)))

m = num/den
c = mean_y - m*mean_x

# Predicted values
Y_pred = []
for x in X:
    Y_pred.append(m*x + c)

print("Predicted Y values:", Y_pred)

# Mean Squared Error
mse = sum((Y[i] - Y_pred[i])**2 for i in range(len(Y))) / len(Y)

# R2 Score
ss_total = sum((y - mean_y)**2 for y in Y)
ss_res = sum((Y[i] - Y_pred[i])**2 for i in range(len(Y)))

r2 = 1 - (ss_res/ss_total)

print("MSE =", round(mse,3))
print("R² Score =", round(r2,3))
import matplotlib.pyplot as plt

experience = [1,2,3,4,5]
salary = [20000,25000,30000,35000,40000]

n = len(experience)

mean_x = sum(experience)/n
mean_y = sum(salary)/n

num = sum((experience[i]-mean_x)*(salary[i]-mean_y) for i in range(n))
den = sum((experience[i]-mean_x)**2 for i in range(n))

m = num/den
c = mean_y - m*mean_x

# Prediction
x_new = 6
predicted_salary = m*x_new + c

print("Predicted Salary for 6 Years Experience: ₹", int(predicted_salary))

# Plot graph
plt.scatter(experience, salary)
line = [m*x + c for x in experience]
plt.plot(experience, line)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")

plt.show()
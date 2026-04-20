import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Import dataset
dataset = pd.read_csv("Salary.csv")

# Step 2: Independent and Dependent variables
X = dataset[["YearsExperience"]].values
y = dataset["Salary"].values

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

# Step 4: Train model (slope & intercept calculated internally)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Show slope and intercept (IMPORTANT for exam)
print("Slope (m):", regressor.coef_[0])
print("Intercept (c):", regressor.intercept_)

# Step 5: Prediction
y_pred = regressor.predict(X_test)

# Step 6: Plot Best Fit Line (Training set)
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Plot Test set
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Step 7: Model Evaluation
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

# Step 8: Single prediction
experience = 5
print("Predicted Salary:", regressor.predict([[experience]])[0])

# Slope (m): 8528.002056992886
# Intercept (c): 30653.80404187284
# RMSE: 4685.185783311836
# R2 Score: 0.9714499470616078
# Predicted Salary: 73293.81432683728

# pip install pandas numpy matplotlib scikit-learn
# !mamba install pandas numpy matplotlib scikit-learn
# pip install scikit-learn
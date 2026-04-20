import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings("ignore")

ts = pd.Series([
    25, 25.8, 26.1, 27.4, 28.9, 29.5, 30.1, 31.8,
    30.2, 29.9, 28.0, 27.2, 26.9, 28.5, 27.8, 29.9,
    31.2, 32.5, 31.0, 30.4, 29.1, 27.6, 26.8, 26.2
])

ts.index = pd.date_range("2023-01", periods=len(ts), freq="M")

ts.plot(title="Time Series Data", marker="o")
plt.show()

print("ADF p-value:", adfuller(ts)[1])
print("Is Stationary:", adfuller(ts)[1] < 0.05)

plot_acf(ts); plt.show()
plot_pacf(ts); plt.show()

train, test = ts[:20], ts[20:]

model = ARIMA(train, order=(2,1,2))
model_fit = model.fit()

model_fit.plot_diagnostics(figsize=(10, 6))
plt.tight_layout()
plt.show()

pred = model_fit.forecast(len(test))

mse = mean_squared_error(test, pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(test, pred)
accuracy = 100 - (mae / test.mean()) * 100
print("Model Performance:")
print("MSE  :", round(mse,3))
print("RMSE :", round(rmse,3))
print("MAE  :", round(mae,3))
print("Accuracy (%):", round(accuracy,2))

plt.plot(train.index, train, label="Train")
plt.plot(test.index, test, label="Test", marker="o")
plt.plot(test.index, pred, label="Forecast", marker="o")
plt.legend()
plt.title("ARIMA Forecast")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()

# ADF p-value: 0.31058704205305154
# Is Stationary: False
# Model Performance:
# MSE  : 5.629
# RMSE : 2.373
# MAE  : 2.075
# Accuracy (%): 92.44

# pip install pandas numpy matplotlib statsmodels scikit-learn
# pip install --upgrade pip
# pip install statsmodels
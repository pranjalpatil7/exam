import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

ts = pd.Series([
    25, 25.8, 26.1, 27.4, 28.9, 29.5, 30.1, 31.8, 30.2, 29.9,
    28.0, 27.2, 26.9, 28.5, 27.8, 29.9, 31.2, 32.5, 31.0, 30.4,
    29.1, 27.6, 26.8, 26.2
])

ts.index = pd.date_range("2023-01", periods=len(ts), freq="M")

ts.plot(title="Temperature Time Series", marker="o")
plt.show()

print("ADF p-value:", adfuller(ts)[1])
print("Is Stationary:", adfuller(ts)[1] < 0.05)

plot_acf(ts); plt.show()
plot_pacf(ts); plt.show()

train, test = ts[:20], ts[20:]

models = {
    "AR": (2,0,0),
    "MA": (0,0,2),
    "ARMA": (2,0,2)
}

results = {}

plt.figure()

plt.plot(train.index, train, label="Train")
plt.plot(test.index, test, label="Test", marker="o")

for name, order in models.items():
    pred = ARIMA(train, order=order).fit().forecast(len(test))
    rmse = np.sqrt(mean_squared_error(test, pred))
    results[name] = rmse

    plt.plot(test.index, pred, label=name)

plt.legend()
plt.title("AR vs MA vs ARMA Forecast")
plt.show()

print("\nRMSE Results:")
for name, rmse in results.items():
    print(name, ":", round(rmse, 3))

print("\nBest Model:", min(results, key=results.get))

# ADF p-value: 0.31058704205305154
# Is Stationary: False

# RMSE Results:
# AR : 1.993
# MA : 1.791
# ARMA : 0.19

# Best Model: ARMA

# pip install pandas numpy matplotlib statsmodels scikit-learn
# pip install --upgrade pip
# pip install statsmodels
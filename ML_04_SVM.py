import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv("Social_Network_Ads.csv")

X = data[["Age", "EstimatedSalary"]].values
y = data["Purchased"].values

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
classifier = SVC(kernel="linear")
classifier.fit(X_train, y_train)

# Predict + Evaluation
y_pred = classifier.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Visualization function (short)
def plot(X, y, title):
    xx, yy = np.meshgrid(
        np.arange(X[:,0].min()-1, X[:,0].max()+1, 0.01),
        np.arange(X[:,1].min()-1, X[:,1].max()+1, 0.01)
    )

    plt.contourf(xx, yy,
        classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape),
        alpha=0.3
    )

    plt.scatter(X[:,0], X[:,1], c=y, edgecolors="k")
    plt.title(title)
    plt.show()

plot(X_train, y_train, "Training Set")
plot(X_test, y_test, "Test Set")

# Confusion Matrix:
#  [[66  2]
#  [ 8 24]]
# Accuracy: 0.9
#pip install numpy pandas matplotlib scikit-learn

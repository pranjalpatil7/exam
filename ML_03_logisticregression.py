import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Load dataset
data = pd.read_csv("diabetes.csv")

# Features and target
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Feature scaling
X = StandardScaler().fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Confusion Matrix
cm = metrics.confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Heatmap
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

# Classification Report
print("\nClassification Report:\n", metrics.classification_report(y_test, y_pred))

# ROC & AUC
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = metrics.roc_curve(y_test, y_prob)
auc = metrics.roc_auc_score(y_test, y_prob)

plt.plot(fpr, tpr, label="AUC = " + str(round(auc, 2)))
plt.plot([0, 1], [0, 1], "--")
plt.title("ROC Curve")
plt.legend()
plt.show()

print("AUC Score:", round(auc, 2))

# Accuracy: 0.8020833333333334

# Confusion Matrix:
#  [[118  12]
#  [ 26  36]]

# Classification Report:
#                precision    recall  f1-score   support

#            0       0.82      0.91      0.86       130
#            1       0.75      0.58      0.65        62

#     accuracy                           0.80       192
#    macro avg       0.78      0.74      0.76       192
# weighted avg       0.80      0.80      0.79       192

# AUC Score: 0.86

#pip install pandas matplotlib seaborn scikit-learn
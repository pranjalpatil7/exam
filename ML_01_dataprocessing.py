import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load dataset
data = pd.read_csv('StudentsPerformance.csv', on_bad_lines='skip')

# Preview dataset
print("Dataset Preview:")
print(data.head())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Separate numeric and categorical columns
numeric_cols = data.select_dtypes(include=[np.number]).columns
categorical_cols = data.select_dtypes(include=['object']).columns

# Fill missing values
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Remove duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
data.drop_duplicates(inplace=True)

# Normalize numeric columns
scaler = MinMaxScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

print("\nNormalized Data:")
print(data.head())

# Encode categorical columns
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

print("\nData after Encoding:")
print(data.head())

# Plot histograms
data.hist(figsize=(10,8))
plt.suptitle("Histograms of Features")
plt.show()

# Scatter plot (use first 2 numeric columns)
num_cols = data.select_dtypes(include=[np.number]).columns

plt.scatter(data[num_cols[0]], data[num_cols[1]])
plt.xlabel(num_cols[0])
plt.ylabel(num_cols[1])
plt.title(f"{num_cols[0]} vs {num_cols[1]}")
plt.show()

# Save processed dataset
data.to_csv('preprocessed_students.csv', index=False)

print("\nPreprocessed data saved as 'preprocessed_students.csv'")

# pip install pandas numpy matplotlib scikit-learn
# !mamba install pandas numpy matplotlib scikit-learn
# pip install scikit-learn

# Dataset Preview:
#    gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
# 0  female        group B           bachelor's degree      standard                    none          72             72             74
# 1  female        group C                some college      standard               completed          69             90             88
# 2  female        group B             master's degree      standard                    none          90             95             93
# 3    male        group A          associate's degree  free/reduced                    none          47             57             44
# 4    male        group C                some college      standard                    none          76             78             75

# Missing Values:
# gender                         0
# race/ethnicity                 0
# parental level of education    0
# lunch                          0
# test preparation course        0
# math score                     0
# reading score                  0
# writing score                  0
# dtype: int64

# Duplicate Rows: 0

# Normalized Data:
#    gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
# 0  female        group B           bachelor's degree      standard                    none        0.72       0.662651       0.711111     
# 1  female        group C                some college      standard               completed        0.69       0.879518       0.866667     
# 2  female        group B             master's degree      standard                    none        0.90       0.939759       0.922222     
# 3    male        group A          associate's degree  free/reduced                    none        0.47       0.481928       0.377778     
# 4    male        group C                some college      standard                    none        0.76       0.734940       0.722222     
# 1        0.69       0.879518       0.866667  ...                                         False            True                         False
# 2        0.90       0.939759       0.922222  ...                                         False            True                          True
# 3        0.47       0.481928       0.377778  ...                                         False           False                          True
# 4        0.76       0.734940       0.722222  ...                                         False            True                          True

# [5 rows x 15 columns]

# Preprocessed data saved as 'preprocessed_students.csv'
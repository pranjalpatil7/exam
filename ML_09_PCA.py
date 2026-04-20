import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load dataset
data = pd.read_csv("StudentsPerformance.csv")

# STEP 2: Convert categorical to numeric
data = pd.get_dummies(data, drop_first=True)

# STEP 3: Convert to numpy array
X = data.values.astype(float)

# STEP 4: Standardize data
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
Z = (X - X_mean) / X_std

# STEP 5: Covariance matrix
cov_matrix = np.cov(Z.T)

# STEP 6: Eigenvalues & Eigenvectors
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)

# STEP 7: Sort eigenvalues (descending)
idx = np.argsort(eig_vals)[::-1]
eig_vals = eig_vals[idx]
eig_vecs = eig_vecs[:, idx]

# STEP 8: Select top 2 principal components
k = 2
principal_components = eig_vecs[:, :k]

# STEP 9: Transform data (PCA projection)
X_pca = np.dot(Z, principal_components)

# STEP 10: Reconstruction (for visualization idea)
X_reconstructed = np.dot(X_pca, principal_components.T) + X_mean

# OUTPUT
print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
print("\nVariance Explained:", eig_vals[:k] / np.sum(eig_vals))

# Better PCA visualization (clean and correct)
plt.figure(figsize=(6,5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
plt.title("PCA - 2D Projection")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid()
plt.show()

#pip install numpy pandas matplotlib
#Original Shape: (1000, 15)
# Reduced Shape: (1000, 2)

# Variance Explained: [0.20489504 0.09711489]
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(10)

# Step 1: Generate dataset (2 clusters)
X = np.r_[np.random.normal(2.5, 0.9, 300),
          np.random.normal(-1.5, 0.7, 700)]

N, K = len(X), 2

# Step 2: Initialize parameters
means = np.random.choice(X, K)
stds = np.random.rand(K) + 0.5
weights = np.ones(K) / K

log_likelihood = []

# Step 3: EM Algorithm
for i in range(50):

    # E-step (responsibility calculation)
    r = np.zeros((N, K))
    for k in range(K):
        r[:, k] = weights[k] * norm.pdf(X, means[k], stds[k])

    r /= r.sum(axis=1, keepdims=True)

    # M-step (update parameters)
    Nk = r.sum(axis=0)
    means = (r.T @ X) / Nk
    stds = np.sqrt((r * (X[:, None] - means) ** 2).sum(axis=0) / Nk)
    weights = Nk / N

    # Log-likelihood
    ll = np.sum(np.log(np.sum(r, axis=1)))
    log_likelihood.append(ll)

    # Stop condition (safe)
    if i > 5 and abs(log_likelihood[-1] - log_likelihood[-2]) < 1e-6:
        break

print("Iterations:", len(log_likelihood))

# Step 4: Plot convergence
plt.plot(log_likelihood)
plt.title("EM Convergence")
plt.xlabel("Iteration")
plt.ylabel("Log-Likelihood")
plt.show()

# Step 5: Final distribution plot
x = np.linspace(min(X), max(X), 1000)

plt.hist(X, bins=40, density=True, alpha=0.4)

for k in range(K):
    plt.plot(x, weights[k] * norm.pdf(x, means[k], stds[k]), '--')

plt.plot(x, sum(weights[k] * norm.pdf(x, means[k], stds[k]) for k in range(K)))

plt.title("Gaussian Mixture Model (EM)")
plt.legend(["Component 1", "Component 2", "Mixture"])
plt.show()

#Iterations: 7
#pip install numpy matplotlib scipy

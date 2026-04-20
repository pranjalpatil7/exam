import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = 0

    # Step activation function
    def step(self, z):
        return 1 if z >= 0 else 0

    # Training
    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])

        for _ in range(self.epochs):
            for i in range(len(X)):
                z = np.dot(X[i], self.w) + self.b
                err = y[i] - self.step(z)

                self.w += self.lr * err * X[i]
                self.b += self.lr * err

    # Prediction
    def predict(self, x):
        z = np.dot(x, self.w) + self.b
        return self.step(z)

# Input data (AND / OR)
X = np.array([[0,0],[0,1],[1,0],[1,1]])

# AND Gate
print("AND Gate:")
y_and = [0,0,0,1]
p = Perceptron()
p.fit(X, y_and)

for x in X:
    print(x, "->", p.predict(x))

# OR Gate
print("\nOR Gate:")
y_or = [0,1,1,1]
p = Perceptron()
p.fit(X, y_or)

for x in X:
    print(x, "->", p.predict(x))

#pip install numpy

# AND Gate:
# [0 0] -> 0
# [0 1] -> 0
# [1 0] -> 0
# [1 1] -> 1

# OR Gate:
# [0 0] -> 0
# [0 1] -> 1
# [1 0] -> 1
# [1 1] -> 1
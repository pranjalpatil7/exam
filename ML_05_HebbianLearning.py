import numpy as np
import matplotlib.pyplot as plt

# Step 1: Bipolar input patterns
inputs = np.array([
    [1, -1],
    [1,  1],
    [-1, -1],
    [-1,  1]
])

# Step 2: Select logic gate
gate = input("Enter logic gate (AND / OR): ").upper()

if gate == "AND":
    targets = np.array([-1, 1, -1, -1])
elif gate == "OR":
    targets = np.array([1, 1, -1, 1])
else:
    print("Invalid gate selection")
    exit()

# Step 3: Initialization
weights = np.zeros(2)
bias = 0
eta = 0.5

print("\nTraining Phase ")

# Step 4: Hebbian Training
for i in range(len(inputs)):
    x = inputs[i]
    y = targets[i]

    weights += eta * x * y
    bias += eta * y

    print(f"Pattern {i+1}: Weights = {weights}, Bias = {bias}")

print("\nTraining Completed")
print("Final Weights:", weights)
print("Final Bias:", bias)

# Step 5: Testing
print("\nTesting Phase ")
outputs = []

for x in inputs:
    net = np.dot(weights, x) + bias
    out = 1 if net >= 0 else -1
    outputs.append(out)
    print("Input:", x, "Output:", out)

# Step 6: Plot
plt.figure()

for i in range(len(inputs)):
    plt.scatter(inputs[i][0], inputs[i][1],
                marker='o' if outputs[i]==1 else 'x')

x_vals = np.linspace(-2, 2, 100)

if weights[1] != 0:
    y_vals = -(weights[0] * x_vals + bias) / weights[1]
    plt.plot(x_vals, y_vals)

plt.xlabel("Input x1")
plt.ylabel("Input x2")
plt.title(f"Hebbian Learning Decision Boundary ({gate})")
plt.grid(True)
plt.show()

#pip install numpy matplotlib

# Enter logic gate (AND / OR): OR

# Training Phase
# Pattern 1: Weights = [ 0.5 -0.5], Bias = 0.5
# Pattern 2: Weights = [1. 0.], Bias = 1.0
# Pattern 3: Weights = [1.5 0.5], Bias = 0.5
# Pattern 4: Weights = [1. 1.], Bias = 1.0

# Training Completed
# Final Weights: [1. 1.]
# Final Bias: 1.0

# Testing Phase
# Input: [ 1 -1] Output: 1
# Input: [1 1] Output: 1
# Input: [-1 -1] Output: -1
# Input: [-1  1] Output: 1


# Enter logic gate (AND / OR): AND

# Training Phase
# Pattern 1: Weights = [-0.5  0.5], Bias = -0.5
# Pattern 2: Weights = [0. 1.], Bias = 0.0
# Pattern 3: Weights = [0.5 1.5], Bias = -0.5
# Pattern 4: Weights = [1. 1.], Bias = -1.0

# Training Completed
# Final Weights: [1. 1.]
# Final Bias: -1.0

# Testing Phase
# Input: [ 1 -1] Output: -1
# Input: [1 1] Output: 1
# Input: [-1 -1] Output: -1
# Input: [-1  1] Output: -1
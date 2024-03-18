import numpy as np
import matplotlib.pyplot as plt

# Define the system dynamics: x_dot = A * x
A = np.array([[0, 1], [-1, -1]])  # State matrix

# Define the Lyapunov function candidate V(x) = x' * P * x
P = np.eye(2)  # Positive definite matrix P

# Define the time vector
t = np.linspace(0, 10, 1000)  # Time vector from 0 to 10 with 1000 points

# Initialize the state vector x
x0 = np.array([1, 1])  # Initial condition
x = np.zeros((len(t), len(x0)))
x[0] = x0

# Simulate the system dynamics using Euler's method
for i in range(1, len(t)):
    x_dot = np.dot(A, x[i-1])
    x[i] = x[i-1] + x_dot * (t[i] - t[i-1])

# Compute the Lyapunov function V(x) for each state vector x
V = np.zeros(len(t))
for i in range(len(t)):
    V[i] = np.dot(np.dot(x[i].T, P), x[i])

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, V, label='Lyapunov Function $V(x)$')
plt.xlabel('Time')
plt.ylabel('Lyapunov Function Value')
plt.title('Lyapunov Stability Test')
plt.legend()
plt.grid(True)
plt.show()

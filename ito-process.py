import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0  # Time horizon
N = 1000  # Number of time steps
dt = T / N  # Time step size
mu = 0.1  # Drift coefficient
sigma = 0.2  # Diffusion coefficient

# Initial value of the process
S0 = 100.0

# Generate Brownian motion increments
t = np.linspace(0.0, T, N+1)
W = np.random.standard_normal(size=N+1)
W[0] = 0.0  # Set the initial value of the Brownian motion to zero
W = np.cumsum(W) * np.sqrt(dt)  # Cumulative sum for Brownian motion

# Generate Ito process increments
dS = mu * S0 * dt + sigma * S0 * W[:-1]  # Ito process increments
S = np.cumsum(dS)  # Cumulative sum for Ito process

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t[:-1], S, label='Ito Process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Simulated Ito Process')
plt.legend()
plt.grid(True)
plt.show()

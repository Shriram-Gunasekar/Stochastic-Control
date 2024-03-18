import numpy as np

# Define parameters
num_steps = 1000
num_simulations = 1000
epsilon = 0.1

# Generate random normal increments
increments = np.random.normal(0, 1, size=(num_simulations, num_steps))

# Create an empty array to store the martingale values
martingale_values = np.zeros((num_simulations, num_steps + 1))
martingale_values[:, 0] = 0  # Initial value of the martingale is 0

# Compute the martingale values
for t in range(num_steps):
    martingale_values[:, t + 1] = martingale_values[:, t] + increments[:, t]

# Compute the maximum absolute value of the martingale
max_martingale = np.max(np.abs(martingale_values), axis=1)

# Compute the upper bound using the BDG inequality
upper_bound = epsilon * np.sqrt(num_steps)

# Check if the BDG inequality holds for each simulation
is_bdg_satisfied = max_martingale <= upper_bound

# Calculate the percentage of simulations where the BDG inequality holds
percentage_bdg_satisfied = np.mean(is_bdg_satisfied) * 100

print(f"Percentage of simulations where BDG inequality holds: {percentage_bdg_satisfied}%")

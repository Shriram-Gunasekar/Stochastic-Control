import numpy as np
import matplotlib.pyplot as plt

# Define the number of functions and their domain
num_functions = 100
domain = np.linspace(0, 1, 1000)

# Generate random coefficients for the functions
coefficients = np.random.randn(num_functions, len(domain))

# Define the functions using the random coefficients
functions = [np.poly1d(coeffs) for coeffs in coefficients]

# Evaluate the functions on the domain
function_values = [func(domain) for func in functions]

# Plotting the functions
plt.figure(figsize=(10, 6))
for values in function_values:
    plt.plot(domain, values, alpha=0.5)  # Use alpha for transparency

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Randomly Generated Functions')
plt.grid(True)
plt.show()

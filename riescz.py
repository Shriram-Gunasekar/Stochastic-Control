import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.linalg import sqrtm

# Define the interval [a, b]
a = 0
b = 1

# Define the linear functional to be represented
def linear_functional(f):
    return quad(lambda x: f(x) * np.exp(x), a, b)[0]

# Define the space L2([a, b])
def L2_function(x):
    return np.sin(2 * np.pi * x)  # Example L2 function

# Define the inner product on L2([a, b])
def inner_product(f, g):
    return quad(lambda x: f(x) * g(x), a, b)[0]

# Define the function to minimize
def objective_function(alpha):
    def phi(x):
        return L2_function(x) * alpha
    return np.abs(linear_functional(phi)) ** 2

# Find the optimal alpha using numerical optimization
initial_guess = np.array([1.0])
result = minimize(objective_function, initial_guess)

# Get the optimal alpha
optimal_alpha = result.x[0]
print(f"Optimal alpha: {optimal_alpha}")

# Calculate the Riesz representation integral
integral_value = quad(lambda x: L2_function(x) * optimal_alpha * np.exp(x), a, b)[0]
print(f"Integral value representing the linear functional: {integral_value}")

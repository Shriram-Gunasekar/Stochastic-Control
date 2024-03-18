import numpy as np
from scipy.integrate import dblquad

# Define the joint probability density function (PDF)
def joint_pdf(x, y):
    return 2 * x * y  # Example PDF: f(x, y) = 2xy

# Define the limits of integration
x_lower = 0
x_upper = 1
y_lower = 0
y_upper = 1

# Integrate the joint PDF using Fubini's theorem
result, _ = dblquad(lambda y, x: joint_pdf(x, y), y_lower, y_upper, x_lower, x_upper)

print(f"Result of double integral using Fubini's theorem: {result}")

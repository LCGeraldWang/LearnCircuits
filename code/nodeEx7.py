import numpy as np

# Coefficients of the equations
# Equation 1: 8 - 2 - (V1/3) - (V2/6) - ((V2 - V3)/2) = 0
# Equation 2: V2 - V1 = 12
# Equation 3: 2 + ((V2 - V3)/2) - (V3/1) = 0

# Represent the equations in matrix form: A * [V1, V2, V3] = B
A = np.array([
    [-1/3, -1/6 - 1/2, 1/2],  # Coefficients from Equation 1
    [-1, 1, 0],               # Coefficients from Equation 2
    [0, 1/2, -1/2 - 1]        # Coefficients from Equation 3
])

B = np.array([
    -6,  # Constant from Equation 1 (8 - 2 = 6, moved to the right-hand side)
    12,  # Constant from Equation 2
    -2   # Constant from Equation 3 (2 moved to the right-hand side)
])

# Solve the system of equations
solutions = np.linalg.solve(A, B)

# Extract the solutions
V1, V2, V3 = solutions

# Print the results
print(f"V1 = {V1:.2f} V")
print(f"V2 = {V2:.2f} V")
print(f"V3 = {V3:.2f} V")